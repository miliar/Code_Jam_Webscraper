#include <iostream>

using namespace std;

long long M[1024];
long long price[10][512];
long long dp[10][11][512];
const long long INF = 1e15;

int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		int N; cin >> N;
		for(int i=0;i<(1<<N);i++) cin >> M[i];
		for(int i=0;i<N;i++){
			for(int j=0;j<(1<<(N-1-i));j++) cin >> price[i][j];
		}
		int ans = 0;
		for(int i=0;i<(1<<N);i++) M[i] = N - M[i];
		for(int i=0;i<=N;i++){
			for(int j=0;j<(1<<N);j+=2){
				int m = max(M[j], M[j+1]);
				if(i >= m) dp[0][i][j/2] = 0;
				else if (i == m-1) dp[0][i][j/2] = price[0][j/2];
				else dp[0][i][j/2] = INF;
			}
		}
		for(int i=1;i<N;i++){
			for(int j=0;j<N;j++){
				for(int k=0;k<(1<<(N-i));k+=2){
					dp[i][j][k/2] = INF;
					dp[i][j][k/2] = min(dp[i][j][k/2], dp[i-1][j][k]+dp[i-1][j][k+1]);
					dp[i][j][k/2] = min(dp[i][j][k/2], dp[i-1][j+1][k]+dp[i-1][j+1][k+1]+price[i][k/2]);
				}
			}
		}
		printf("Case #%d: %d\n", test, dp[N-1][0][0]);
	}
}

/*
int main(){
	int TEST; cin >> TEST;
	for(int test=1;test<=TEST;test++){
		int N; cin >> N;
		for(int i=0;i<(1<<N);i++) cin >> M[i];
		for(int i=N-1;i>=0;i--){
			for(int j=0;j<(1<<i);j++) cin >> price[i][j];
		}
		int ans = 0;
		for(int i=0;i<(1<<N);i++) M[i] = N - M[i];
		for(int i=0;i<N;i++){
			for(int j=0;j<(1<<N);j+=(1<<(N-i))){
				bool flag = false;
				for(int k=0;k<(1<<(N-i));k++){
					if(M[j+k] > 0) flag = true;
				}
				if(flag){
					for(int k=0;k<(1<<(N-i));k++) M[j+k]--;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", test, ans);
	}
}
*/