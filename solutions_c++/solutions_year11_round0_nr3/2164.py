#include <iostream>
#include <cassert>
#include <memory.h>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int powSize = 21;
const int maxlen = 1000100;

int T, N;
vector<int> v;
int ppow[powSize];

struct binary {
	int d[powSize];
	binary(){}
	binary(int num) {
		memset(d, 0, sizeof(d));
		for (int i = powSize - 1; i >= 0; i--) {
			if (num >= ppow[i]) {
				num -= ppow[i];
				d[i] = 1;
			}
		}
	}

	inline int getInt() {
		int res = 0;
		for (int i = 0; i < powSize; i++) res += d[i] * ppow[i];
		return res;
	}
	inline friend bool operator==(const binary &xx, const binary &yy) {
		for (int i = 0; i < powSize; i++) if (xx.d[i] != yy.d[i]) return false;
		return true;
	}
	inline friend bool operator!=(const binary &xx, const binary &yy) {
		for (int i = 0; i < powSize; i++) if (xx.d[i] != yy.d[i]) return true;
		return false;
	} 	
	inline friend binary operator+(const binary &xx, const binary &yy) {
		binary res;
		for (int i = 0; i < powSize; i++) res.d[i] = (xx.d[i] ^ yy.d[i]);
		return res;
	}
};

binary mas[maxlen];

int main() {
	ppow[0] = 1;
	for (int i = 1; i < powSize; i++) ppow[i] = ppow[i - 1] * 2;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N;
		v.resize(N);
		for (int i = 0; i < N; i++) cin >> v[i];
		for (int i = 0; i < N; i++) mas[i] = binary(v[i]);

		binary nnul(0);
		binary now(0);
		for (int i = 0; i < N; i++) now = now + mas[i];

		if (nnul != now) {
			cout << "Case #" << t << ": NO" << endl;
			continue;
		} else {
			sort(v.begin(), v.end());
			int sum = 0;
			for (int i = 1; i < N; i++) sum += v[i];
			cout << "Case #" << t << ": " << sum << endl;
		}
	}
}