using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
int n;
int D[10001];
int L[10001];
int R;
bool memo[110][110];
bool fmemo[110][110];
bool dp(int i, int j) {
    if (fmemo[i][j]) return memo[i][j];
    fmemo[i][j] = true;
	if (D[i] + min(D[i] - D[j], L[i]) >=R) return memo[i][j] = true;
	for (int k=i+1;k<=n;k++) {
		if (D[i] + min(D[i]-D[j], L[i]) >= D[k]) {
			if (dp(k, i)) return memo[i][j] = true;
		}
	}
	return memo[i][j] = false;
}
int main() {
	int tc;
	scanf("%d", &tc);
	int caseno = 1;
	while(tc-- !=0) {
		scanf("%d", &n);
		memset(fmemo,0, sizeof(fmemo));
		D[0] = 0;
		L[0] = 0;
		for (int i=1;i<=n;i++) {
			scanf("%d%d", D+i, L+i);
		}
		scanf("%d", &R);
		printf("Case #%d: ", caseno++);
		if (dp(1, 0)) puts("YES");
		else puts("NO");
	}
	return 0;
}