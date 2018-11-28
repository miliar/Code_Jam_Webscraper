#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<int> VI;

VVLL operator*(const VVLL& a, const VVLL& b) {
	int N = a.size();
	int M = a[0].size();
	int L = b[0].size();
	assert( M == b.size() );
	VVLL ret(N, L);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < L; j++) {
			for (int k = 0; k < M; k++) {
				ret[i][j] += a[i][k] * b[k][j];
			}
		}
	}
	return ret;
}

VVLL myPower(const VVLL& a, int b) {
	if (b == 1) return a;
	return b%2 == 0 ? myPower(a*a, b/2) : myPower(a*a, b/2) * a;
}

long long calc(int R, int k, VI& g) {
	int N = g.size();
	VVLL T(N+1, N+1);
	T[N][N] = 1;
	for (int i = 0; i < N; i++) {
		int j = i;
		int c = k;
		int e = 0;
		int ng = 0;
		while (ng < N && g[j] <= c) {
			c -= g[j];
			e += g[j];
			j = (j+1) % N;
			ng++;
		}
		T[j][i] = 1;
		T[N][i] = e;
	}
	VVLL s(N+1, 1);
	s[0][0] = 1;
	VVLL f = myPower(T, R) * s;
	return f[N][0];
}

int main() {
	int TC;
	cin >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int R, k, N;
		cin >> R >> k >> N;
		VI g(N);
		for (int i = 0; i < N; i++) cin >> g[i];
		cout << "Case #" << tc << ": " << calc(R, k, g) << endl;
	}
}
