#define DBG
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



int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z){
		int n; scanf("%d", &n);
		int sum = 0;
		int bsum = 0;
		int sm = 1000000100;
		while(n--) {
			int a; scanf("%d", &a);
			sum += a;
			bsum ^= a;
			sm = min(sm, a);
		}
		printf("Case #%d: ", zz);
		if(bsum == 0) printf("%d\n", sum - sm);
		else printf("NO\n");
	}
	return 0;
}
