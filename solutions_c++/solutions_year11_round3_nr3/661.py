// PerfectHarmony.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>
#include <string>
using namespace std;

int readi() { int a; scanf( "%d", &a ); return a; }
double readf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string readstr() { scanf( "%s", sbuf ); return sbuf; }
long long readll() { long long a; scanf( "%lld", &a ); return a; }
#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )

#define MAX 10000

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);	

	int T, N;
	long long L, H;
    int i, j, k, r, s, t;
	int players[MAX];
	bool found, all;

	T = readi();
	for(r=1; r <= T; ++r) {
		N = readi(); L = readi(); H=readi();
		memset(players, 0, MAX * sizeof(int));

		for(j = 0; j < N; ++j) players[j] = readll();

		all = false;
		for(i = L; i <= H; i++) {
			found = true;
			for(j = 0; j < N; ++j) {
				if((players[j] % i != 0) && (i % players[j] != 0)) {
					found = false; break;
				}
			}

			if(found) {all = true; break;}
		}
	
		if(!all) printf("Case #%d: NO\n", r);
		else printf("Case #%d: %d\n", r, i);

	}
	

	return 0;
}

