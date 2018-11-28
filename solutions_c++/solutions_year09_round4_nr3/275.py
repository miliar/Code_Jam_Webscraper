#include <cstdio>
#include <cassert>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

void initialize() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
}

const int MAXN = 110;
const int MAXK = 110;

bool sm[MAXN][MAXN];

bool used[MAXN];
int pr[MAXN];
int n;

bool DFS(int i) {
	if (used[i])
		return false;
	used[i] = true;
	for (int j = 0; j < n; ++j)
		if (sm[i][j] && ((pr[j] == -1) || (DFS(pr[j])))) {
			pr[j] = i;
			return true;
		}
	return false;
}

int PS() {
	for (int i = 0; i < n; ++i)
		pr[i] = -1;
	int res = 0;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j)
			used[j] = false;
		if (DFS(i)) res++;
	}
	return n - res;
}

/*int solve2() {
	int can[1 << MAXN];
	for (int i = 0; i < (1 << n); ++i) {
		bool can1 = true;
		for (int p = 0; p < n; ++p)
			for (int q = 0; q < n; ++q)
				if ((i & (1 << p)))
					if ((i & (1 << q)))
						if (sm[p][q] || sm[q][p] || (p == q))
							continue;
						else
							can1 = false;
		if (can1) can[i] = 1; else can[i] = n;
		for (int j = i - 1; j > 0; j = (j - 1) & i)
			can[i] = min(can[i], can[j] + can[i ^ j]);
	}
	return can[(1 << n) - 1];
}*/

void solve() {
	int k;
	cin >> n >> k;
	int price[MAXN][MAXK];
	
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < k; ++j){
			cin >> price[i][j];
//			cout << price[i][j] << endl;
		}
	}
	//sm means less
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			sm[i][j] = true;
			for (int u = 0; u < k; ++u) {
				if ((price[i][u] >= price[j][u]))
					sm[i][j] = false;
			}
		}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
			for (int k = 0; k < n; ++k)
				if (sm[i][j] && sm[j][k])
					assert(sm[i][k]);
	for (int i = 0; i < n; ++i)
		used[i] = false;
	for (int i = 0; i < n; ++i)
		used[i] = false;
	int res = PS();
/*	if (res != solve2()) {
		cerr << res << endl;
		cerr << solve2() << endl;
		cerr << n << " " << k << endl;
		cerr << endl;

		cout << n << " " << k << endl;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < k; ++j)
				cout << price[i][j] << " ";
			cout << endl;
		}
		cout << endl << endl << endl;
//		assert(res == solve2());
	}*/
//	res = solve2();
	cout << res << endl;
}

int main() {
	initialize();
	int t = 0;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cerr << "Case #" << (i + 1) << ": " << endl;
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
	return 0;
}
