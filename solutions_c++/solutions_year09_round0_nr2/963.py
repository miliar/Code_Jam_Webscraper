#include <cstdio>
#include <memory>

#define REP(i,n) for(i=0;i<n;i++)
#define FOR(i,a,b) for(i=a;i<=b;i++)

#define N 105
#define K 4
#define inf 1000000000
int moves[K][2]={{-1,0},{0,-1},{0,1},{1,0}};

int a[N][N];
char ans[N][N];
int n,m,i,j,t,test;
bool used[N][N];
int numbas;

char dfs(int i,int j)
{
	if(!used[i][j]){
		used[i][j]=1;
		int k=0,l=-1;
		REP(k,K)
			if((l==-1 && a[i+moves[k][0]][j+moves[k][1]]<a[i][j])||(a[i+moves[k][0]][j+moves[k][1]]<a[i+moves[l][0]][j+moves[l][1]]))
				l=k;
		if(l==-1){
			ans[i][j]='a'+numbas;
			numbas++;
		}else
		{
			ans[i][j]=dfs(i+moves[l][0],j+moves[l][1]);
		}
	}
	return ans[i][j];
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&test);
	FOR(t,1,test){
		scanf("%d%d",&n,&m);
		FOR(i,1,n)
			FOR(j,1,m)
				scanf("%d",&a[i][j]);
		FOR(i,0,n+1){
			a[i][0]=inf;
			a[i][m+1]=inf;
		}
		FOR(i,0,m+1){
			a[0][i]=inf;
			a[n+1][i]=inf;
		}
		numbas=0;
		memset(used,0,sizeof(used));
		FOR(i,1,n)
			FOR(j,1,m)		
				if(!used[i][j])
					dfs(i,j);
		printf("Case #%d:\n",t);
		FOR(i,1,n){
			FOR(j,1,m-1)	
				printf("%c ",ans[i][j]);
			printf("%c\n",ans[i][m]);
		}
	}
	return 0;
}
