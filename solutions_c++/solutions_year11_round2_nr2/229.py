#define DBGi
// Grzegorz Guspiel
#include <iostream>
#include <cassert>
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

typedef pair<int,int> pii;
vector<int> t;
int d;
const long double eps = 0.0000001;
const long double upb = 1e13;
bool ok(long double r) {
	debug("check %lf\n", r);
	long double last = -upb;
	REP(i,t.size()) {
		long double pos = max(last + d, (long double)(t[i]) - r);
		//debug("position %d at %lf\n", t[i], pos);
		if(pos - t[i] > r) {
			//debug("stop\n");
			return 0;
		}
		last = pos;
	}
	//debug("ok\n");
	return 1;
}

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		int hm; scanf("%d%d", &hm, &d);
		while(hm--) {
			int pos, cnt;
			scanf("%d%d", &pos, &cnt);
			while(cnt--) t.PB(pos);
		}
		sort(t.begin(), t.end());
		long double b = 0;
		long double e = upb;
		while(e - b > eps) {
			long double s = (b+e)/2;
			if(ok(s)) e = s;
			else b = s;
			debug("%.10lf %.10lf %.10lf\n", b,s,e);
		}
		printf("Case #%d: %.9Lf\n", zz,b);
		assert(b < upb - 1); 
		t.clear();
	}
	return 0;
}

