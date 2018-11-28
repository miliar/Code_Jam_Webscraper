#include <string.h>
#include <stdio.h>

const int maxn=1<<12;
const int inf=1000000000;
int P,N,T;
int M[maxn];
int price[maxn];
int g[maxn][12];

int min(int a,int b){return a<b?a:b;}
int max(int a,int b){return a>b?a:b;}

void input()
{
	int i,j,k;
	scanf("%d",&P);
	for(i=0;i<(1<<P);i++){
		scanf("%d",&M[i]);
	}
	for(i=1;i<=P;i++){
		k=(1<<(P-i));
		for(j=0;j<k;j++){
			scanf("%d",&price[k+j]);
		}
	}
}

int solve()
{
	int i,j,k;
	memset(g,0,sizeof(g));
	for(i=(1<<P);i<(1<<(P+1));i++){
		for(j=0;j<=M[i-(1<<P)];j++) g[i][j]=0;
		for(;j<=P;j++) g[i][j]=inf;
	}
	for(i=(1<<P)-1;i>0;i--){
		g[i][0]=min(g[i+i][0]+g[i+i+1][0]+price[i], inf);
		for(j=0;j<P;j++){
			g[i][j]=min(inf, min(g[i+i][j]+g[i+i+1][j]+price[i], g[i+i][j+1]+g[i+i+1][j+1]));
		}
		for(j=1;j<=P;j++){
			//g[i][j]=min(g[i][j],g[i][j-1]);
		}
		for(j=P-1;j>=0;j--){
			//g[i][j]=min(g[i][j], g[i][j+1]);
		}
	}
	return g[1][0];
}


int main()
{
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		input();
		printf("Case #%d: ",i);
		printf("%d\n",solve());
	}
	return 0;
}