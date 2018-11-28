#include<stdio.h>
#include<memory.h>

int n,m;
char c[100][100];
int a[100][100];
int f[100][100];
int left[100][100];

int ans;

int dx[]={-1,0,-1};
int dy[]={-1,-1,1};

void dfs(int i,int j,int num)
{
	if(num+left[i][j]<=ans) return;

	for(a[i][j]=1;a[i][j]>=0;a[i][j]--)
	{		
		if(a[i][j])
		{
			if(c[i][j]=='x') continue;
			if(f[i][j]) continue;
			int dir;
			for(dir=0;dir<=2;dir++)
			{
				int xx=i+dx[dir];
				int yy=j+dy[dir];

				if(xx<=0 || xx>=n+1 || yy<=0 || yy>=m+1) continue;
				if(a[xx][yy]) break;				
			}
			if(dir!=3) continue;
		}
		

		int ii=i,jj=j;
		jj++;
		if(jj==m+1)
		{
			ii++;
			jj=1;
		}
		int tnum=num+a[i][j];
		if(ii==n+1)
		{
			if(tnum>ans) 
			{
				ans=tnum;
			}
		}
		else
		{
			dfs(ii,jj,tnum);
		}
	}
}

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("C-small-attempt2.out","w",stdout);
	
	int i,j;
	int T,T1;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d",&n,&m);

		for(i=1;i<=n;i++)
		{
			scanf("%s",&c[i][1]);
		}

		int top=0;
		for(i=n;i>=1;i--)
		{
			for(j=m;j>=1;j--)
			{
				if((j-m)%2==0) left[i][j]=++top;
				else left[i][j]=top;
			}
		}

		

		ans=0;
		memset(a,0,sizeof(a));
		memset(f,0,sizeof(f));
		dfs(1,1,0);

		printf("Case #%d: %d\n",T1,ans);
	}
	return 0;
}