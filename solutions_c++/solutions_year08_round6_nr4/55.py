#include <cstdio>
#include <memory>

const int maxn = 100;

bool ans;
int casei, cases, n, m;
bool avai[maxn];
int num[maxn];
int ed[maxn][2], ed2[maxn][2];

inline void init() {
	scanf("%d", &n);
	for (int i = 0; i < n - 1; ++i) {
		scanf("%d%d", &ed[i][0], &ed[i][1]);
		--ed[i][0]; --ed[i][1];
	}
	scanf("%d", &m);
	for (int i = 0; i < m - 1; ++i) {
		scanf("%d%d", &ed2[i][0], &ed2[i][1]);
		--ed2[i][0]; --ed2[i][1];
	}
}

inline bool find(int tmp1, int tmp2) {
	for (int i = 0; i < n - 1; ++i) 
		if ((ed[i][0] == tmp1 && ed[i][1] == tmp2) || (ed[i][0] == tmp2 && ed[i][1] == tmp1)) return true;
	return false;
}

inline bool DFS(int now) {
	if (now == m) {
		for (int i = 0; i < m - 1; ++i) if (!find(num[ed2[i][0]], num[ed2[i][1]])) return false;
		return true;
	}
	for (int i = 0; i < n; ++i) if (avai[i]) {
		num[now] = i;
		avai[i] = false;
		if (DFS(now + 1)) return true;
		avai[i] = true;
	}
	return false;
}

inline void process() {
	memset(avai, true, sizeof avai);
	ans = DFS(0);
}

inline void print() {
	if (ans) printf("Case #%d: YES\n", casei);
	else printf("Case #%d: NO\n", casei);
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin); freopen("sd.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
	
	return 0;
}
