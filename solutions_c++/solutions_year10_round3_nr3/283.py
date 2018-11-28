#include <cstdio>
#include <vector>

#define input "C-small-attempt0.in"
#define output "C.out"
using namespace std;

FILE *fin = freopen(input, "r", stdin);
FILE *fout = freopen(output, "w", stdout);

int min(int a, int b)
{
	return (a > b) ? b : a;
}

bool check(vector< vector< bool > > board, vector< vector< bool > > ck, int y, int x, int k)
{
	int i, j;

	for (i = y; i < y + k - 1; i++) {
		for (j = x; j < x + k; j++) {
			if (ck[i][j] || ck[i + 1][j]) return false;
			if (!(board[i][j] ^ board[i + 1][j])) return false;
		}
	}

	for (j = x; j < x + k - 1; j++) {
		for (i = y; i < y + k; i++) {
			if (ck[i][j] || ck[i][j + 1]) return false;
			if (!(board[i][j] ^ board[i][j + 1])) return false;
		}
	}

	return true;
}

int main()
{
	int cases, t;
	scanf("%d", &t);
	for (cases = 1; cases <= t; cases++) {
		int m, n;
		int i, j, k;
		char data[255];
		int res = 0;

		scanf("%d %d\n", &m, &n);
		vector< vector< bool > > board(m, vector< bool >(n, false));
		vector< vector< bool > > ck(m, vector< bool >(n, false));
		int mx = min(m, n);
		vector< int > cnt(mx, 0);

		for (i = 0; i < m; i++) {
			scanf("%s\n", &data);
			for (j = 0; j < n / 4; j++) {
				int num;
				if ('0' <= data[j] && data[j] <= '9') num = data[j] - '0'; else num = data[j] - 'A' + 10;
				if (num & 8) board[i][j * 4] = true;
				if (num & 4) board[i][j * 4 + 1] = true;
				if (num & 2) board[i][j * 4 + 2] = true;
				if (num & 1) board[i][j * 4 + 3] = true;
			}
		}

		for (k = mx; k >= 1; k--) {
			for (i = 0; i < m - k + 1; i++) {
				for (j = 0; j < n - k + 1; j++) {
					if (ck[i][j]) continue;
					if (check(board, ck, i, j, k)) { 
						cnt[k - 1]++; 
						int py, px;
						for (py = i; py < i + k; py++) {
							for (px = j; px < j + k; px++) {
								ck[py][px] = true;
							}
						}
					}
				}
			}

		}

		for (i = 0; i < mx; i++) {
			if (cnt[i] > 0) res++;
		}
		printf("Case #%d: %d\n", cases, res);
		for (i = mx - 1; i >= 0; i--) {
			if (cnt[i] > 0) printf("%d %d\n", i + 1, cnt[i]);
		}
	}

	return 0;
}