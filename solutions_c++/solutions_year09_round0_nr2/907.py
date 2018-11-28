#include <stdio.h>
#include <map>
#define N 200

using namespace std;

int n,m,a[N][N],b[N][N];

void fillb(int i,int j)
{
	if(b[i][j]!=-1)
		return;
	int x,y;
	int mi=a[i][j];
	if(i)
		if(a[i-1][j]<mi)
		{
			mi=a[i-1][j];
			x=i-1;
			y=j;
		}
	if(j)
		if(a[i][j-1]<mi)
		{
			mi=a[i][j-1];
			x=i;
			y=j-1;
		}
	if(j+1<m)
		if(a[i][j+1]<mi)
		{
			mi=a[i][j+1];
			x=i;
			y=j+1;
		}
	if(i+1<n)
		if(a[i+1][j]<mi)
		{
			mi=a[i+1][j];
			x=i+1;
			y=j;
		}
	if(mi==a[i][j])
	{
		b[i][j]=m*i+j;
		return;
	}
	if(b[x][y]==-1)
		fillb(x,y);
	b[i][j]=b[x][y];
}

map<int,char>mm;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	char c;
	int t=1;
	int i,j;
	while(T--)
	{
		mm.clear();
		c='a';
		scanf("%d%d",&n,&m);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				b[i][j]=-1;
			}
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				fillb(i,j);
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if(mm.find(b[i][j])==mm.end())
					mm[b[i][j]]=c++;
		printf("Case #%d:\n",t);
		t++;
		for(i=0;i<n;i++)
		{
			printf("%c",mm[b[i][0]]);
			for(j=1;j<m;j++)
				printf(" %c",mm[b[i][j]]);
			printf("\n");
		}
	}
	return 0;
}