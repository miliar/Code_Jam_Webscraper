#include <vector>
#include <queue>
#include <iostream>

using namespace std;

typedef long long ll;
typedef vector<bool> VB;

const int N = 1000;

int lp[N + 1];
int d[N + 1][N + 1];

void erasto() {
	memset(lp, 0, sizeof(lp));
	for (int i = 2; i <= N; ++i)
		if (lp[i] == 0) { 
			for (int j = i; j <= N; j += i) 
				lp[j] = i;
		}
}

int gcd(int a, int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int numSets(int A, int B, int P) {
	int res = 0;
	VB mark(B + 1);
	for (int i = A; i <= B; ++i) 
		if (!mark[i]) {
			++res;
			mark[i] = true;
			if (lp[i] < P)
				continue;
			queue<int> q;
			q.push(i);
			while (!q.empty()) {
				int x = q.front();
				q.pop();
				for (int y = A; y <= B; ++y)
					if (!mark[y] && lp[d[x][y]] >= P) {
						mark[y] = true;
						q.push(y);
					}
			}
		}
	return res;
}

int main() {
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int nCases;
	cin >> nCases;
	erasto();
	for (int i = 0; i <= N; ++i)
		for (int j = 0; j <= N; ++j)
			d[i][j] = gcd(i, j);
	int A, B, P;
	for (int c = 1; c <= nCases; ++c) {
		cin >> A >> B >> P;
		printf("Case #%d: %d\n", c, numSets(A, B, P));
	}
	return 0;
}