#define DBGi
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

typedef pair<long double,long double> pdd;
vector<pdd> v;

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		long double x,r,s,t,sum_walkways,result;
		int n;
		scanf("%Lf%Lf%Lf%Lf%d", &x, &s, &r, &t, &n);
		sum_walkways = 0;
		REP(i,n) {
			long double b,e,w;
			scanf("%Lf%Lf%Lf", &b, &e, &w);
			v.PB(MP(w, e - b));
			sum_walkways += e - b;
		}
		v.PB(MP(0.0, x - sum_walkways));
		sort(v.begin(), v.end());
		result = 0;
		REP(i,v.size()) {
			debug("%Lf meters extra speed %Lf\n", v[i].ND, v[i].ST);
			long double todo = v[i].ND;
			long double faster_speed = r + v[i].ST;
			long double running_time = min(t, todo / faster_speed);
			todo -= running_time * faster_speed;
			t -= running_time;
			result += running_time;
			long double slower_speed = s + v[i].ST;
			result += todo / slower_speed;
			debug("ran s=%Lf v=%Lf, walked s=%Lf v=%Lf\n", running_time * faster_speed, faster_speed, todo, slower_speed);
		}
		v.clear();
		printf("Case #%d: %.9Lf\n", zz,result);
	}
	return 0;
}

