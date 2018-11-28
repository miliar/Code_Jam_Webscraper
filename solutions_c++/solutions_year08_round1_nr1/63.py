#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FS(i,v) for(__typeof((v).begin())i=(v).begin();i!=v.end();++(i))
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) ((int)(a).size())
#define MK make_pair
#define FI first
#define SE second
typedef long long ll;
typedef long double ldouble;
int t, n;
ll t1[1005], t2[1005];
void lecim(int numer) {
	scanf("%d",&n);
	REP(i,n) scanf("%lld", &t1[i]);
	REP(i,n) scanf("%lld", &t2[i]);
	sort(t1, t1 + n);
	sort(t2, t2 + n);
	ll ret = 0;
	deque<ll> a1, a2;
	REP(i,n) {
		a1.push_back(t1[i]);
		a2.push_back(t2[i]);
	}
	REP(i,n) {
		if(a1.back() * a2.front() < a1.front() * a2.back()) {
			ret += a1.back() * a2.front();
			a1.pop_back();
			a2.pop_front();
		} else {
			ret += a2.back() * a1.front();
			a2.pop_back();
			a1.pop_front();
		}
	}
	printf("Case #%d: %lld\n", numer, ret);
}
int main() {
	scanf("%d",&t);
	REP(i,t) lecim(i + 1);
	return 0;
}
