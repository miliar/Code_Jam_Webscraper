#include <cstdio>
#include <memory>

const int maxn = 200;
const int maxm = 100;

int casei, cases, n, m, ans;
bool avai[maxn];
int from[maxn];
int pri[maxn][maxm];
bool g[maxn][maxn];

inline void init() {
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) scanf("%d", &pri[i][j]);
}

inline bool check(int n1, int n2) {
	for (int i = 0; i < m; ++i) if (pri[n1][i] >= pri[n2][i]) return false;
	return true;
}

inline void buildG() {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) g[i][j] = check(i, j);
}

inline bool getConnect(int now) {
	if (now == -1) return true;
	for (int i = 0; i < n; ++i) if (g[now][i] && avai[i]) {
		avai[i] = false;
		if (getConnect(from[i])) {
			from[i] = now;
			return true;
		}
	}
	return false;
}

inline void process() {
	buildG();
	
	memset(from, 255, sizeof from);
	ans = 0;
	for (int i = 0; i < n; ++i) {
		memset(avai, true, sizeof avai);
		if (getConnect(i)) ++ans;
	}
	ans = n - ans;
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C-small-attempt0.out", "w", stdout);
	
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
