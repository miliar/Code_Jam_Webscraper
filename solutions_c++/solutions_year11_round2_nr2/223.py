#include <cstdio>
#include <vector>
#include <algorithm>
//#include <map>
//#include <set>

#define FOR(i,s,e) for (int i=(s);i<(e);i++)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define PB push_back

using namespace std;

typedef long long int lld;
vector<pair<lld,lld> > data;
lld D;

inline lld absy(lld x) {
	return x < 0 ? -x : x;
}

bool check(lld tim) {
	//printf("CHECK %lld\n", tim);
	lld last = data[0].first - tim + D*(data[0].second-1);
	//printf("Last0 %lld - data @ %lld\n", last, data[0].first);
	if (absy(last - data[0].first) > tim) return false;
	FOR(i,1,data.size()) {
		last = max(data[i].first - tim, last + D);
		if (absy(last - data[i].first) > tim) return false;
		last = last + D*(data[i].second-1);
		if (absy(last - data[i].first) > tim) return false;
	}
	return true;
}

void test(int cid) {
	int c;
	lld a, cnt = 0, b;
	scanf("%d%lld", &c, &D);
	D *= 2;
	data.clear();
	REP(i,c) {
		scanf("%lld%lld", &a, &b);
		data.push_back(make_pair(2*a,b));
		cnt += b;
	}
	sort(data.begin(), data.end());
	lld l = 0, r = D * cnt;
	if (!check(l)) {
		while (r-l > 1) {
			lld mid = (l+r)/2;
			if (check(mid)) r = mid;
			else l = mid;
		}
	}
	if (!check(l)) l = r;
	if (l%2) printf("Case #%d: %lld.5\n", cid, l/2);
	else printf("Case #%d: %lld.0\n", cid, l/2);
}

main() {
	int t;
	scanf("%d", &t);
	REP(i,t) test(i+1);
}

