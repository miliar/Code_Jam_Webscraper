#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

const double eps = 1e-8;
const double pi = acos(-1.0);

/** Return a float number's sign */
inline int sign(double d) {
    return d < -eps ? -1 : d > eps;
}

inline double sqr(double x) {
    return x * x;
}

struct Point {
    double x, y;
    Point() { x = 0.0; y=0.0; }
    Point(double nx, double ny) : x(nx), y(ny) {}
    Point TurnLeft() const {
        return Point(-y, x);
    }
    Point TurnRight() const {
        return Point(y, -x);
    }
    Point Rotate(double ang) const {
        return Point(x * cos(ang) - y * sin(ang), x * sin(ang) + y * cos(ang));
    }
        double Length()
        {
                return sqrt(x*x + y*y);
        }
        void Normalize()
        {
                double r = Length();
                if (sign(r)!=0)
                        x/=r,y/=r;
        }
        bool operator < (const Point & other)
        {
                return sign(y - other.y) < 0 || sign(y - other.y) == 0 && sign(x - other.x) < 0;
        }

        friend ostream & operator << (ostream & out , const Point & point)
        {
                out<<point.x<<" "<<point.y;
                return out;
        }

};

inline Point operator + (const Point & a, const Point & b) {
    return Point(a.x + b.x, a.y + b.y);
}

inline Point operator - (const Point & a , const Point & b) {
    return Point(a.x - b.x, a.y - b.y);
}

inline Point operator * (const Point & a , double d) {
    return Point(a.x * d, a.y * d);
}

inline Point operator / (const Point & a , double d) {
        if (sign(d)==0) return Point();
    return Point(a.x / d, a.y / d);
}

inline bool operator == (const Point & a , const Point & b) {
    return sign(a.x - b.x) == 0 && sign(a.y - b.y) == 0;
}

inline bool operator != (const Point & a , const Point & b) {
    return sign(a.x - b.x) || sign(a.y - b.y);
}

inline double dist(const Point & a , const Point & b) {
    return sqrt(sqr(a.x - b.x) + sqr(a.y - b.y));
}

inline double sqrdist(const Point & a , const Point & b)
{
        return sqr(a.x - b.x) + sqr(a.y - b.y);
}

/** Cross Product */
inline double operator ^ (const Point & a , const Point & b) {
    return a.x * b.y - a.y * b.x;
}

inline double cross(const Point & p , const Point & a , const Point & b) {
    return (a - p) ^ (b - p);
}

/** Dot product */
inline double operator * (const Point & a , const Point & b) {
    return a.x * b.x + a.y * b.y;
}

inline double dot(const Point & p , const Point & a , const Point & b) {
    return (a - p) * (b - p);
}

/** Whether Point p is on the segment [a, b] or not */
inline bool onSeg(const Point & p , const Point & a , const Point & b) {
    return ( sign(cross(p, a, b)) == 0 && sign(dot(p, a, b)) <= 0) ;
}

/** Whether Point p is on the ray from a to b */
inline bool onRay(const Point & p , const Point & a , const Point & b) {
    return ( sign(cross(p, a, b)) == 0 && sign(dot(a, p, b)) >= 0) ;
}

/** Whether Point p is on the straight line a-b or not */
inline bool onLine(const Point & p , const Point & a , const Point & b)
{
        return sign(cross(p,a,b))==0;
}

/** Find the intersection point of two strait lines a-b and c-d,
          storing the result in p */
bool lineIntersect(const Point & a , const Point & b ,
                           const Point & c , const Point & d , Point & p) {
    double u = cross(a, c, b), v = cross(a, b, d);
    if (sign(u + v) == 0) return false;
    p = (c * v + d * u) / (u + v);
    return true;
}

/** Find the intersection point of two segment a-b and c-d,
          storing the result in p */
bool segIntersect(const Point & a , const Point & b ,
                                  const Point & c , const Point & d , Point & p)
{
        bool lineInter = lineIntersect(a,b,c,d,p);
        if (lineInter && onSeg(p,a,b) && onSeg(p,c,d)) return true;
        else return false;
}

/** Intersection of two circles,
          whose centers are a and b, radius are r1 and r2, respectively
          Return the number of intersections, storing the result to array p */
vector<Point> interCir(const Point & a , const Point & b , double r1 , double r2) {
        vector<Point> ret;
    double d = dist(a, b), d1 = ((sqr(r1) - sqr(r2)) / d + d) / 2;
    if (sign(r1 + r2 - d) < 0 || sign(abs(r1 - r2) - d) > 0) return ret;
    Point mid = a + ((b - a) / d) * d1;
    if (sign(r1 + r2 - d) == 0) {
        ret.push_back(mid);
                return ret;
    }
    Point incr = (b - a).TurnLeft() / d * sqrt(sqr(r1) - sqr(d1));
        ret.push_back(mid - incr);
    ret.push_back(mid + incr);
        return ret;
}

vector<Point> ps;
vector<double> R;

bool isOK(double nowR)
{
	vector<Point> c1;
	vector<double> r1;
	vector<Point> c2;
	vector<double> r2;

	for (int i = 0; i < ps.size(); ++i) {
		Point cirPoint = Point(ps[i].x, ps[i].y);
		double rad = nowR - R[i];
		bool c1inter = true;
		bool c2inter = true;
		for (int j = 0; j < c1.size(); ++j)
			if (interCir(c1[j], cirPoint, r1[j], rad).size() == 0)
				c1inter = false;
		for (int j = 0; j < c2.size(); ++j)
			if (interCir(c2[j], cirPoint, r2[j], rad).size() == 0)
				c2inter = false;
		if (c1inter == false && c2inter == false) 
			return false;
		if (c1inter == true) {
			c1.push_back(cirPoint);
			r1.push_back(rad);
		}
		else {
			c2.push_back(cirPoint);
			r2.push_back(rad);
		}
	}
	return true;
}

double getAns()
{
	double leftR = 0;
	double rightR = 1e5;
	for (int i = 0; i < R.size(); ++i) 
		if (R[i] > leftR) leftR = R[i];
	leftR += 1e-6;

	while (fabs(rightR - leftR) > 1e-7) {
		double newR = (leftR + rightR) / 2;
		bool ok = isOK(newR);
		if (ok)
			rightR = newR;
		else
			leftR = newR;
	}

	return leftR;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int N;
		scanf("%d", &N);
		ps.clear();
		R.clear();
		for (int j = 0; j < N; ++j) {
			Point newp;
			double newr;
			scanf("%lf %lf %lf", &newp.x, &newp.y, &newr);
			ps.push_back(newp);
			R.push_back(newr);
		}

		printf("Case #%d: %.6lf\n", i, getAns());
	}

	return 0;
}