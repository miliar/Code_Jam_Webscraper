#include <cstdio>

int casei, cases, n, m, newx, newy, ans, num;
char bb[20][20];

inline void init() {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j) {
			scanf(" %c", &bb[i][j]);
		}
}

inline bool check(int nowx, int nowy) {
	if (bb[nowx][nowy] != '.') return false;
	if (nowx > 1) {
		if (nowy > 1)
			if (bb[nowx - 1][nowy - 1] == 's') return false;
		if (nowy < m)
			if (bb[nowx - 1][nowy + 1] == 's') return false;
	}
	return true;
}

inline void DFS(int nowx, int nowy, int total) {
	if ((n - nowx) * num + (m - nowy) / 2 + 1 + total <= ans) return;
	if (nowx > n) {
		if (total > ans) ans = total;
		return;
	}

	if (nowy == m) {
		newx = nowx + 1; newy = 1;
	}
	else {
		newx = nowx; newy = nowy + 1;
	}
	DFS(newx, newy, total);

	if (check(nowx, nowy)) {
		if (nowy + 1 == m || nowy == m) {
			newx = nowx + 1; newy = 1;
		}
		else {
			newx = nowx; newy = nowy + 2;
		}
		bb[nowx][nowy] = 's';
		DFS(newx, newy, total + 1);
		bb[nowx][nowy] = '.';
	}


}

inline void process() {
	ans = 0;
	num = (m + 1) / 2;
	DFS(1, 1, 0);
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("C-small-attempt0.in", "r", stdin); freopen("C-small.out", "w", stdout);

	scanf("%d", &cases);
	for  (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
