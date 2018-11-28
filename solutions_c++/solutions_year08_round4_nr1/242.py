#include <iostream>
using namespace std;

const int nn = 100000;

int M, V;

int it, lf;

int O[nn], C[nn];
int Z[nn];

int R[nn][2];

int test;

void update(int& R, int a, int b, int c = 0) {
	if (a == -2 || b == -2) return;
	if (R == -2 || R > a + b + c)
		R = a + b + c;
 }

int dfs(int x, int v) {
	if (R[x][v] != -1) return R[x][v];
	if (x > it) {
		if (v == Z[x]) return 0; else return -2;
	} else {
		int a[2][2]; 
		R[x][0] = R[x][1] = -2;
		a[0][0] = dfs(x*2, 0);
		a[0][1] = dfs(x*2, 1);
		a[1][0] = dfs(x*2+1, 0);
		a[1][1] = dfs(x*2+1, 1);
		if (O[x] == 1) {
			update(R[x][0], a[0][0], a[1][0]);
			update(R[x][0], a[0][1], a[1][0]);
			update(R[x][0], a[0][0], a[1][1]);
			update(R[x][1], a[0][1], a[1][1]);
			if (C[x]) {
				update(R[x][0], a[0][0], a[1][0], 1);
				update(R[x][1], a[0][1], a[1][0], 1);
				update(R[x][1], a[0][0], a[1][1], 1);
				update(R[x][1], a[0][1], a[1][1], 1);
			}
		} else {
			update(R[x][0], a[0][0], a[1][0]);
			update(R[x][1], a[0][1], a[1][0]);
			update(R[x][1], a[0][0], a[1][1]);
			update(R[x][1], a[0][1], a[1][1]);
			if (C[x]) {
				update(R[x][0], a[0][0], a[1][0], 1);
				update(R[x][0], a[0][1], a[1][0], 1);
				update(R[x][0], a[0][0], a[1][1], 1);
				update(R[x][1], a[0][1], a[1][1], 1);
			}
		}
	}
	return R[x][v];
}

void solve() {
	cin >> M >> V;
	it = (M-1) /2;
	lf = (M + 1) / 2;
	for (int i= 1; i <= it; i++) {
		cin >> O[i] >> C[i];
	}
	for (int i= it + 1; i <= M; i++) cin >> Z[i];
	memset(R, 0xff, sizeof(R));
	int res = dfs(1, V);
	cout << "Case #" << test << ": ";
	if (res == -2) cout << "IMPOSSIBLE" << endl; else cout << res << endl;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T; cin >> T;
	for (test = 1; test <= T; test++)
		solve();
	fclose(stdout);
	return 0;
}