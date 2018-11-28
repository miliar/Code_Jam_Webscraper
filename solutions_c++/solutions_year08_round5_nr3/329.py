#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int count(int bit){
	int cnt=0;
	while (bit>0){
		cnt+=bit&1;
		bit = bit>>1;
	}
	return cnt;
}

bool check(int bit,int m){
	for (int i=1;i<m;i++){
		int b1=(bit>>i)&1;
		int b2=(bit>>(i-1))&1;

		if (b1==1 && b2==1)return false;
	}
	return 1;
}

void out(int bit,int m){
	for (int i=0;i<m;i++)printf("%d",(bit>>i)&1); 
	printf("  ");
}

int main(){
	int tt; scanf("%d",&tt);
	for (int ti=1;ti<=tt;ti++){
		int n,m; scanf("%d%d",&n,&m);
		char s[n+1][m+1];
		int map[n+1];
		for (int i=1;i<=n;i++){
			scanf("%s",s[i]);
			map[i]=0;
			for (int j=0;j<m;j++)map[i]|=(s[i][j]=='.')<<j;
		}

		int M = 1<<m;
		int dp[n+1][M]; memset(dp,0,sizeof(dp));
		map[0]=M-1;

		int ans=0;

		for (int i=0;i<n;i++){
			for (int bit=0;bit<M;bit++){
				if (!check(bit,m))continue;
				if ((bit|map[i])!=map[i])continue;
				bool t[m],t2[m]; 
				memset(t,0,sizeof(t));
				memset(t2,0,sizeof(t2));
				for (int j=0;j<m;j++){
					t[j]=(bit>>j)&1;
				}

				if (t[0])t2[1]=true;
				if (t[m-1] && m>1)t2[m-2]=true;
				for (int j=1;j<m-1;j++){
					if (t[j]){
						t2[j-1]=t2[j+1]=true;
					}
				}

				int valid=0;
				for (int j=0;j<m;j++){
					if (!t2[j])valid|=1<<j;
				}
/*
				out(bit,m);
				out(valid,m);
				puts("");
*/

				for (int bit2=0;bit2<M;bit2++){
					if (!check(bit2,m))continue;
					if ((bit2|map[i+1])!=map[i+1])continue;
					if ((bit2|valid)!=valid)continue;

					int cnt = count(bit2);

					dp[i+1][bit2] = max(dp[i+1][bit2],dp[i][bit]+cnt);

					ans = max(ans,dp[i+1][bit2]);
				}

				if (i==0)break;

			}

/*
			puts("-------------------------------------------------------");
			printf("row %d: ",i); out(map[i],m); puts("");
			for (int bit=0;bit<M;bit++){
				if (dp[i][bit]==0)continue;
				out(bit,m);
				printf(": %d\n",dp[i][bit]);
			}
			*/
		}

/*
		printf("row %d: ",n); out(map[n],m); puts("");
		for (int bit=0;bit<M;bit++){
			out(bit,m);
			printf(": %d\n",dp[n][bit]);
		}
*/
		printf("Case #%d: %d\n",ti,ans);
	}

	return 0;
}
