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

typedef long double ld;

void test() {
	ld x,s,r,t;
	int n;
	scanf("%Lf%Lf%Lf%Lf%d", &x, &s, &r, &t, &n);
	vector<pair<ld,ld> > vec;
	REP(i,n) {
		ld a,b,v;
		scanf("%Lf%Lf%Lf", &a, &b, &v);
		ld d = b-a;
		x -= b-a;
		vec.PB(make_pair(v,b-a));
	}
	vec.PB(make_pair(0,x));
	sort(vec.begin(),vec.end());
	ld res = 0;
	REP(i,vec.size()) {
		//printf("%Lf %Lf\n", vec[i].first, vec[i].second);
		ld dist = vec[i].second;
		if (t > 0) {
			ld tt = dist / (vec[i].first+r);
			if (tt < t) {
				t -= tt;
				res += tt;
				dist = 0;
			}
			else {
				dist -= (vec[i].first+r)*t;
				res += t;
				t = 0;
			} 
		}
		if (dist > 0) {
			ld tt = dist / (vec[i].first+s);
			res += tt;
		}
	}
	printf(" %.9Lf\n", res);
}

main() {
	int t; scanf("%d", &t);
	REP(i,t) { printf("Case #%d:", i+1); test(); }
}

