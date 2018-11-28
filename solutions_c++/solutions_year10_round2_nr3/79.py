#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

typedef long long ll;
const int MOD = 100003;
ll dp[510][510];
ll C[510][510];

void precompute(){
	for(int i=0; i<=500; ++i) C[i][0] = C[i][i] = 1;
	for(int i=1; i<=500; ++i)
		for(int j=1; j<i; ++j)
			C[i][j] = (C[i-1][j] + C[i-1][j-1]) % MOD;
	///////////
	for(int i=2; i<=500; ++i) dp[i][1] = 1;
	for(int i=2; i<=500; ++i){
		for(int k=2; k<i; ++k){
			// i is k-th element in S < {2,...,i}
			dp[i][k] = 0;
			for(int l=1; l<k; ++l){
				// k is l-th element in S
				dp[i][k] = ( dp[i][k] + dp[k][l] * C[i-k-1][k-l-1] ) % MOD;
			}
		}
	}
}

int main()
{
	precompute();
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		int n;
		scanf("%d", &n);
		ll res = 0;
		for(int i=1; i<n; ++i) res += dp[n][i];
		printf("Case #%d: %lld\n", iii, res%MOD);
	}
	return 0;
}
