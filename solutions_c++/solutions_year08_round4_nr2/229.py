#include <iostream>
using namespace std;

int test;

void solve() {
	int x1, x2, x3, y1, y2, y3;
	x1 = -1;

	int A, N, M;
	cin >> N >> M >> A;
	
	for (int X = 0; X <= N; X++) for (int Y = 0; Y <= M; Y++) {
		for (int x = 0; x <= N; x++) for (int y = 0; y <= M && x1 == -1; y++) {
			int D = x*Y + y*X - X*Y;
			if (D == A) {
				x1 = X; y1 = 0;
				x2 = 0; y2 = Y;
				x3 = x; y3 = y;
				break;
			}
		}
	}

	cout << "Case #" << test << ": ";
	if (x1 == -1) cout << "IMPOSSIBLE" << endl; else
		cout << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T; cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	fclose(stdout);
	return 0;
}