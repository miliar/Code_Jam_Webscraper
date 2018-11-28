#define DBG
// Grzegorz Guspiel
#include <iostream>
#include <queue>
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

const int maxn = 110;
char t[maxn][maxn];
bool use[maxn];
int n;

double wp(int a) {
	int all = 0;
	double r = 0;
	REP(i,n) if(use[i] && t[a][i] != '.'){
		if(t[a][i] == '1') r += 1;
		all++;
	}
	//if(all == 0) return 0;
	return r/all;
}

double owp(int a) {
	use[a] = 0;
	double r = 0;
	int all = 0;
	REP(i,n) if(use[i] && t[a][i] != '.') {
		r += wp(i);
		all++;
	}
	use[a] = 1;
	return r/all;
}

double oowp(int a) {
	//use[a] = 0;
	double r = 0;
	int all = 0;
	REP(i,n) if(t[a][i] != '.') {
		r += owp(i);
		all++;
	}
	//use[a] = 1;
	return r/all;
}

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		scanf("%d", &n);
		REP(i,n) scanf("%s", t[i]);
		REP(i,n) use[i] = 1;
		printf("Case #%d:\n", zz);
		REP(i,n) printf("%.9lf\n", wp(i)/4+oowp(i)/4+owp(i)/2);
	}
	return 0;
}

