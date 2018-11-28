#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <assert.h>
#include <set>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (long long i=a,_n=b; i<=_n; i++)
#define FORE(i,a) for (__typeof(a.begin()) i=a.begin(); i!=a.end(); i++)

int nTC,N,Pd,Pg;

bool can(){
	FOR(D,1,N) if ((D*Pd)%100 == 0)
		FOR(G,D,10000000) if ((G*Pg)%100 == 0){
			long long Wd = D*Pd / 100;
			long long Wg = G*Pg / 100;
			long long Ld = D - Wd;
			long long Lg = G - Wg;
			if (Ld <= Lg && Wd <= Wg){
				return true;
			}
		}
	return false;
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		scanf("%d %d %d",&N,&Pd,&Pg);

		/*
		long long a = Pd, b = 100, gab = __gcd(a,b); a /= gab; b /= gab;
		long long c = Pg, d = 100, gcd = __gcd(c,d); c /= gcd; d /= gcd;
		long long LCM = b*d/__gcd(b,d);
		long long Wg = LCM * c / d;
		long long 
		*/
		printf("Case #%d: ",TC);
		puts(can()? "Possible" : "Broken");
		fflush(stdout);
	}
}
