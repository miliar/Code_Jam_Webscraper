#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int table[11][1024];

int count(int a) {
	int ret = 0;
	while (a) {
		ret += a & 1;
		a >>= 1;
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		int n, m;
		cin >> n >> m;
		vector <string> a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		memset(table, -1, sizeof(table));

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < (1 << m); ++j) {
				bool ispos = true;
				for (int k = 0; k < m; ++k)
					if ((j & (1 << k)) && a[i][k] == 'x') ispos = false;
				for (int k = 0; k < m - 1; ++k)
					if ((j & (1 << k)) && (j & (1 << (k + 1)))) ispos = false;
				if (!ispos) continue;

				int isposnum = 0;
				for (int k = 0; k < m; ++k) {
					if (j & (1 << k)) {
						if (k != 0) isposnum |= (1 << (k - 1));
						if (k != m - 1) isposnum |= (1 << (k + 1));
					}
				}

				if (i == 0) {
					table[i][j] = count(j);
				} else {
					int ret = 0;
					for (int k = 0; k < (1 << m); ++k) {
						if (isposnum & k) continue;
						ret >?= table[i - 1][k];
					}
					table[i][j] = ret + count(j);
				}
			}
		}
		int ret = 0;
		for (int i = 0; i < (1 << m); ++i)
			ret >?= table[n - 1][i];
		printf("Case #%d: %d\n", cn, ret);
	}
}
