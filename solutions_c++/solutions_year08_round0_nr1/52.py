#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
#include<map>
#include<string>
using namespace std;

char name[128][128];
int cnt;
int getId(char str[])
{
	for(int i = 0; i < cnt; i++)
	{
		if(strcmp(str,name[i])==0)
			return i;
	}return -1;
}
char str[1024];
#define N 1024
int p[N],p_cnt;

int dp[N][128];
#define INF 1000000000
int main()
{	

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		cnt=0,p_cnt=0;
		int s,q;
		scanf("%d\n",&s);
		while(s--) gets(name[cnt++]);
		scanf("%d\n",&q);
		while(q--){
			gets(str);
			p[p_cnt++]=getId(str);
		}
		memset(dp,0,sizeof(dp));
		int i;
		for( i=0;i<cnt;i++){
			if(p[0]==i) dp[0][i]=INF;
		}

		for( i=1;i<p_cnt;i++){
			for(int j=0;j<cnt;j++){
				if(p[i]==j){
					dp[i][j]=INF;
					continue;
				}
				int min=INF;
				if(dp[i-1][j]!=INF){
					if(min>dp[i-1][j])
						min=dp[i-1][j];
				}
				for(int k=0;k<cnt;k++){
					if(k==j) continue;
					if(dp[i-1][k]!=INF){
						if(min>dp[i-1][k]+1)
							min=dp[i-1][k]+1;
					}
				}
				dp[i][j]=min;
			}
		}		
		int re=INF;
		for(i=0;i<cnt;i++){
			if(dp[p_cnt-1][i]!=INF){
				if(re>dp[p_cnt-1][i])
					re=dp[p_cnt-1][i];
			}
		}
		printf("%d\n",re);
	}
	return 0;
}