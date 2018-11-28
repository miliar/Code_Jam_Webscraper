#include <cstdio>
#include <cstring>

const int oo = 1000000000;

int casei, cases, n, m, ans;
char st[10000];
int board[200][200];

inline void init() {
	scanf("%d", &n);
	m = n + n - 1;
	gets(st);
	for (int i = 0; i < m; ++i) {
		for (int j = 0; j < m; ++j) board[i][j] = -1;
		gets(st);		
		for (int j = strlen(st) - 1; j >= 0; --j)
			if (st[j] != ' ') board[i][j] = st[j] - '0';
	}
}

inline bool check(int px, int py) {
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < m; ++j) if (board[i][j] != -1) {
			int ii = px + px - i;
			int jj = py + py - j;

			if (ii >= 0 && ii < m && jj >= 0 && jj < m) if (board[ii][jj] != -1 && board[ii][jj] != board[i][j]) return false;
			if (jj >= 0 && jj < m) if (board[i][jj] != -1 && board[i][jj] != board[i][j]) return false;
			if (ii >= 0 && ii < m) if (board[ii][j] != -1 && board[ii][j] != board[i][j]) return false;
		}
	return true;
}

inline int abs(int now) {
	if (now < 0) return -now;
	else return now;
}

inline void process() {
	ans = oo;
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < m; ++j) {
			if (check(i, j)) {
				int t = abs(n - 1 - i) + abs(n - 1 - j) + n;
				t = t * t - n * n;
				if (t < ans) {
					ans = t;
					//printf("%d %d\n", i, j);
				}
			}
		}
}

inline void print() {
	printf("Case #%d: %d\n", casei, ans);
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("A-small-attempt1.in", "r", stdin);
	//freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}

	return 0;
}
