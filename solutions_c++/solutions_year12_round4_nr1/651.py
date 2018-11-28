#include<cstdio>
#include<cstring>
#include<cmath>

const int N = 10005;

int d[N];
int l[N];
int dp[N];
bool flag[N];
int D;

int main(){
//	freopen("A-large.in", "r" , stdin);
//	freopen("out.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--){
		int n;
		scanf("%d" , &n);
		int i;
		for(i = 0;i < n;i++){
			scanf("%d%d" , &d[i], &l[i]);
		}
		scanf("%d" , &D);
		bool can = false;
		memset(flag, false, sizeof(flag));
		memset(dp, 0, sizeof(dp));
		if(l[0] < d[0]){
			can = false;
		}else{
			dp[0] = d[0];
			while(1){
				int max = -1;
				for(int i = 0;i < n;i++){
					if(flag[i]) continue;
					if(max == -1 || dp[max] < dp[i]) max = i;
				}
				if(max == -1) break;
				flag[max] = true;
				if(d[max] + dp[max] >= D){
					can = true;
					break;
				}
				for(int i = 0;i < n;i++){
					if(!flag[i] && abs(d[i] - d[max]) <= dp[max]){
						int temp = abs(d[i] - d[max]) < l[i] ? abs(d[i] - d[max]) : l[i];
						dp[i] = dp[i] > temp ? dp[i] : temp;
					}
				}
			}
		}
		if(can) printf("Case #%d: YES\n", ++ii);
		else printf("Case #%d: NO\n", ++ii);
	}
	return 0;
}