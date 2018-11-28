#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <sstream>
#include <cstdlib>
#include <cassert>
using namespace std;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef  vector<int> VI;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"
const int NMAX = 15;
const int NUM_ITER = 100;
struct Point {
	double x, y, z, p;
};
Point p[NMAX];
int n;

double getDist(double x, double y, double z) {
	double ret = (abs(x-p[0].x) + abs(y-p[0].y) + abs(z-p[0].z)) / p[0].p;
	forn(i, n) {
		double tmp = (abs(x-p[i].x) + abs(y-p[i].y) + abs(z-p[i].z)) / p[i].p;
		ret = max(tmp, ret);
	}
	return ret;
}

double Search3(double x, double y, double &z) {
	double l = 0, r = 1000000.0;
	forn(iter, NUM_ITER) {
		double m1 = (r-l)/3+l;
		double m2 = r - (r-l)/3;
		if (getDist(x, y, m1) > getDist(x, y, m2)) {
			l = m1;
		} else {
			r = m2;
		}			
	}	
	z = l;
	return getDist(x, y, z);
}
double Search2(double x, double& y, double &z) {
	double l = 0, r = 1000000.0;
	forn(iter, NUM_ITER) {
		double m1 = (r-l)/3+l;
		double m2 = r - (r-l)/3;
		if (Search3(x, m1, z) > Search3(x, m2, z)) {
			l = m1;
		} else {
			r = m2;
		}			
	}	
	y = l;
	return getDist(x, y, z);
}
double Search1(double& x, double& y, double &z) {
	double l = 0, r = 1000000.0;
	forn(iter, NUM_ITER) {
		double m1 = (r-l)/3+l;
		double m2 = r - (r-l)/3;
		if (Search2(m1, y, z) > Search2(m2, y, z)) {
			l = m1;
		} else {
			r = m2;
		}			
	}	
	x = l;
	return getDist(x, y, z);
}

int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
	int tc;
	cin >> tc; 
	for1(it, tc) {
		cin >> n;
		forn(i, n) {
			scanf("%lf %lf %lf %lf", &p[i].x, &p[i].y, &p[i].z, &p[i].p);
		}
		double x, y, z;
		double ans = Search1(x, y, z);
		printf("Case #%d: %.6lf\n", it, ans);
	}

	return 0;
}
