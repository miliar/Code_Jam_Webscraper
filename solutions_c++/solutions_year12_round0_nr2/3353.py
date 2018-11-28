#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn = 111;
bool A[maxn];
bool B[maxn];
bool C[maxn];
bool D[maxn];
int dp[maxn][maxn];
int main() {
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1 ; cas <= T ; cas ++) {
		int N , S , P;
		scanf("%d%d%d",&N,&S,&P);
		memset(A , false , sizeof(A));
		memset(B , false , sizeof(B));
		memset(C , false , sizeof(C));
		memset(D , false , sizeof(D));
		for (int i = 0 ; i < N ; i ++) {
			int t;
			scanf("%d",&t);
			for (int a = 0 ; a <= t && a <= 10 ; a ++) {
				for (int b = a ; b <= 10 && a + b <= t ; b ++) {
					int c = t - a - b;
					if (c < b || c > 10) continue;
					if (a + 2 < c) continue;
		//			printf("{%d %d %d %d}\n" , t , a , b , c);
					if (a + 2 == c) {
						if (c >= P) {
							A[i] = true;
						} else {
							B[i] = true;
						}
					} else {
						if (c >= P) {
							C[i] = true;
						} else {
							D[i] = true;
						}
					}
				}
			}
			
		}
		memset(dp , 0 , sizeof(dp));
		for (int i = 0 ; i < N ; i ++) {
			for (int j = 0 ; j <= S ; j ++) {
				if (A[i]) dp[i+1][j+1] = max(dp[i+1][j+1] , dp[i][j] + 1);
				if (B[i]) dp[i+1][j+1] = max(dp[i+1][j+1] , dp[i][j]);
				if (C[i]) dp[i+1][j] = max(dp[i+1][j] , dp[i][j] + 1);
				if (D[i]) dp[i+1][j] = max(dp[i+1][j] , dp[i][j]);
			}
		}
// 		for (int i = 0 ; i <= N ; i ++) {
// 			for (int j = 0 ; j <= S ; j ++) {
// 				printf("%d ",dp[i][j]);
// 			}
// 			puts("");
// 		}
		printf("Case #%d: %d\n", cas , dp[N][S]);
	}
	return 0;
}