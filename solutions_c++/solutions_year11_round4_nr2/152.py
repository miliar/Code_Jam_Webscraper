#include <stdio.h>
#include <algorithm>

using namespace std;


int n,m;
char dat[512][512];
long long sum[512][512];
long long sum2[512][512];
long long sum3[512][512];

int main(){
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++){
		scanf("%d%d%*d",&n,&m);
		for(int i = 0;i < n;i++){
			scanf("%s",dat[i]);
		}
		for(int i = 0;i < n; i++) {
			sum[i][0] = 0;
			sum3[i][0] = 0;
			for(int j = 0;j < m; j++){
				dat[i][j] -= '0';
				sum[i][j+1] = sum[i][j] + (dat[i][j]);
				sum3[i][j+1] = sum3[i][j] + j * dat[i][j];
			}
		}
		for(int i = 0;i < n;i ++) {
			for(int j = 0;j <= m; j++) {
				sum2[i+1][j] = sum2[i][j] + sum[i][j];
			}
		}
		int ans = -1;
		for(int k = min(n,m); k >= 3; k--) {
			int flg = 0;
			for(int j = k;j <= m;j ++) {
				long long cursum = 0,cursum2 = 0;
				for(int i = 0;i < k; i++) {
					cursum += i * (sum[i][j] - sum[i][j-k]);
				}
				for(int i = j-k;i < j; i++) {
					cursum2 += i * (sum2[k][i+1] - sum2[k][i]);
				}
				for(int i = k; i <= n;i ++) {
					if((cursum - (i-k)*(dat[i-k][j-k]+dat[i-k][j-1]) - (i-1)*(dat[i-1][j-k]+dat[i-1][j-1]))*2
						== (2*i-k-1) * (sum2[i][j] - sum2[i-k][j] - sum2[i][j-k] + sum2[i-k][j-k] - (dat[i-k][j-k]+dat[i-k][j-1]+dat[i-1][j-k]+dat[i-1][j-1]))) {
						if((cursum2 - (j-k) * (dat[i-k][j-k] + dat[i-1][j-k]) - (j-1)*(dat[i-k][j-1] + dat[i-1][j-1])) * 2
							== (2*j-k-1) * (sum2[i][j] - sum2[i-k][j] - sum2[i][j-k] + sum2[i-k][j-k] - (dat[i-k][j-k]+dat[i-k][j-1]+dat[i-1][j-k]+dat[i-1][j-1]))) {
							flg = 1;
							break;
						}
					}

					cursum -= (i-k) * (sum[i-k][j] - sum[i-k][j-k]);
					cursum += i * (sum[i][j] - sum[i][j-k]);

					cursum2 -= sum3[i-k][j] - sum3[i-k][j-k];
					cursum2 += sum3[i][j] - sum3[i][j-k];
				}
				if(flg) break;
			}
			if(flg) {
				ans = k;
				break;
			}
		}
		printf("Case #%d: ",testcase);
		if(ans == -1){
			printf("IMPOSSIBLE\n");
		}else {
			printf("%d\n",ans);
		}
	}
	return 0;
}
