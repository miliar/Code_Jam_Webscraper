#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <set>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <list>
#include <stack>

using namespace std;

const int INF = 0x7FFFFFFF;
const int N = 10002;

long long dist[N];
long long leng[N];
set<pair<int, long long> > vis;
int n;

void init() {
	vis.clear();
	for (int i=0; i<=n; ++i) dist[i] *= 2;
	for (int i=0; i<n; ++i) leng[i] *= 2;
}

bool move(int a, int b) ;
bool moveFrom(int a, long long r) {
	r = min(r, leng[a]);
	if (dist[a] + r >= dist[n]) return true;
	if (vis.count(make_pair(a, r))) return false;
	vis.insert(make_pair(a, r));
//	printf("moveFrom(%d %lld)\n", a, r);
	int c = lower_bound(dist, dist+n, dist[a]-r) - dist;
	for (;c < n; ++c) {
		if (dist[a] + r < dist[c]) break;
		if (c == a) continue;
//		long long dx = dist[a]-dist[c];
		// too short
	//	if (dx*dx + leng[c]*leng[c] < r*r) continue;
		if (move(min(a,c), max(a,c))) return true;
	}
	return false;
}

bool move(int a, int b) {
	long long r = dist[b] - dist[a];
//	printf("move(%d %d)\n", a, b);
//	if (r > leng[a] || r > leng[b]) return false;
	return ( moveFrom(a, r) || moveFrom(b, r));
}

int main(void) {
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) scanf("%lld%lld", dist+i, leng+i);
		leng[n] = 0;
		scanf("%lld", dist+n);
		init();
		printf("Case #%d: %s\n", tc, moveFrom(0, dist[0]) ? "YES" : "NO");
	}
	return 0;
}
