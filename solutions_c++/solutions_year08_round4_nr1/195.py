#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#define let(i,a) __typeof(a)i=a
#define each(i,a) (let(i,(a).begin());i!=(a).end();++i)
#define INF 999999
using namespace std;

int N, M, V, G[10000], C[10000];

pair<int, int> saiki(int n) {
	if (n < M / 2) {
		let(a, saiki(n * 2 + 1));
		let(b, saiki(n * 2 + 2));
		pair<int, int> pand, por;
		pand = make_pair(min(
		 min(a.first + b.first, a.first + b.second), 
		 a.second + b.first),
		 a.second + b.second);
		por = make_pair(a.first + b.first, min(
		 min(a.second + b.second, a.first + b.second), 
		 a.second + b.first));
		if (C[n]) {
			pand = make_pair(min(pand.first, por.first + 1),
			 min(pand.second, por.second + 1));
			por = make_pair(min(por.first, pand.first + 1),
			 min(por.second, pand.second + 1));
		}
		return G[n] ? pand : por;
	} else {
		return G[n] ? make_pair(INF, 0) : make_pair(0, INF);
	}
}

int main(void) {
	scanf("%d", &N);
	for (int case_x = 1; case_x <= N; case_x++) {
		scanf("%d%d", &M, &V);
		for (int i = 0; i < M; i++) {
			scanf("%d", &G[i]);
			if (i < M / 2) scanf("%d", &C[i]);
		}
		let(ret, saiki(0));
		let(ans, V ? ret.second : ret.first);
		if (INF <= ans) printf("Case #%d: IMPOSSIBLE\n", case_x);
		else printf("Case #%d: %d\n", case_x, ans);
	}
	return 0;
}
