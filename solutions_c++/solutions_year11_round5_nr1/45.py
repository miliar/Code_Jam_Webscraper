//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second
#define X real()
#define Y imag()

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 100 + 10;
const double EPS = 1e-8;

double w;
int nu, nd, g;
point up[MAX_N];
point dn[MAX_N];

double area(point pnt[], int n, double x){
	double ret = 0;
	FOR(i, n - 1){
		if(x < pnt[i].X)
			break;
		if(x > pnt[i + 1].X){
			double mid = (pnt[i].Y + pnt[i + 1].Y) / 2;
			ret += mid * (pnt[i + 1].X - pnt[i].X);
			continue;
		}
		double y = (pnt[i + 1].Y - pnt[i].Y) / (pnt[i + 1].X - pnt[i].X);
		y *= (x - pnt[i].X);
		y += pnt[i].Y;
		
		double mid = (pnt[i].Y + y) / 2;
		ret += mid * (x - pnt[i].X);
	}
	return ret;
}

double areaBitween(double x){
	return area(up, nu, x) - area(dn, nd, x);
}

int main(){
	int testN;
	cin >> testN;
	FOR(testI, testN){
		printf("Case #%d:\n", testI + 1);
		cin >> w >> nd >> nu >> g;
		
		FOR(i, nd){
			double x, y;
			cin >> x >> y;
			dn[i] = point(x, y);
		}
		FOR(i, nu){
			double x, y;
			cin >> x >> y;
			up[i] = point(x, y);
		}
		
		double total = areaBitween(w);
		double bef = 0;
		FOR(i, g - 1){
			double s = bef, e = w + EPS;
			while(abs(s - e) > EPS){
				double m = (s + e) / 2;
				double cur = areaBitween(m) - areaBitween(bef);
				if(cur * g > total)
					e = m;
				else	s = m;
			}
			
			printf("%0.7lf\n", s);
			bef = s;
		}
		
	}
	return 0;
}
