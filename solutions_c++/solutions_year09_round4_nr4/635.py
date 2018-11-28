// C++ Header

// -- Base
#include <iostream>
#include <sstream>
// Data Structure
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <numeric>
#include <algorithm>

// C Header
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <cstring>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstddef>

using namespace std;

// Global Macro

#define FOR(V,I,L) for(int V=(I);V<(L);(V)++)     // for loop macro start from I until < L
#define FORe(V,I,L) FOR(V,I,L+1)
#define FORd(V,I,L) for(int V=(I);V>=(L);(V)--)
#define REP(V,L) FOR(V,0,L)                           // for loop start from 0
#define REPe(V,L) FORe(V,0,L)
#define REPd(V,I) FORd(V,I,0)
#define IT(adt) adt::iterator        // Create Iterator
#define FOR_EACH(I,C) for(I=(C).begin(); I!=(C).end(); ++I)    // for loop for iterator

typedef pair<int ,int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int    ui;
typedef long double     ld;

char s[1111][1111];

int N;
pii a[1111];

double x[111];
double y[111];
double r[111];

double dist(double x1, double y1, double x2, double y2) {
	double dx = x2-x1;
	double dy = y2-y1;

	double t = dx*dx+dy*dy;

	return sqrt(t);
}

int main(void) {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);


	int T; scanf("%d" ,&T);
	int tc=1;
	while(T--) {
		scanf("%d", &N);

		for(int i=0;i<N;i++) scanf("%lf %lf %lf", &x[i], &y[i], &r[i]);

		double res=1111111.0;
		
		if(N==1) {
			res = r[0];
		}
		else if(N==2) {
			res = max(r[0],r[1]);
		}
		else if(N==3) {
			res =          max( (dist(x[0], y[0], x[1], y[1])+r[0]+r[1])/2.0, r[2]);
			res = min(res, max( (dist(x[1], y[1], x[2], y[2])+r[1]+r[2])/2.0, r[0]));
			res = min(res, max( (dist(x[0], y[0], x[2], y[2])+r[0]+r[2])/2.0, r[1]));
		}
		else assert(false);
		
	
		printf("Case #%d: %.6lf\n", tc++, res);
	}
	return 0;
}
