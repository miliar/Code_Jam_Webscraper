// codeJam2A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
#define FORR(i, a, b) for(int i = (a); i<(b); i++)
#define FOR(i, n) FORR(i,0,n)
int p[500], k[500];



bool czek(int n, long double d, long double t) {
	long double t1 = t*1.00000000001 + 0.00000000001;
	long double f = -1e100;
	FOR(i, n) {
		long double first = p[i]-t;
		if(i>0) first = max(f+d, p[i]-t);

		long double last = first + (k[i]-1)*d;

		if(first-p[i]>t1 || last-p[i]>t1 || first-p[i]<-t1 || last-p[i]<-t1)  {
			//cout << first << ' ' << last << ' ' << p[i] << ' ' << t1 << "!" << endl;
			return false;
		}
		f = last;
	}
	return true;
}

long double jeden() {
	int n, d;scanf("%d%d", &n, &d);
	FOR(i, n) {
		scanf("%d%d", p+i, k+i);
	}
	if(d == 0) return 0.0;
	bool zero = true;
	FOR(i, n) if(k[i] >1) zero = false;
	FORR(i, 1, n) if(p[i]-p[i-1] <d) zero = false;
	if(zero) return 0.0;

	long double a = 0.01, b = 5e13;
	long double c;
	FOR(i, 250) {
		c = a/2.+b/2.;
		//cout << a << ' ' << b << ' ' << c << endl;
		if(czek(n,d,c)) {
			b = c;
		} else {
			a = c;
		}
	}
	return c;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t; scanf("%d", &t);
	for(int i = 1; i<=t; i++) {
		cout.precision(20);
		cout << "Case #" << i << ": " << jeden() << endl;
	}
	return 0;
}

