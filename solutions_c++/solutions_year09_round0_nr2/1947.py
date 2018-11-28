#include <iostream>
using namespace std;

int		H[20000],Fa[20000];
char	Color[20000];
int		n,m,Test;
char	Sum;

inline int getfa(int p)
{
	if (Fa[p]==p)	return p;
	Fa[p]=getfa(Fa[p]);
	return Fa[p];
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&Test);
	for (int Case=1;Case<=Test;Case++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
			scanf("%d",&H[(i-1)*m+j]);
		for (int i=1;i<=n;i++)
		for (int j=1;j<=m;j++)
		{
			Fa[(i-1)*m+j]=(i-1)*m+j;
			if (i>1 && H[(i-2)*m+j]<H[Fa[(i-1)*m+j]])		Fa[(i-1)*m+j]=(i-2)*m+j;
			if (j>1 && H[(i-1)*m+(j-1)]<H[Fa[(i-1)*m+j]])	Fa[(i-1)*m+j]=(i-1)*m+(j-1);
			if (j<m && H[(i-1)*m+(j+1)]<H[Fa[(i-1)*m+j]])	Fa[(i-1)*m+j]=(i-1)*m+(j+1);
			if (i<n && H[i*m+j]<H[Fa[(i-1)*m+j]])			Fa[(i-1)*m+j]=i*m+j;
		}
		Sum='a'-1;
		for (int i=1;i<=n*m;i++)	Color[i]=' ';
		for (int i=1;i<=n*m;i++)
			if (Color[getfa(i)]==' ')
				Color[getfa(i)]=++Sum;
		printf("Case #%d:\n",Case);
		for (int i=1;i<=n;i++)
		{
			for (int j=1;j<m;j++)
				printf("%c ",Color[getfa((i-1)*m+j)]);
			printf("%c\n",Color[getfa(i*m)]);
		}
	}
}
