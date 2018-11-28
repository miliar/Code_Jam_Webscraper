#include <iostream>
#include <cassert>
using namespace std;

int main() {
	int N;
	cin >> N;
	for(int i = 1; i <= N; ++i) {
		cout << "Case #" << i << ": ";
		long long n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		long long X = x0, Y = y0;
		long long  T[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
		for(long long j = 0; j != n; ++j) {
			++T[3*(X%3)+(Y%3)];
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}
		long long sol = 0;
		for(int a = 0; a != 9; ++a) {
			for(int b = 0; b != 9; ++b) {
				for(int c = 0; c != 9; ++c) {
					if((((a%3)+(b%3)+(c%3))%3 == 0)
						&& (((a/3)+(b/3)+(c/3))%3 == 0)) {
						
						long long as = T[a], bs = T[b], cs = T[c];
						if(a == b) --bs;
						if(a == c) --cs;
						if(b == c) --cs;
						if(as && bs && cs)
							sol += as*bs*cs;
					}
				}
			}
		}
		assert(sol % 6 == 0);
		sol /= 6;
		cout << sol << endl;
	}
}
