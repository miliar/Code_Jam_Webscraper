#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 10240

int n, m;
int g[maxn],c[maxn],v[maxn];
int dp[maxn][2];

void input(){
     scanf("%d%d", &n, &m);
     for(int i=1; i<=(n-1)/2; i++)
		scanf("%d%d", &g[i], &c[i]);
	 for(int i=(n+1)/2; i<=n; i++)
		scanf("%d", &v[i]);
}

void work(){
     memset(dp, -1, sizeof(dp));
	 for(int i=(n+1)/2; i<=n; i++)dp[i][v[i]] = 0;
 	 for (int i=(n-1)/2; i>=1; i--){
		  int left = 2*i, right = 2*i+1;
		  for (int j=0; j<=1; j++)
			if (dp[left][j] != -1)
			for (int k=0; k<=1; k++)
			if (dp[right][k]!=-1){
			     if (g[i] == 1){
			     int t = j&k;
			     if (dp[i][t] == -1)dp[i][t]=dp[left][j]+dp[right][k];
		         else dp[i][t] = min(dp[i][t], dp[left][j]+dp[right][k]);	
		         if (c[i] == 1){
			        t = j|k;
					if (dp[i][t] == -1)dp[i][t] = dp[left][j]+dp[right][k]+1;
					else dp[i][t] = min(dp[i][t], dp[left][j]+dp[right][k]+1);	
			     }
			}
			else{
			    int t = j|k;
			    if (dp[i][t] == -1)dp[i][t] = dp[left][j]+dp[right][k];
			    else dp[i][t] = min(dp[i][t], dp[left][j]+dp[right][k]);
			    if (c[i] == 1){
					t = j&k;
			    	if (dp[i][t] == -1)dp[i][t] = dp[left][j]+dp[right][k]+1;
		            else dp[i][t] = min(dp[i][t], dp[left][j]+dp[right][k]+1);	
			}
			}	
        }
      }
	  if (dp[1][m] == -1)printf("IMPOSSIBLE\n");
      else  printf("%d\n", dp[1][m]);
}

int main(){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cases,k=1;
	scanf("%d", &cases);
	while(cases-->0){
		input();
		printf("Case #%d: ", k++);
		work();	
	}	
	return 0;
}
