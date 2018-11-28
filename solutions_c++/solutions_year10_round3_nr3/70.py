
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

vector<pair<int, int> > solve(int n, int m, int board[512][512]) {
	vector<pair<int, int> > res;
	for (int size = n; size >= 1; --size) {
		static int num[512][512];
		for (int i = 0; i < n; ++i) {
			for (int j = m - 1; j >= 0; --j)
				if (board[i][j] == 2) {
					num[i][j] = 0;
				} else {
					num[i][j] = 1;
					if (j + 1 < m && board[i][j] != board[i][j + 1])
						num[i][j] += num[i][j + 1];
				}
		}
		static bool can[512][512];
		memset(can, 0, sizeof(can));
		for (int j = 0; j + size <= m; ++j) {
			for (int i = 0; i < n; ++i)
				if (num[i][j] >= size) {
					int ii = i;
					while (ii + 1 < n && num[ii + 1][j] >= size && board[ii + 1][j] != board[ii][j])
						++ii;
					for (int k = i; k <= ii; ++k)
						if (ii - k + 1 >= size) {
							can[k][j] = true;
						}
						i = ii;
				}
		}
		int cnt = 0;
		for (int i = 0; i + size <= n; ++i)
			for (int j = 0; j + size <= m; ++j)
				if (can[i][j]) {
					++cnt;
					for (int ii = 0; ii < size; ++ii)
						for (int jj = 0; jj < size; ++jj) {
							board[i + ii][j + jj] = 2;
						}
					for (int ii = -size + 1; ii <= size - 1; ++ii)
						for (int jj = -size + 1; jj <= size - 1; ++jj)
							if (i + ii >= 0 && i + ii < n && j + jj >= 0 && j + jj < m) {
								can[i + ii][j + jj] = false;
							}
				}
		if (cnt > 0)
			res.push_back(make_pair(size, cnt));
	}
	return res;
}

int main() {
	int cases;
	cin >> cases;
	for (int cas = 0; cas < cases; ++cas) {
		int n, m;
		cin >> n >> m;
		static int board[512][512];
		for (int i = 0; i < n; ++i) {
			string str;
			cin >> str;
			for (int j = 0; j < int(str.size()); ++j) {
				int ch;
				if (str[j] >= '0' && str[j] <= '9')
					ch = int(str[j] - '0');
				else
					ch = int(str[j] - 'A') + 10;
				for (int k = 0; k < 4; ++k) {
					board[i][j * 4 + k] = ((ch >> (4 - 1 - k)) & 1) > 0;
				}
			}
		}
		vector<pair<int, int> > res = solve(n, m, board);
		printf("Case #%d: %d\n", cas + 1, res.size());
		for (int i = 0; i < int(res.size()); ++i)
			printf("%d %d\n", res[i].first, res[i].second);
	}
	return 0;
}