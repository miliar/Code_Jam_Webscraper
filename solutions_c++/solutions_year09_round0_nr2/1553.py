#include <stdio.h>
#include <string>
#include <set>
using namespace std;

int T,n,m;
int a[100][100];
char b[100][100];
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
char count;

char rec(int x,int y)
{
	if(b[x][y]!='0')
		return b[x][y];
	int mn=a[x][y];
	int nxx,nyy;
	for(int i=0;i<4;i++)
	{
		int tx=x+dx[i];
		int ty=y+dy[i];
		if((tx>=0)&&(tx<n)&&(ty>=0)&&(ty<m)&&(mn>a[tx][ty]))
		{
			nxx=tx;
			nyy=ty;
			mn=a[tx][ty];
		}
	}
	if(mn==a[x][y])
		b[x][y]=count++;
	else
		b[x][y]=rec(nxx,nyy);
	return b[x][y];
}

void death()
{
	freopen("input.txt","w",stdout);
	printf("1\n100 100\n");
	for(int i=0;i<100;i++)
	{
		if((i&1)==0)
			for(int j=0;j<100;j++)
				printf("%d ",i*100+j);
		else
			for(int j=99;j>=0;j--)
				printf("%d ",i*100+j);
		printf("\n");
	}
	fclose(stdout);
}

int main()
{
	//death();
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{
		count='a';
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				b[i][j]='0';
			}
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				rec(i,j);
		printf("Case #%d:\n",t+1);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				printf("%c ",b[i][j]);
			printf("\n");
		}
	}
	//
	return 0;
}