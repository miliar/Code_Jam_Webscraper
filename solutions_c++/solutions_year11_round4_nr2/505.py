#include <iostream>

using namespace std;

void process(long long W[500][500], long long SUM[500][500], int R, int C, int k) {
	//cout << "k = " << k << endl;
	for (int r0 = 0; r0 <= R - k; ++r0) {
		for (int c0 = 0; c0 <= C - k; ++c0) {
			//cout << "(r0,c0) = (" << r0 << "," << c0 << ")" << endl;
			if (r0 == 0 && c0 == 0) {
				SUM[r0][c0] = 0;
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						SUM[r0][c0] += W[r][c] * r;
					}
				}
			} else if (c0 > 0) {
				SUM[r0][c0] = SUM[r0][c0 - 1];
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0 - 1; c <= c0 - 1; ++c) {
						SUM[r0][c0] -= W[r][c] * r;
					}
				}
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0 + k - 1; c <= c0 + k - 1; ++c) {
						SUM[r0][c0] += W[r][c] * r;
					}
				}
			} else {
				//c0 = 0
				SUM[r0][c0] = SUM[r0 - 1][c0];
				for (int r = r0 - 1; r <= r0 - 1; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						SUM[r0][c0] -= W[r][c] * r;
					}
				}
				for (int r = r0 + k - 1; r <= r0 + k - 1; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						SUM[r0][c0] += W[r][c] * r;
					}
				}
			}
		}
	}
}

void process2(long long W[500][500], long long WSUM[500][500], int R, int C, int k) {
	for (int r0 = 0; r0 <= R - k; ++r0) {
		for (int c0 = 0; c0 <= C - k; ++c0) {
			if (r0 == 0 && c0 == 0) {
				WSUM[r0][c0] = 0;
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						WSUM[r0][c0] += W[r][c];
					}
				}
			} else if (c0 > 0) {
				WSUM[r0][c0] = WSUM[r0][c0 - 1];
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0 - 1; c <= c0 - 1; ++c) {
						WSUM[r0][c0] -= W[r][c];
					}
				}
				for (int r = r0; r < r0 + k; ++r) {
					for (int c = c0 + k - 1; c <= c0 + k - 1; ++c) {
						WSUM[r0][c0] += W[r][c];
					}
				}
			} else {
				//c0 = 0
				WSUM[r0][c0] = WSUM[r0 - 1][c0];
				for (int r = r0 - 1; r <= r0 - 1; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						WSUM[r0][c0] -= W[r][c];
					}
				}
				for (int r = r0 + k - 1; r <= r0 + k - 1; ++r) {
					for (int c = c0; c < c0 + k; ++c) {
						WSUM[r0][c0] += W[r][c];
					}
				}
			}
			/*if (k == 5 && R == 6) {
				cout << "WSUM[" << r0 << "," << c0 << "] = " << WSUM[r0][c0] << endl;
			}*/
		}
	}
}

bool check(long long W[500][500], long long SUM[500][500], long long WSUM[500][500], int r0,
		int c0, int k) {
	int S = SUM[r0][c0] - W[r0][c0] * r0 - W[r0][c0 + k - 1] * r0
			- W[r0 + k - 1][c0] * (r0 + k - 1) - W[r0 + k - 1][c0 + k - 1] * (r0 + k
			- 1);
	int WS = WSUM[r0][c0] - W[r0][c0] - W[r0][c0 + k - 1] - W[r0 + k - 1][c0]
			- W[r0 + k - 1][c0 + k - 1];
	if (r0 == 1 && c0 == 1 && k == 5) {
		/*cout << "*****" << endl;
		cout << SUM[r0][c0] << " -->" << S << endl;
		cout << WSUM[r0][c0] << " --> " << WS << endl;
		cout << (2 * r0 + k - 1) << endl;
		cout << "*****" << endl;*/
	}
	return (2 * r0 + k - 1) * WS == 2 * S;
}

int check(long long W[500][500], long long WT[500][500], long long SUM[500][500],
		long long SUMT[500][500], long long WSUM[500][500], long long WSUMT[500][500], int R, int C,
		int k) {
	for (int r0 = 0; r0 <= R - k; ++r0) {
		for (int c0 = 0; c0 <= C - k; ++c0) {
			if (check(W, SUM, WSUM, r0, c0, k) && check(WT, SUMT, WSUMT, c0, r0, k)) {
				return k;
			}

		}
	}
	return -1;
}

int main() {
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		int R, C, D;
		scanf("%d %d %d", &R, &C, &D);
		static long long W[500][500], WT[500][500];
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c) {
				char ch;
				scanf(" %c", &ch);
				//cout << "read " << ch << endl;
				W[r][c] = ch - '0';
				//cout << "convert to " << W[r][c] << endl;
				WT[c][r] = W[r][c];
			}
		}
		int ans = -1;
		for (int k = min(R, C); k >= 3 && ans == -1; --k) {
			static long long SUM[500][500], SUMT[500][500];
			static long long WSUM[500][500], WSUMT[500][500];
			process(W, SUM, R, C, k);
			//cout << "ok" << endl;
			process2(W, WSUM, R, C, k);
			//cout << "ok" << endl;
			process(WT, SUMT, C, R, k);
			//cout << "ok" << endl;
			process2(WT, WSUMT, C, R, k);
			//cout << "ok" << endl;
			ans = check(W, WT, SUM, SUMT, WSUM, WSUMT, R, C, k);
			//cout << "ok" << endl;
		}
		printf("Case #%d: ", test);
		if (ans == -1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
