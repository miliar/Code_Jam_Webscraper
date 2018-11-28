#include<stdio.h>
#include<memory.h>
#include<algorithm>

using namespace std;


int fmin(int a,int b)
{
	if(a<b) return a;
	else return b;
}

int fmax(int a,int b)
{
	if(a>b) return a;
	else return b;
}

int MOD=10007;
int n,m,k;
int f[101][101];
int a[101][101];

int dx[]={1,2};
int dy[]={2,1};

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	
	int i,j;
	int T,T1;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d%d",&n,&m,&k);
		
		memset(a,0,sizeof(a));
		for(i=1;i<=k;i++)
		{
			int r,c;
			scanf("%d%d",&r,&c);
			a[r][c]=1;
		}

		memset(f,0,sizeof(f));
		f[1][1]=1;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
			{
				if(a[i][j]) continue;

				int dir;
				for(dir=0;dir<=1;dir++)
				{
					int x=i+dx[dir];
					int y=j+dy[dir];
					if(x>=n+1 || y>=m+1) continue;
					
					if(!a[x][y]) f[x][y]=(f[x][y]+f[i][j])%MOD;
				}
			}
		}

		int ans=f[n][m];
		printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}