#include<iostream>

#define MOD 100003

using namespace std;

long long dp[512][512];
long long c[512][512];

int main(){
	int csn;

	for(int i = 0; i < 512; ++i)
		c[i][0] = 1;
	
	for(int i = 1; i < 512; ++i)
		for(int j = 1; j < 512; ++j)
			c[i][j] = (c[i-1][j] + c[i-1][j-1]) % MOD;

	for(int i = 2; i < 512; ++i)
		dp[i][1] = 1;

	for(int i = 3; i < 512; ++i){
		int j, k;
		for(int j = 2; j < i; ++j){
			for(k = 1; k < j; ++k){
				long long tmp = (dp[j][k] * c[i - j - 1][j - k - 1]) % MOD;
				dp[i][j] = (dp[i][j] + tmp) % MOD;
			}
		}
	}

	
	cin >> csn;

	for(int cs = 1; cs <= csn; ++cs){
		long long sum = 0;
		int n;

		cin >> n;

		for(int i = 0; i < n; ++i)
			sum = (sum + dp[n][i]) % MOD;

		cout << "Case #" << cs << ": " << sum << endl;
	}

	return 0;
}
