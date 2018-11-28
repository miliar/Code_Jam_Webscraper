#include<stdio.h>
#include<memory.h>
#include<algorithm>
#define N 111

int T;
int n,cc[N][N],f[N][N],k,ans,dp[1111111],ed[1111111],ccc[1111111];


bool cross(int x,int y){
	for(int i=0;i<k-1;i++)
		if(cc[x][i]<=cc[y][i] && cc[x][i+1]>=cc[y][i+1] ||
		   cc[x][i]>=cc[y][i] && cc[x][i+1]<=cc[y][i+1]) return 1;
	return 0;
}

bool can(int y){
	if(ccc[y]<2) return ccc[y];
	if(ed[y]<2) return 1;
	for(int i=0;i<n;i++)if(y & (1<<i))
		for(int j=i+1;j<n;j++)if(y & (1<<j) && f[i][j]){
			ccc[y]=0;
			return 0;
		}
	ccc[y]=1;
	return 1;
}


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=0;_<T;_++){
		memset(dp,63,sizeof(dp));
		memset(ccc,63,sizeof(ccc));
		memset(cc,0,sizeof(cc));

		scanf("%d%d\n",&n,&k);
		for(int i=0;i<n;i++){
			for(int j=0;j<k;j++) scanf("%d",&cc[i][j]);
			for(int j=0;j<i;j++) f[i][j]=f[j][i]=cross(i,j);
		}
		ed[0]=0;
		for(int i=1;i<(1<<n);i++){
			ed[i]=ed[i & (i-1)]+1;
			dp[i]=ed[i];
			if(can(i)) dp[i]=1;else
			for(int j=i;j;j=(j-1)&i)
				if(i^j && dp[j]<1000000000)
					if(can(i^j))
						dp[i]<?=dp[j]+1;
		}

		printf("Case #%d: %d\n",_+1,dp[(1<<n)-1]);
	}
	return 0;
}
