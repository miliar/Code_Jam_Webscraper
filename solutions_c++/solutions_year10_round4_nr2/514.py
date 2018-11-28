#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

#define INF 0x3f3f3f3f

int v[2048];

int opt[15][2048];

void dfs(int i, int lv,int P){
	int u;
	if (lv==P) return;
	dfs(i+i,lv+1,P);
	dfs(i+i+1,lv+1,P);
	for (u=0;u<14;u++){
		opt[u][i]=min(opt[u][i+i]+opt[u][i+i+1]+v[i],opt[u][i]);
		if (u) opt[u-1][i]=min(opt[u][i+i]+opt[u][i+i+1],opt[u-1][i]);
	}
}

void sol(int cas){
	int i,j,k,p,c,K;
	int ret;
	scanf("%d",&p);
	for (i=p;i>=0;i--){
		k=1<<i;
		for (j=0;j<k;j++) scanf("%d",&v[k+j]);
	}
	
	memset(opt,0x3f,sizeof(opt));
	K=1<<p;
	for (i=0;i<K;i++){
		if (v[i+K]>14) v[i+K]=14;
		for (j=0;j<=v[i+K];j++) opt[j][i+K]=0;
	}
	
	dfs(1,0,p);
	ret = opt[0][1];
	printf("Case #%d: %d\n",cas,ret);
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		sol(cas);
	return 0;
}

