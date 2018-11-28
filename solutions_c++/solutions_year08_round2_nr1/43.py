#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

long long N, a, b, c, d, x0, y0, M;
long long ret;
vector <long long> X, Y;
long long t[3][3];

int main() {
	int T;
	scanf("%d", &T);

	for (int cn = 1; cn <= T; ++cn) {
		scanf("%Ld%Ld%Ld%Ld%Ld%Ld%Ld%Ld", &N, &a, &b, &c, &d, &x0, &y0, &M);
		X.clear(), Y.clear();
		
		X.push_back(x0), Y.push_back(y0);
		for (int i = 0; i < N - 1; ++i) {
			X.push_back((a * X.back() + b) % M);
			Y.push_back((c * Y.back() + d) % M);
		}
		for (int i = 0; i < 3; ++i)
			for (int j = 0; j < 3; ++j)
				t[i][j] = 0;

		for (int i = 0; i < N; ++i) {
			t[X[i] % 3][Y[i] % 3]++;
		}

		ret = 0;
		for (int i = 0; i < 9; ++i) {
			for (int j = i; j < 9; ++j) {
				for (int k = j; k < 9; ++k) {
					int xmod = (i / 3 + j / 3 + k / 3) % 3;
					int ymod = (i % 3 + j % 3 + k % 3) % 3;
					if (xmod == 0 && ymod == 0) {
						long long n1 = t[i / 3][i % 3];
						long long n2 = t[j / 3][j % 3];
						long long n3 = t[k / 3][k % 3];

						if (i == j && j == k) { // all - same
							ret += n1 * (n2 - 1) * (n3 - 2) / 6;
							continue;
						} else if (i == j || j == k || k == i) { // two of three - same
							if (i == j) {
								ret += n1 * (n2 - 1) * n3 / 2;
							} else if (j == k) { 
								ret += n1 * n2 * (n3 - 1) / 2;
							} else if (k == i) {
								ret += (n1 - 1) * n2 * n3 / 2;
							}
							continue;
						} else {
							ret += n1 * n2 * n3;
						}
					}
				}
			}
		}
		cout << "Case #" << cn << ": " << ret << endl;
	}
}
