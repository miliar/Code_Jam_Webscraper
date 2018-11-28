#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MaxN = 10005;
const int oo = 0x3F3F3F3F;

int DP[MaxN];

struct Node {
	int x, L;
	void init() {
		scanf("%d%d", &x, &L);
	}
	bool operator<(const Node& other) const {
		return x < other.x;
	}
} node[MaxN];

int main() {
	int T, cas = 1;
	int N;
	
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", cas++);
		scanf("%d", &N);
		for (int i = 0; i < N; i++) node[i].init();
		memset(DP, -1, sizeof(DP));
		sort(node, node + N);
		scanf("%d", &node[N].x);
		if (node[0].L < node[0].x) { puts("NO"); continue; }
		node[N].L = oo;
		DP[0] = node[0].x;
		for (int i = 0; i < N; i++) if (DP[i] != -1) {
			if (DP[i] > node[i].L) DP[i] = node[i].L;
			for (int j = i + 1; j <= N; j++) {
				if (node[j].x - node[i].x > DP[i]) break;
				DP[j] = max(DP[j], node[j].x - node[i].x);
			}
		}
		if (DP[N] == -1) puts("NO");
		else puts("YES");
		// for (int i = 0; i <= N; i++) printf("%d ", DP[i]);
		// puts("");
	}
	
	return 0;
}
