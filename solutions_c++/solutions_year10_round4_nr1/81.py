#include <iostream>
#include <cmath>
using namespace std;

int i,j,k,m,n,t,c,x,y;
int a[200][200];
int p[200][200];
bool h[200],l[200];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for (c=1; c<=t; c++)
	{
		scanf("%d",&n);
		memset(a,-1,sizeof(a));
		for (i=1; i<=n; i++)
		{
			k=n-i+1;
			for (j=k,x=1; x<=i; x++,j+=2)
				scanf("%d",&a[i][j]);
		}
		for (i=n+1; i<=n*2-1; i++)
		{
			k=i-n+1;
			for (j=k,x=1; x<=n*2-i; x++,j+=2)
				scanf("%d",&a[i][j]);
		}
		
		k=n*2-1;
		
		memset(h,false,sizeof(h));
		for (i=1; i<=k; i++)
		{
			memset(p,-1,sizeof(p));
			h[i]=true;
			for (x=1; x<=k; x++)
			{
				for (y=1; y<=k; y++)
				{
					if (a[x][y]==-1) continue;
					if (p[abs(x-i)][y]==-1) p[abs(x-i)][y]=a[x][y];
					if (p[abs(x-i)][y]!=a[x][y]) {h[i]=false; break;}
				}
				if (!h[i]) break;
			}
		}
			
		memset(l,false,sizeof(l));
		for (j=1; j<=k; j++)
		{
			memset(p,-1,sizeof(p));
			l[j]=true;
			for (x=1; x<=k; x++)
			{
				for (y=1; y<=k; y++)
				{
					if (a[x][y]==-1) continue;
					if (p[x][abs(y-j)]==-1) p[x][abs(y-j)]=a[x][y];
					if (p[x][abs(y-j)]!=a[x][y]) {l[j]=false; break;}
				}
				if (!l[j]) break;
			}
		}
		
		int ans=11111111LL;
		int tmp=n*n;
		for (i=1; i<=k; i++)
			if (h[i])
			{
				for (j=1; j<=k; j++)
					if (l[j])
					{
						x=abs(i-n)+abs(j-n)+n;
						ans=min(ans,x*x-tmp);
					}
			}
		
		printf("Case #%d: %d\n",c,ans);
		
	}
	
//	system("pause");
	return 0;
}
