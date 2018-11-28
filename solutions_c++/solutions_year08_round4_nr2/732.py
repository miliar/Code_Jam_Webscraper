#include <iostream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <cmath>
#include <utility>
#include <cassert>

using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}

int main() {
	int C; cin >> C;
	for (int i = 0; i < C; i++) {
		int N, M, A; cin >> N >> M >> A;
		for (int j = 0; j <= N; j++) {
			for (int k = 0; k <= M; k++) {
				for (int m = 0; m <= N; m++) {
					for (int n = 0; n <= M; n++) {
						if (abs(j*n-m*k) == A) {
							cout << "Case #" << i+1 << ": 0 0 " << j << " " << k << " "
								<< m << " " << n << "\n";
							goto end;
						}
					}
				}
			}
		}
		cout << "Case #" << i+1 << ": IMPOSSIBLE\n";
	end: continue;
	}
	return 0;
}