#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int dp[101][256];
int a[101];

int main(){
	int T;
	scanf("%d",&T);
	for(int TT = 1; TT <=T; TT++){
		int D,I,m,n;
		scanf("%d%d%d%d",&D,&I,&m,&n);
		for(int i=0;i<n;i++){
			scanf("%d", &a[i]);
		}

		for(int i=0;i<256;i++){
			dp[0][i] = min(D, abs(a[0]-i));
		}
		for(int i=1;i<n;i++){
			for(int j=0;j<256;j++){
				int &v = dp[i][j];
				v = dp[i-1][j] + D; //删这个

				for(int k=max(j-m,0);k<=min(j+m,255);k++){//改这个
					int t = dp[i-1][k] + abs(a[i]-j);
					if(t < v)
						v = t;
				}
				
				if(m != 0){
					for(int k=0;k<256;k++){//中间插入
						
						int t = abs(k - j);
						if(t % m == 0)
							t = t / m - 1;
						else
							t = t / m;
						if(t < 0) t = 0;
						
						t = dp[i-1][k] + t * I + abs(a[i]-j);
						if(t < v)
							v = t;
					}
				}
			}
		}

		int ret=10000000;
		for(int i=0;i<256;i++){
			if(ret>dp[n-1][i])
				ret = dp[n-1][i];
		}


		printf("Case #%d: %d\n", TT, ret);
	}
}