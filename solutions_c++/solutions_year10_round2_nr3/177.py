#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>

#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

const int Mod = 100003;
const int N = 510;

int C[N][N];
int F[N][N];

int f(int k, int n) {
	int &res = F[k][n];
	if (res != -1) return res;

	res = 0;

	if (k == 1) {
		return res = 1;
	}

	for (int t = 1; t < n; ++t) {
		if (n - k - 1 >= k - t - 1) {
			res = (res + (long long)f(t, k) * C[n - k - 1][k - t - 1]) % Mod;
		}
	}

	return res;
}

int f(int n)
{
	int res = 0;
	for (int k = 1; k <= n - 1; ++k) {
		res = (res + f(k, n)) % Mod;
	}
	return res;
}

int main() {

	memset(F, -1, sizeof(F));
	C[0][0] = 1;
	for (int i = 1; i < N; ++i) {
		C[i][0] = C[i][i] = 1;
		for (int j = 1; j < i; ++j) {
			C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % Mod;
		}
	}

	vector<int> res(510);
	for (int i = 2; i <= 500; ++i) {
		res[i] = f(i);
		cerr << "f[" << i << "] = " << res[i] << endl;
	}

	int T;
	cin >> T;
	for (int cas = 1; cas <= T; ++cas) {
		int n;
		cin >> n;
		cout << "Case #" << cas << ": " << res[n] << endl;
	}
	return 0;
}
