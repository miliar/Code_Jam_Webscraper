#include <stdio.h>
#include <memory.h>

#define MOD 10009
char s[1000];
char w[100][100];
int cnt[255];
int res[10];
int k, n;

void go(int k) {
	int sum = 0, prd = 1;
	for (int i = 0; s[i]; ++i) {
		if (s[i] == '+') {
			sum += prd;
			prd = 1;
		} else {
			prd *= cnt[s[i]];
		}
	}
	res[::k - k] += prd + sum;
	res[::k - k] %= MOD;
	if (k == 0) return;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; w[i][j]; ++j)
			cnt[w[i][j]]++;
		go(k-1);
		for (int j = 0; w[i][j]; ++j)
			cnt[w[i][j]]--;
	}
}

void solve() {
	scanf("%s", s);
	scanf("%d%d\n", &k, &n);
	for (int i = 0; i < n; ++i)
		gets(w[i]);
	memset(cnt, 0, sizeof(cnt));
	memset(res, 0, sizeof(res));
	go(k);
	for (int i = 1; i <= k; ++i)
		printf(" %d", res[i]);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d:", i+1);
		solve();
		printf("\n");
	}
}