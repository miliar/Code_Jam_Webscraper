#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int N, M, A;

int go() {
	if (N * M < A) return 0;
	
	for (int area = A; area <= A + M; ++area) {
		int b = area - A, c = 1;
		int a, d;
		int st = max(area / M, 1);
		for (int a = st; a <= N; ++a) {
			if (area % a == 0 && area / a <= M) {
				d = area / a;
				printf("0 0 %d %d %d %d\n", a, b, c, d);
				if (a * d - b * c != A) while(1);
				if (a == c && b == d) while(1);
				if (a > N || b > M || c > N || d > M) while(1);
				return 1;
			}
		}
	}
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int cn = 1; cn <= T; ++cn) {
		cin >> N >> M >> A;
		printf("Case #%d: ", cn);
		if (go() == 0) printf("IMPOSSIBLE\n");
	}
}

