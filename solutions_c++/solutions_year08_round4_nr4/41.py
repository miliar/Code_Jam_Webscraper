#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int K, N;
int T;
string S;
int c[20][20];
int d[20][20];
int table[18][(1 << 16) + 2];
int st;

int memoi(int sv, int set) {
	if (set == 0) return table[sv][set] = d[st][sv];
	if (table[sv][set] != -1) return table[sv][set];

	int min = 9999999;
	for (int i = 0; i < N; ++i) {
		if (((set & (1 << i)) != 0) && (sv != i)) {
			int tmp = memoi(i, set - (1 << i));
			min <?= c[sv][i] + tmp;
		}
	}

	return (table[sv][set] = min);
}

int main() {
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		cin >> K; N = K;
		cin >> S;

		memset(c, 0, sizeof(c));
		memset(d, 0, sizeof(c));

		for (int i = 0; i < K; ++i) {
			for (int j = 0; j < K; ++j) {
				if (i == j) {
					continue;
				}
				for (int k = 0; k < S.size(); k += K) {
					if (S[k + i] != S[k + j]) c[i][j]++;
					if (k + K < S.size()) {
						if (S[k + j] != S[k + K + i]) d[i][j]++;
					}
				}
			}
		}

		int ret = 999999;
		for (int i = 0; i < K; ++i) {
			memset(table, -1, sizeof(table));
			st = i;
			ret <?= memoi(i, (1 << K) - 1 - (1 << i));
		}
		printf("Case #%d: %d\n", cn, ret + 1);
	}
}

