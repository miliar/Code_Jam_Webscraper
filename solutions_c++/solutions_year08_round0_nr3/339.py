#include <algorithm>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <stack>
#include <map>
#include <sstream>
#include <iostream>
#include <cmath>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pI;
typedef pair<string,int> pSI;
typedef pair<int,string> pIS;

#define FOR(i,n) for(int i=0, upTo##i=n; i<upTo##i; ++i)
#define REVFOR(i,n) for(int i=(n)-1; i>=0; --i)
#define FOR2(i,b,n) for(int i=b; i<(n); ++i)
#define REVFOR2(i,b,n) for(int i=(n)-1; i>=b; --i)
#define SC(i) scanf("%d", i)
#define ALL(C) (C).begin(), (C).end()
#define MIN(C) *min_element(ALL(C))
#define MAX(C) *max_element(ALL(C))
#define A first
#define B second

const double PI = 2*acos(0.0);

double dist2(double x1, double x2) {
	return x2*x2 + x1*x1;
}

int main(void) {
	int n; SC(&n);

	FOR(i,n) {
		if (i<69)  continue;
		double f;	//fly - radius
		double R;	//racquet - radius
		double t;	//thickness 
		double r;	//string - radius
		double g;	//gap between strings
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

		double area = PI * R * R;

		if (2*f >= g) {
			printf("Case #%d: %.6lf\n", i+1, 1.0);
		} else {
			double res = 0;
			double Rfixed2 = (R - t)*(R - t);
			double correctSize = g - 2*f;
			double singleField = correctSize * correctSize;

			double field = 0;
			double X = r;		//pierwsze pole
			double Y = r;

			while(true) {
				while(true) {
					if (dist2(X+g, Y+g) <= Rfixed2) {
						field += singleField;
					} else {
 						double XXbeg = X+f, XXend = X+g-f;
						double YYbeg = Y+f, YYend = Y+g-f; 
						double Rtf2 = (R-t-f)*(R-t-f);

						YYend = min(YYend, sqrt(Rtf2 - XXbeg*XXbeg));

						int steps = 10000;
						double step = (YYend-YYbeg) / steps;
						FOR(i,steps) {
							double YY1 = YYbeg + step*i;
							double YY2 = YY1+step;

							double XX1 = sqrt(Rtf2 - YY1*YY1);
							double a = min(XX1, XXend) - XXbeg;
							double XX2 = sqrt(Rtf2 - YY2*YY2);
							double b = min(XX2, XXend) - XXbeg;

							if (a>0 && b>0) {
								field += ((a+b)/2) * step;
							}
						}
					}

					Y += g + 2*r;
					if (dist2(X, Y) >= Rfixed2) break;
				}

				X += g + 2*r;
				Y = r;
				if (dist2(X, Y) >= Rfixed2) break;
			}

			res = 1 - ((field*4) / area);
			printf("Case #%d: %.6lf\n", i+1, res);
		}
	}

    return 0;
}
