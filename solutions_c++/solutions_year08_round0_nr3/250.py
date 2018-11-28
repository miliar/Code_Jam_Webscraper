#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;

const double PI = acos(-1.0);
const double INF = 1e100;
const double EPS = 1e-10;

typedef struct {
	double x, y;
} Pt;

inline int sign(double a)
{
	return a<-EPS? -1: a>EPS? 1:0;
}

double polar(Pt p)
{
	if (sign(p.x) == 0) return p.y>0 ? PI/2 : 3*PI/2;
	else { 
		double r = atan2(p.y, p.x);
		if (r<0) r += 2*PI;
		return r;
	}
}

double Ar_Area(double r, Pt A, Pt B)
{
	double ag = polar(A)-polar(B);
	return r*r*(ag-sin(ag))/2;
}

bool inArea(double xx, double yy, double rr)
{
	return (xx*xx+yy*yy < rr*rr);
}

double getOther(double rr, double a)
{
	return sqrt(rr*rr-a*a);
}

double getArea(Pt a, double g, double rr)
{
	Pt A, B;
	if (inArea(a.x+g, a.y+g, rr))
		return g*g;
	else {
		double ans = 0;
		if (inArea(a.x+g, a.y, rr)) {
			if (inArea(a.x, a.y+g, rr)) {
				A.y = a.y+g, A.x = getOther(rr, A.y);
				B.x = a.x+g, B.y = getOther(rr, B.x);
				ans += ((A.x-a.x)*g);
				ans += ((B.y-a.y)+g)*(a.x+g-A.x)/2;
			}
			else {
				A.x = a.x, A.y = getOther(rr, A.x);
				B.x = a.x+g, B.y = getOther(rr, B.x);
				ans += ((A.y-a.y)+(B.y-a.y))*g/2;
			}
		}
		else {
			if (inArea(a.x, a.y+g, rr)) {
				A.y = a.y+g, A.x = getOther(rr, A.y);
				B.y = a.y, B.x = getOther(rr, B.y);
				ans += ((A.x-a.x)+(B.x-a.x))*g/2;
			}
			else {
				A.x = a.x, A.y = getOther(rr, A.x);
				B.y = a.y, B.x = getOther(rr, B.y);
				ans += (A.y-a.y)*(B.x-a.x)/2;
			}
		}
		ans += Ar_Area(rr, A, B);
		return ans;
	}
}

int main()
{
	int N, i;
	double f, R, t, r, g, xx, yy, ans;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> N;
	for (i = 1; i <= N; i ++)
	{
		cin >> f >> R >> t >> r >> g;
		if (2*f > g) {
			ans = 1;
		}
		else {
			double rr = R-t-f;
			double area = 0;
			for (xx = 0; xx < rr; xx += (g+2*r)) {
				for (yy = 0; yy < rr; yy += (g+2*r)) {
					Pt a;
					a.x = xx+r+f, a.y = yy+r+f;
					if (inArea(a.x, a.y, rr)) {
						area += getArea(a, g-2*f, rr);
					}
				}
			}
			ans = 1 - 4*area/(PI*R*R);
		}
		cout << "Case #" << i << ": ";
		cout << setiosflags(ios::fixed) << setprecision(6) << ans << endl;
	}
	return 0;
}