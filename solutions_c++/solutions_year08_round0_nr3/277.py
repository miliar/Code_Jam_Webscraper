#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

double f, R, t, r, g;
struct dot {
	double x, y;
	dot &operator-=(const dot &b) {x -= b.x; y -= b.y; return *this;}
	dot &operator*=(const double k) {x *= k; y *= k; return *this;}
	dot &operator/=(const double k) {x /= k; y /= k; return *this;}
} orig;
dot operator-(const dot &a, const dot &b) {dot c(a); return c-=b;}
dot operator*(const dot &a, const double k) {dot c(a); return c*=k;}
dot operator/(const dot &a, const double k) {dot c(a); return c/=k;}

const double EPS = 1e-9;
int cmp(const double x, const double y) {return x<=y+EPS?x<y-EPS?-1:0:1;}
double cross(const dot &a, const dot &b) {return a.x*b.y - a.y*b.x;}
double trian(const dot &a, const dot &b, const dot &c) {return fabs(cross(b-a, c-a))/2.0;}
int ccw(const dot &a, const dot &b, const dot &c) {return cmp(cross(b-a, c-a), 0.0);}
void line_inter(const dot &a, const dot &b, const dot &c, const dot &d, dot &e) {
	double s1 = cross(c-a, b-a);
	double s2 = cross(d-a, b-a);
	e = (d*s1 - c*s2) / (s1-s2);
}

double inter(int i, int j) {
	dot ll = (dot) {r + (g+2*r)*i, r + (g+2*r)*j};
	dot lr = (dot) {ll.x + g, ll.y};
	dot ul = (dot) {ll.x, ll.y + g};
	dot ur = (dot) {ll.x + g, ll.y + g};

	ll.x += f; ll.y += f;
	lr.x -= f; lr.y += f;
	ul.x += f; ul.y -= f;
	ur.x -= f; ur.y -= f;

	double rad = R-t-f;
	bool insidell = hypot(ll.x, ll.y) < rad;
	bool insidelr = hypot(lr.x, lr.y) < rad;
	bool insideul = hypot(ul.x, ul.y) < rad;
	bool insideur = hypot(ur.x, ur.y) < rad;

	if (!insidell) return 0.0;
	
	if (insideur) return (ur.x-ll.x)*(ur.y-ll.y);

	if (!insideul && !insidelr) {
		dot c1, c2;
		c1.x = ll.x; c1.y = sqrt(rad*rad-c1.x*c1.x);
		c2.y = ll.y; c2.x = sqrt(rad*rad-c2.y*c2.y);
		double area = asin(fabs(cross(c1, c2))/(rad*rad))*rad*rad/2.0;
		return area - trian(orig,ll,c1) - trian(orig,ll,c2);
	}
	
	if (insideul && insidelr) {
		dot c1, c2, d1, d2;
		c1.y = ul.y; c1.x = sqrt(rad*rad-c1.y*c1.y);
		c2.x = lr.x; c2.y = sqrt(rad*rad-c2.x*c2.x);
		double area = asin(fabs(cross(c1, c2))/(rad*rad))*rad*rad/2.0;
		if (ccw(orig, ll, c1) > 0) {
			if (ccw(orig, ll, c2) > 0) {
				line_inter(ll, ul, orig, c1, d1);
				line_inter(ll, ul, orig, c2, d2);
				return area + trian(d1,ul,c1) + trian(d2,ll,lr) + trian(lr,c2,d2) - trian(orig,d1,d2);
			} else {
				line_inter(ll, ul, orig, c1, d1);
				line_inter(ll, lr, orig, c2, d2);
				return area + trian(d1,ul,c1) + trian(d2,lr,c2) - trian(orig,ll,d1) - trian(orig,ll,d2);
			}
		} else {
			line_inter(ll, lr, orig, c1, d1);
			line_inter(ll, lr, orig, c2, d2);
			return area + trian(d2,lr,c2) + trian(d1,ll,ul) + trian(ul,c1,d1) - trian(orig,d1,d2);
		}
	}

	if (insideul) {
		dot c1, c2, d1;
		c1.y = ul.y; c1.x = sqrt(rad*rad-c1.y*c1.y);
		c2.y = ll.y; c2.x = sqrt(rad*rad-c2.y*c2.y);
		double area = asin(fabs(cross(c1, c2))/(rad*rad))*rad*rad/2.0;
		if (ccw(orig, ll, c1) > 0) {
			line_inter(ll, ul, orig, c1, d1);
			return area + trian(d1,ul,c1) - trian(orig,ll,d1) - trian(orig,ll,c2);
		} else {
			line_inter(ll, lr, orig, c1, d1);
			return area - trian(orig,d1,c2);
		}
	}

	if (insidelr) {
		dot c1, c2, d2;
		c1.x = ll.x; c1.y = sqrt(rad*rad-c1.x*c1.x);
		c2.x = lr.x; c2.y = sqrt(rad*rad-c2.x*c2.x);
		double area = asin(fabs(cross(c1, c2))/(rad*rad))*rad*rad/2.0;
		if (ccw(orig, ll, c2) > 0) {
			line_inter(ll, ul, orig, c2, d2);
			return area - trian(orig,c1,d2);
		} else {
			line_inter(ll, lr, orig, c2, d2);
			return area + trian(d2,lr,c2) - trian(orig,ll,c1) - trian(orig,ll,d2);
		}
	}

	return 0.0;
}

int main() {
	double area;
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> f >> R >> t >> r >> g;
		double ans = 0.0;
		int i = 0, j = 0;
		if (g > 2*f) {
			while (true) {
				area = inter(i, j);
				ans += area;
				if (area == 0.0) {
					if (j > 0) {
						j = 0;
						i++;
					} else {
						break;
					}
				} else {
					j++;
				}
			}
		}
		cout << "Case #" << caso + 1 << ": ";
		cout << fixed << setprecision(6) << 1.0 - 4.0*ans/(M_PI*R*R) << endl;
	}
	return 0;
}
