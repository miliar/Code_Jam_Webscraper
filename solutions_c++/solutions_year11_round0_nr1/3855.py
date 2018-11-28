#include <iostream>
#include <string>

using namespace std;

int N;
string o[100];
int pos[100];

int memo[101][101][101];

int go(int a, int b, int x) {
	if (x == N) return 0;
	int& res = memo[a][b][x];
	if (res != -1) return res;
	res = 1<<30;
	
	if (o[x] == "O") {
		int d = abs(pos[x] - a) + 1;
		for (int j = -d; j <= d; j++) {
			int bb = b + j;
			if (bb < 1 || bb > 100) continue;
			res = min(res, go(pos[x], bb, x + 1) + d);
		}
	} else {
		int d = abs(pos[x] - b) + 1;
		for (int j = -d; j <= d; j++) {
			int aa = a + j;
			if (aa < 1 || aa > 100) continue;
			res = min(res, go(aa, pos[x], x + 1) + d);
		}
	}
	
	return res;
}

void solve() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> o[i] >> pos[i];
	}
	memset(memo, -1, sizeof memo);
	cout << go(1, 1, 0) << endl;
}

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	return 0;
}
