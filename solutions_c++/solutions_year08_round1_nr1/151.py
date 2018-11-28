#define SOLVE "A-large"
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <string>
#include <cstdio>
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"
#define GI ({int t; scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(), (v).end())
#define sz size()
#define pb push_back
#define cs c_str()
#define INF ((int)(1e8))
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		int n = GI;
		LL a[n], b[n], ans = 0;
		REP(i,n) a[i]=GI; REP(i,n) b[i]=GI;
		sort(a,a+n); sort(b,b+n);
		REP(i,n) ans += a[i]*b[n-1-i];
		cout << ans << endl;
	}
	return 0;
}
