#define DBGi
// Grzegorz Guspiel
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,bb,ee) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define ST first
#define ND second
#define PB push_back
#define PP pop_back
#define MP make_pair

typedef long double treal;

const int maxn = 1010;
treal t[maxn];
treal f[maxn];

treal pnk(int n) {
	treal s = 0;
	FOR(i,0,n) {
		//debug("take i %d %Lf\n",i, f[i]);
		s += treal(((i)%2)?-1:1) / f[i];
	}
	 
	return s;	
}

treal pn(int n, int k) {
	treal res =   pnk(n-k) / f[k];
	debug("pn %d %d : %Lf\n", n,k,res);
	return res;
}

int main() {
	f[0] = 1;
	int n = 1001;
	FOR(i,1,n) f[i] = f[i-1] * i;
	t[0] = 0;
	t[1] = 0;
	FOR(i,2,n) {
		double r = 1;
		FOR(j,1,i) r += pn(i,j) * t[i-j];
		double p = pn(i,0);
		t[i] = r/(1-p);
		if(i < 5) debug("t[%d] = %Lf\n", i, t[i]);
	}
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		scanf("%d", &n);
		int k = 0;
		FOR(i,1,n) {
			int a;
			scanf("%d", &a);
			if(a != i) k++;
		}
		printf("Case #%d: %Lf\n", zz,t[k]);
	}
	return 0;
}
