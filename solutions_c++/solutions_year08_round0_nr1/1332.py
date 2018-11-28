#include <iostream>
#include <cstdio>
using namespace std;
const int MAXL = 100;
const int MAXQ = 1000;
const int MAXS = 100;
int Q, S;
char q[MAXQ + 10][MAXL + 10];
char s[MAXS + 10][MAXL + 10];
int dp[MAXQ + 10][MAXS + 10];
bool E[MAXQ + 10][MAXS + 10];


int rec(int k, int p) {
	if (dp[k][p] != -1) return dp[k][p];
	if (Q == k) return dp[k][p] = 0;
	int ret = 1 << 30, t;
	//if (strcmp(q[k], s[p]) == 0) return 1 << 30;
	if (E[k][p]) return 1 << 30;
	for (int i = 0; i < S; ++i) {
		t = rec(k + 1, i);
		if (t == 1 << 30) continue;
		if (i != p) ++t;
		ret = min(ret, t);
	}
	return dp[k][p] = ret;
}

void Solve(int tst) {
	scanf("%d", &S);
	for (int i = 0; i < S; ++i) {
		do {
			gets(s[i]);
		} while (!s[i][0]);
	}
	scanf("%d", &Q);
	for (int i = 0; i < Q; ++i) {
		do {
			gets(q[i]);
		} while (!q[i][0]);
	}
	int ans = 1 << 30, t;
	for (int i = 0; i <= Q; ++i)
		for (int j = 0; j <= S; ++j) {
			dp[i][j] = -1;
			E[i][j] = !strcmp(q[i], s[j]);
		}
	for (int i = 0; i < S; ++i) {		
		t = rec(0, i);
		ans = min(t, ans);
	}
	printf("Case #%d: %d\n", tst, ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N; ++i)
		Solve(i);
	return 0;
}
