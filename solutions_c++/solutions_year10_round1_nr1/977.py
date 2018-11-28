#include <iostream>
#include <string.h>
#include <queue>

using namespace std;

typedef long long ll;

int main(int argc, char* argv[]) {
	int Tests;
	cin >> Tests;
	for (int test = 1; test <= Tests; ++test) {
		int N, K;
		cin >> N >> K;
		int f[N][N], f2[N][N], wr[N][N], wb[N][N];
		string s;
		getline(cin, s);
		for (int i = 0; i < N; ++i) {
			getline(cin, s);
			for (int j = 0; j < N; ++j) {
				if (s[j] == '.') {
					f[i][j] = 0;
				} else if (s[j] == 'R') {
					f[i][j] = 1;
				} else {
					f[i][j] = 2;
				}
				f2[i][j] = wr[i][j] = wb[i][j] = 0;
			}
		}

		for (int i = 0; i < N; ++i) {
			int k = N - 1;
			for (int j = N - 1; j >= 0; --j) {
				if (f[i][j] != 0) {
					f2[i][k] = f[i][j];
					--k;
				}
			}
		}

		bool r = false;
		bool b = false;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (f2[i][j] == 0 || (f2[i][j] == 1 && r) || (f2[i][j] == 2 && b)) continue;

				bool ok;

				ok = true;
				if (N - j >= K) {
					for (int k = 0; k < K; ++k) {
						if (f2[i][j] != f2[i][j + k]) {
							ok = false;
							break;
						}
					}
					if (ok) {
						if (f2[i][j] == 1) r = true;
						else b = true;
					}
				}

				ok = true;
				if (N - i >= K) {
					for (int k = 0; k < K; ++k) {
						if (f2[i][j] != f2[i + k][j]) {
							ok = false;
							break;
						}
					}
					if (ok) {
						if (f2[i][j] == 1) r = true;
						else b = true;
					}
				}

				ok = true;
				if (N - i >= K && N - j >= K) {
					for (int k = 0; k < K; ++k) {
						if (f2[i][j] != f2[i + k][j + k]) {
							ok = false;
							break;
						}
					}
					if (ok) {
						if (f2[i][j] == 1) r = true;
						else b = true;
					}
				}

				ok = true;
				if (N - i >= K && j + 1 >= K) {
					for (int k = 0; k < K; ++k) {
						if (f2[i][j] != f2[i + k][j - k]) {
							ok = false;
							break;
						}
					}
					if (ok) {
						if (f2[i][j] == 1) r = true;
						else b = true;
					}
				}
			}
		}
		if (r) {
			if (b) cout << "Case #" << test << ": Both" << endl;
			else   cout << "Case #" << test << ": Red" << endl;
		} else {
			if (b) cout << "Case #" << test << ": Blue" << endl;
			else   cout << "Case #" << test << ": Neither" << endl;
		}
	}
	return 0;
}
