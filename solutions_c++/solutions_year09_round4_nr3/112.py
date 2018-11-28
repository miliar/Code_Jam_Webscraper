#include<stdio.h>
#include<string.h>

int n,m;
int ntest;
int a[200][50];
int g[200][200];
int b[200],lk[200];

bool find(int x)
{
	if(b[x]) return false;
	b[x] = true;
	for(int i=0;i<n;i++)
		if(g[x][i])
		{
			if(lk[i]==-1 || find(lk[i]))
			{
				lk[i] = x;
				return true;
			}
		}
	return false;
}

int main()
{
	scanf("%d",&ntest);
	for(int test=1;test<=ntest;test++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		for(int x=0;x<n;x++)
			for(int y=0;y<n;y++)
			{
				bool ok = true;
				for(int p=0;p<m;p++)
					if(a[x][p] >= a[y][p]) ok = false;
				g[x][y] = ok;
			}
		int ans = n;
		memset(lk,-1,sizeof(lk));
		for(int i=0;i<n;i++)
		{
			memset(b,0,sizeof(b));
			if(find(i)) ans--;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	return 0;
}

