#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

pair<long long, int> A[110];
pair<long long, int> B[110];
int n,m;
long long dp[110][110];
bool memo[110][110];

long long solve(int i, int j) {
	if (memo[i][j]) return dp[i][j];
	memo[i][j] = true;
	if (i>=n || j>=m) return dp[i][j] = 0;
	long long ret = max(solve(i+1, j), solve(i, j+1));
	
	long long TT = 0, BB = 0;
	for (int k=i;k<n;k++) {
		if (A[k].second == A[i].second) TT += A[k].first;
		if (A[k].second == B[j].second) BB += A[k].first;
		long long  AJ = 0 , BJ = 0;
		for (int l=j;l<m;l++) {
			if (B[l].second == A[i].second) AJ += B[l].first;
			if (B[l].second == B[j].second) BJ += B[l].first;
			long long take = max(min(BB, BJ) + solve(k+1, l+1), min(TT, AJ) + solve(k+1, l+1));
			ret = max(ret, take);
		}
	}
	return dp[i][j] = ret;
}

int main() {
	int t;
	cin>>t;
	int cnt = 1;
	while(t--) {
		memset(memo, 0, sizeof(memo));
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) {
			scanf("%lld%d", &A[i].first, &A[i].second);
		}
		for (int i=0;i<m;i++) {
			scanf("%lld%d", &B[i].first, &B[i].second);
		}
		long long take = solve(0, 0);
		printf("Case #%d: %lld\n", cnt++, take);
	}
//	system("pause");
	return 0;
}
