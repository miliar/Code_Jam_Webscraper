#include <iostream>
#include <string>
using namespace std;

int n, N;
long long A, B, C, D, x0, y0, M;
long long num[3][3];

void add(long long x, long long y) {
	num[x%3][y%3]++;
}

int main() {
	cin >> N;
	for (int tcs = 1; tcs <= N; tcs++) {
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		memset(num, 0, sizeof(num));
		long long X = x0, Y = y0;
		add(X, Y);
		for (int i = 1; i < n; i++) {
			X = (A * X + B) % M;
  			Y = (C * Y + D) % M;
			add(X, Y);
		}
		long long xx[] = {0, 1, 2, 0, 1, 2, 0, 1, 2};
		long long yy[] = {0, 0, 0, 1, 1, 1, 2, 2, 2};
		long long res = 0;
		for (int i = 0; i < 9; i++) {
			for (int j = i; j < 9; j++) {
				for (int k = j; k < 9; k++) {
					if ((xx[i] + xx[j] + xx[k]) % 3 == 0 && (yy[i] + yy[j] + yy[k]) % 3 == 0) {
						if (i == j && j == k) {
							res += (num[xx[i]][yy[i]] * (num[xx[i]][yy[i]] - 1) * (num[xx[i]][yy[i]] - 2)) / 6;
						} else if (i == j) {
							res += ((num[xx[i]][yy[i]] * (num[xx[i]][yy[i]] - 1)) / 2) * num[xx[k]][yy[k]];
						}  else if (j == k) {
							res += ((num[xx[j]][yy[j]] * (num[xx[j]][yy[j]] - 1)) / 2) * num[xx[i]][yy[i]];
						} else {
							res += num[xx[i]][yy[i]] * num[xx[j]][yy[j]] * num[xx[k]][yy[k]];
						}
					}
				}
			}
		}
		cout << "Case #" << tcs << ": " << res << endl;
	}
	return 0;
}
