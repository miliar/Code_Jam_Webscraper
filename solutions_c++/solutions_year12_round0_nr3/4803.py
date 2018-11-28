#define debug if(1)
// Grzegorz Guspiel
#include <iostream>
#include <vector>
#include <cassert>
#include <cstring>
#include <cmath>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,ee,bb) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define st first
#define nd second
#define pb push_back
#define pp pop_back
#define mp make_pair
int stmp; 
#define scanf stmp=scanf

// In g++, you can use the little known __uint128_t type.

int d(int a) {
	if(a == 0) return 0;
	else return 1 + d(a/10);
}

bool is(int n, int m) {
	if(d(n) != d(m)) return 0;
	int c = d(n);
	int k = 1;
	REP(i,c-1) k *= 10;
	REP(i,c) {
		if(d(n) == c && n == m) return 1;
		int tmp = n % 10;
		n /= 10;
		n += tmp * k;
	}
	return 0;
}

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		int r = 0;
		int a, b; scanf("%d%d", &a, &b);
		FOR(n,a,b) FOR(m,n+1,b) if(is(n,m)) r++;
		printf("Case #%d: %d\n", zz, r);
	}
	return 0;
}
