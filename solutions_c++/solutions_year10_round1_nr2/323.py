#include <iostream>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	int val[100];
	int dp[100][256];
	for(int test=1;test<=TEST;test++){
		int D, I, M, N; cin >> D >> I >> M >> N;
		for(int i=0;i<N;i++) cin >> val[i];
		for(int i=0;i<256;i++) dp[0][i] = abs(i-val[0]);
		for(int i=1;i<N;i++){
			for(int j=0;j<256;j++){
				dp[i][j] = dp[i-1][j] + D;
				if(j == val[i]) dp[i][j] = min(dp[i][j], D*i);
				dp[i][j] = min(dp[i][j], dp[i-1][j] + abs(j-val[i]));	
				if(M!=0){
					for(int k=0;k<256;k++){
						dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(j-val[i]) + max(abs(j-k)-1,0)/M*I);
					}
				}
			}
		}
		int ans = dp[N-1][0];
		for(int i=0;i<256;i++){
			ans = min(ans, dp[N-1][i]);
		}
		printf("Case #%d: %d\n", test, ans);
	}
}