#include <iostream>
using namespace std;

int main() {
	int C;
	cin >> C;
	for (int i = 0; i < C; i++) {
		int N, M, A;
		cin >> N >> M >> A;
		
		cout << "Case #" << i+1 << ": ";
		bool done = false;
		for (int j = -N; j <= N && !done; j++)
			for (int k = -M; k <= M && !done; k++)
				for (int l = -N; l <= N && !done; l++) {
					int m = A+k*l;
					if (m != 0) {
						if (j == 0 || m%j) continue;
						m /= j;
					}
					if (m < -M || m > M) continue;
					for (int a = 0; a <= N; a++) {
						if (a+j < 0 || a+j > N || a+l < 0 || a+l > N) continue;
						for (int b = 0; b <= M; b++) {
							if (b+k < 0 || b+k > M || b+m < 0 || b+m > M) continue;
							done = true;
							cout << a << ' ' << b << ' ' << a+j << ' ' << b+k << ' ' << a+l << ' ' << b+m << endl;
							break;
						}
						break;
					}
				}
		if (!done) cout << "IMPOSSIBLE" << endl;
	}
}
