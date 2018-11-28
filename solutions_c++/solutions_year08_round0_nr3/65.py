#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define EPS 1e-9

typedef struct Point {
  long double x, y;
  Point() { x = 0; y = 0; }
  Point(long double a, long double b) { x = a; y = b; }
  Point operator+(const Point &p) { Point res; res.x = this->x + p.x, res.y = this->y + p.y; return res; }
  Point operator-(const Point &p) { Point res; res.x = this->x - p.x, res.y = this->y - p.y; return res; }
  long double operator*(const Point &p) { return this->x * p.y - this->y * p.x; }
} Point;
vector< Point > convex_hull(vector< Point > v) {
  vector<Point> ret;
  int p = 0, start = 0, used[v.size()];
  memset(used, 0, sizeof(used));
  for (int i = 1; i < v.size(); ++i)
    if ((v[i].x < v[p].x) || ((v[i].x == v[p].x) && (v[i].y < v[p].y)))
      p = start = i;
  ret.push_back(v[p]);
  do {
    long double dist = 0;
    int n = -1;
    for (int i = 0; i < v.size(); ++i) if (i != p && !used[i]) {
	if (n == -1) n = i;
	long double cross = (v[i] - v[p]) * (v[n] - v[p]);
	Point x = v[i] - v[p];
	long double d = x.x*x.x + x.y*x.y;
	if (cross < 0) n = i, dist = d;
	else if (cross==0 && d > dist) dist = d, n = i;
      }
    ret.push_back(v[n]);
    p = n, used[n] = 1;
  } while (start != p);
  return ret;
}
long double convex_area(vector< Point > v) {
  long double ret = 0;
  for (int i = 0; i + 1 < v.size(); ++i)
    ret += v[i].x * v[i+1].y - v[i].y * v[i+1].x;
  return fabs(ret) / 2;
}

// calculate area of circle of radius r centered at the origin that lies
// on the smaller side of the chord defined by (x1,y1) and (x2,y2)
long double calc_segment(long double x1, long double y1, long double x2, long double y2, long double r) {
  long double xav = (x1 + x2) / 2, yav = (y1 + y2) / 2;
  long double d = sqrt(xav*xav+yav*yav), h = r - d;
  return r*r*fabs(acos((r-h)/r)) - (r-h)*sqrt(2*r*h - h*h);
}

int main() {
  int no_tests;
  cin >> no_tests;
  for (int rr = 1; rr <= no_tests; ++rr) {
    long double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;
    long double Rt = R - t, Rtf = Rt - f;
    
    if (g <= 2*f) {
      printf("Case #%d: 1.000000\n", rr);
      continue;
    }
    
    long double safe_area = 0, tot_area = M_PI*R*R/4;
    for (long double atx = r; atx < Rt; atx += g + 2*r) 
      for (long double aty = r; aty < Rt; aty += g + 2*r) {
	long double x1 = atx + f, x2 = atx + g - f;
	long double y1 = aty + f, y2 = aty + g - f;
	vector< Point > inside, intersections;
	if (x1*x1+y1*y1 <= Rtf*Rtf)
	  inside.push_back(Point(x1, y1));
	if (x1*x1+y2*y2 <= Rtf*Rtf)
	  inside.push_back(Point(x1, y2));
	if (x2*x2+y1*y1 <= Rtf*Rtf)
	  inside.push_back(Point(x2, y1));
	if (x2*x2+y2*y2 <= Rtf*Rtf)
	  inside.push_back(Point(x1, y1));
	
	// figure out the intersections with vertical segments
	long double A = Rtf*Rtf - x1*x1;
	if (A >= 0) {
	  long double y = sqrt(A);
	  if (y>=y1 && y<=y2)
	    intersections.push_back(Point(x1, y));
	  if (-y>=y1 && -y<=y2 && fabs(y)>EPS)
	    intersections.push_back(Point(x1, -y));
	}
	A = Rtf*Rtf - x2*x2;
	if (A >= 0) {
	  long double y = sqrt(A);
	  if (y>=y1 && y<=y2)
	    intersections.push_back(Point(x2, y));
	  if (-y>=y1 && -y<=y2 && fabs(y)>EPS)
	    intersections.push_back(Point(x2, -y));
	}
	
	// figure out the intersections with horizontal segments
	A = Rtf*Rtf - y1*y1;
	if (A >= 0) {
	  long double x = sqrt(A);
	  if (x>=x1 && x<=x2)
	    intersections.push_back(Point(x, y1));
	  if (-x>=x1 && -x<=x2 && fabs(x)>EPS)
	    intersections.push_back(Point(-x, y1));
	}
	A = Rtf*Rtf - y2*y2;
	if (A >= 0) {
	  long double x = sqrt(A);
	  if (x>=x1 && x<=x2)
	    intersections.push_back(Point(x, y2));
	  if (-x>=x1 && -x<=x2 && fabs(x)>EPS)
	    intersections.push_back(Point(-x, y2));
	}
	
	if (inside.size() == 4)
	  safe_area += (x2-x1)*(y2-y1);
	else if (intersections.size()) {
	  if (intersections.size() != 2)
	    fprintf(stderr, "something is wrong\n");
	  inside.push_back(intersections[0]);
	  inside.push_back(intersections[1]);
	  safe_area += convex_area(convex_hull(inside));
	  safe_area += calc_segment(intersections[0].x, intersections[0].y,
				    intersections[1].x, intersections[1].y, Rtf);
	}
      }
    printf("Case #%d: %.6Lf\n", rr, 1. - safe_area/tot_area);
  }
  return 0;
}
