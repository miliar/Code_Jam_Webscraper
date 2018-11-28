#include <stdio.h>
#include <string.h>

#define MN 110

char g[MN][MN];
int mat[MN];
char u[MN];

int N,K;
int c[MN][MN];

int dfs(int t){
	int i;
	for (i=0;i<N;i++){
		if (u[i]==0 && g[t][i]){
			u[i]=1;
			if (mat[i]==-1 || dfs(mat[i])){
				mat[i]=t;
				return 1;
			}
		}
	}
	return 0;
}

int solve(){
	int i,j,k;
	int ret=0;
	for (i=0;i<N;i++) for (j=0;j<K;j++)
		scanf("%d",&c[i][j]);
	memset(g,0,sizeof(g));
	memset(mat,-1,sizeof(mat));
	for (i=0;i<N;i++) for (j=0;j<N;j++){
		for (k=0;k<K;k++) if (c[i][k]<=c[j][k]) break;
		if (k==K) g[i][j]=1;
	}
	for (i=0;i<N;i++){
		memset(u,0,sizeof(u));
		ret+=dfs(i);
	}
	return ret;
}

int main(){
	int T,cas;
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++){
		scanf("%d%d",&N,&K);
		printf("Case #%d: %d\n",cas,N-solve());
	}
	return 0;
}

