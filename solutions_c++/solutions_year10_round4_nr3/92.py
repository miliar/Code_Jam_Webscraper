#include <iostream>
using namespace std;

bool a[101][101];
bool b[101][101];
bool ok;
int i,j,k,m,n,t,c,x,y,p,q,ii,jj,ans;

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	for (c=1; c<=t; c++)
	{
		memset(a,false,sizeof(a));
		scanf("%d",&m);
		for (i=1; i<=m; i++)
		{
			scanf("%d%d%d%d",&x,&y,&p,&q);
			for (ii=min(x,p); ii<=max(x,p); ii++)
				for (jj=min(y,q); jj<=max(y,q); jj++)
					a[ii][jj]=true;
		}
		int ans=0;
		while (1)
		{
			ok=true;
			for (i=1; i<=100; i++)
			{
				for (j=1; j<=100; j++)
					if (a[i][j]) {ok=false; break;}
				if (!ok) break;
			}
			if (ok) break;
			memcpy(b,a,sizeof(b));
			
			for (i=1; i<=100; i++)
				for (j=1; j<=100; j++)
				{
					if (a[i-1][j] && a[i][j-1]) b[i][j]=true;
					if (!a[i-1][j] && !a[i][j-1]) b[i][j]=false;
				}
			memcpy(a,b,sizeof(a));
			ans++;
		}
		printf("Case #%d: %d\n",c,ans);
	}
	
//	system("pause");
	return 0;
}
