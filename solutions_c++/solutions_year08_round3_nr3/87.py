#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const long long MOD = 1000000007;

int main() {
	int N;
	cin >> N;
	for(int nacho = 1; nacho <= N; nacho++) {
		long long n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;
		vector<long long> A(m);
		vector<long long> speeds(n);
		for(int i = 0; i < m; i++)
			cin >> A[i];
		
		for(int i = 0; i < n; i++) {
			speeds[i] = A[i%m];
			A[i%m] = (X * A[i%m] + Y * (i + 1))%Z;
		}
		
		vector<long long> dp(n, 1);
		dp[0] = 1;
		for(int i = 1; i < n; i++) {
			for(int j = i-1; j >= 0; j--) {
				if(speeds[i] > speeds[j]) {
					dp[i] += dp[j];
					dp[i] = dp[i]%MOD;
				}
			}
		}
		
		long long sol = 0;
		for(int j = n-1; j >= 0; j--) {
			sol += dp[j];
			sol = sol%MOD;
		}
		
		cout << "Case #" << nacho << ": " << sol << endl;
	}
	
	return 0;
}
