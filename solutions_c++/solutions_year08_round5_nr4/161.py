#include <cstdio>
#include <memory>

const int number = 10007;

int casei, cases, n, m, rocks, tttmp, ans;
int rock[20][2];
int combi[10010][10010];

inline void prepare() {
	memset(combi, 0, sizeof combi);
	combi[0][0] = 1;
	for (int i = 1; i <= 10007; ++i) {
		combi[i][0] = 1;
		for (int j = 1; j <= i; ++j) {
			combi[i][j] = combi[i - 1][j] + combi[i - 1][j - 1];
			combi[i][j] %= number;
		}
	}
}

inline void init() {
	scanf("%d%d%d", &n, &m, &rocks);
	for (int i = 0; i < rocks; ++i) scanf("%d%d", &rock[i][0], &rock[i][1]);
}

inline int CMod(int nown, int nowm) {
	if (nown < number && nowm < number)
		return combi[nown][nowm];
	if (nown % number < nowm % number) return 0;
	int tmp = CMod(nown / number, nowm / number);
	tmp *= combi[nown % number][nowm % number];
	return tmp % number;
}

inline int calc(int nown, int nowm) {
	if (2 * nown - nowm < 0) return 0;
	if (2 * nowm - nown < 0) return 0;
	if ((2 * nown - nowm) % 3 > 0) return 0;
	if ((2 * nowm - nown) % 3 > 0) return 0;
	int aa, bb;
	aa = (2 * nown - nowm) / 3;
	bb = (2 * nowm - nown) / 3;
	return CMod(aa + bb, aa);
}

inline void DFS(int nowr, int xx, int nown, int nowx, int nowy) {
	if (nown == 0) return;
	if (nowr == rocks) {
		tttmp = calc(n - nowx, m - nowy);
		tttmp *= nown * xx;
		tttmp %= number;
		if (tttmp < 0) tttmp += number;
		ans += tttmp;
		ans %= number;
		return;
	}

	DFS(nowr + 1, xx, nown, nowx, nowy);
	tttmp = calc(rock[nowr][0] - nowx, rock[nowr][1] - nowy);
	DFS(nowr + 1, -xx, (nown * tttmp) % number, rock[nowr][0], rock[nowr][1]);
}

inline void process() {
	ans = 0;
	for (int i = 0; i < rocks; ++i)
		for (int j = i + 1; j < rocks; ++j) if (rock[i][0] > rock[j][0] || (rock[i][0] == rock[j][0] && rock[i][1] > rock[j][1])) {
			int tmp;
			tmp = rock[i][0]; rock[i][0] = rock[j][0]; rock[j][0] = tmp;
			tmp = rock[i][1]; rock[i][1] = rock[j][1]; rock[j][1] = tmp;
		}
	DFS(0, 1, 1, 1, 1);
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);

	prepare();
/*	while (true) {
		int n, m;
		scanf("%d%d", &n, &m);
		printf("%d\n", CMod(n, m));
	}*/
	scanf("%d", &cases);
	for  (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
