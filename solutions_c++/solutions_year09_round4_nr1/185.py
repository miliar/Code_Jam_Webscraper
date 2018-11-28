#include <stdio.h>
#include <memory.h>
const int maxn = 200;
int cases,T,i,j,k,n,ans;
char map[maxn][maxn];
bool bol[maxn];
bool able(int i,int j)
{
	int k;
	for (k=n;k>j;k--)
		if (map[i][k]=='1') return false;
	return true;
}
void change(int x)
{
	int i;
	char k;
	for (i=1;i<=n;i++)
	{
		k=map[x-1][i];
		map[x-1][i]=map[x][i];
		map[x][i]=k;
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cases);
	for (T=1;T<=cases;T++)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
			{
				scanf("%c",&map[i][j]);
				while (map[i][j]!='1'&&map[i][j]!='0') scanf("%c",&map[i][j]);
			}
		ans = 0;
		for (i=1;i<=n;i++)
		{
			for (j=i;j<=n;j++)
				if (able(j,i)) break;
			if (j>i)
			{
				for (k=j;k>i;k--)
				{
					ans++;
					change(k);
				}
			}
		}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}