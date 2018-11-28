#include <iostream>
using namespace std;

int achooseb[501][501];

int main() {
	for (int i = 0; i <= 500; i++) achooseb[i][0] = 1;
	for (int i = 1; i <= 500; i++)
		for (int j = 1; j <= 500; j++)
			achooseb[i][j] = (achooseb[i-1][j-1]+achooseb[i-1][j])%100003;
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		
		long long dp[n+1][n]; // How many ways can position i be the end of a pure sequence where it is the jth element of the set
		for (int i = 2; i <= n; i++) {
			dp[i][1] = 1;
			for (int j = 2; j < i; j++) {
				dp[i][j] = 0;
				for (int k = 1; k < j; k++)
					dp[i][j] = (dp[i][j]+dp[j][k]*achooseb[i-j-1][j-k-1])%100003;
			}
		}
		int ans = 0;
		for (int i = 1; i < n; i++)
			ans = (ans+dp[n][i])%100003;
		
		cout << "Case #" << t << ": " << ans << endl;
	}
}
