#include <cstdlib>
#include <iostream>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

int T;
int M, N;
int B[512][512];
int ans[513];

void check(int xx, int yy, int n)
{
	if (B[xx][yy] < 0) return;
	for (int x = xx; x < xx + n; ++x) {
		for (int y = yy; y < yy + n; ++y) {
			if (x > xx && B[x][y] + B[x - 1][y] != 1) return;
			if (y > yy && B[x][y] + B[x][y - 1] != 1) return;
		}
	}
	for (int x = xx; x < xx + n; ++x) {
		for (int y = yy; y < yy + n; ++y) {
			B[x][y] = -1;
		}
	}
	++ans[n];
}

int solve()
{
	string x;
	int v;
	memset(B, 0, sizeof(B) );
	cin >> M >> N;
	for (int i = 0; i < M; ++i) {
		cin >> x;
		for (int j = 0; j < x.size(); ++j) {
			if (x[j] >= '0' && x[j] <= '9') v = x[j] - '0';
			else v = x[j] - 'A' + 10;
			for (int k = 3; k >= 0; --k) {
				if (v & (1 << k) ) B[i][j * 4 + 3 - k] = 1;
			}
		}
	}
	memset(ans, 0, sizeof(ans) );
	
/*
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < N; ++j) {
			printf("%d", B[i][j]);
		}
		printf("\n");
	}
*/
	
	for (int n = 512; n > 0; --n) {
		for (int i = 0; i <= M - n; ++i) {
			for (int j = 0; j <= N - n; ++j) {
				check(i, j, n);
			}
		}
	}
	
	return 0;
}

int main(int argc, char *argv[])
{
	cin >> T;
	
	for (int i = 0; i < T; ++i) {
		solve();
		int cnt = 0;
		for (int j = 0; j < 512; ++j) {
			if (ans[j] > 0) ++cnt;
		}
		printf("Case #%d: %d\n", i + 1, cnt);
		for (int j = 512; j > 0; --j) {
			if (ans[j]) {
				printf("%d %d\n", j, ans[j]);
			}
		}
	}
	
    return EXIT_SUCCESS;
}
