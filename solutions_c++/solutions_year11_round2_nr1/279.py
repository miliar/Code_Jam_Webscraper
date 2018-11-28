// codeJam2A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;
#define FORR(i, a, b) for(int i = (a); i<(b); i++)
#define FOR(i, n) FORR(i,0,n)

char T[200][200];
double wp[200];
int ls[200], ws[200];
double owp[200];
double oowp[200];


void jeden() {
	int n ;scanf("%d", &n);
	FOR(i, n) scanf("%s", T[i]);
	FOR(i, n) {
		int l =0, w = 0;
		FOR(j, n) if(T[i][j] == '1') {
			w++;
		} else if(T[i][j] == '0') {
			l++;
		}
		wp[i] = w/double(w+l);
		ls[i] = l; ws[i]=w;
	}
	FOR(i, n) {
		double a = 0.0;
		int sum = 0.0;

		FOR(j, n) if(T[i][j] !='.'){
			int l = ls[j];
			int w = ws[j];
			if(T[i][j] == '1') l--;
			if(T[i][j] == '0') w--;
			sum++;
			a+=w/double(l+w);
		}
		owp[i] = a/sum;
	}

	FOR(i, n) {
		double a = 0.0;
		int sum = 0.0;
		FOR(j, n) if(T[i][j] !='.'){
			sum++;
			a += owp[j];
		}
		oowp[i] = a/sum;
	}
	FOR(i, n) {
		printf("%.10lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t; scanf("%d", &t);
	for(int i = 1; i<=t; i++) {
		printf("Case #%d:\n", i);
		jeden();
	}
	return 0;
}

