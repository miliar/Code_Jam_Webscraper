#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int neigh[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int used[20][20];
int d[20][20];
char a[20][20];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int i,j,k,l,t,m,n,sx,sy,ex,ey,min,bi,bj,z,x,y,best;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&m,&n);
		for (i=0;i<m;i++)
			scanf("%s",a[i]);
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
			{
				if (a[i][j]=='O')
				{
					sx=i;sy=j;
				}
				if (a[i][j]=='X')
				{
					ex=i;ey=j;
				}
			}
		memset(used,0,sizeof(used));
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				d[i][j]=2000000000;
		d[sx][sy]=0;
		while (1)
		{
			min=2000000000;
			for (i=0;i<m;i++)
				for (j=0;j<n;j++)
					if ((used[i][j]==0)&&(d[i][j]<min))
					{
						bi=i;bj=j;
						min=d[i][j];
					}
			if (min==2000000000) break;
			used[bi][bj]=1;
			z=d[bi][bj];
			for (i=0;i<4;i++)
			{
				x=bi+neigh[i][0];
				y=bj+neigh[i][1];
				if ((x>=0)&&(x<m)&&(y>=0)&&(y<n)&&(a[x][y]!='#')&&(used[x][y]==0)&&(z+1<d[x][y]))
				{
					d[x][y]=z+1;
				}
			}
			best=bi+1;
			if (bj+1<best) best=bj+1;
			if (m-bi<best) best=m-bi;
			if (n-bj<best) best=n-bj;
			for (i=0;i<m;i++)
				for (j=0;j<n;j++)
					if ((a[i][j]=='#')&&(abs(i-bi)+abs(j-bj)<best))
						best=abs(i-bi)+abs(j-bj);
			for (i=0;i<4;i++)
			{
				x=bi;
				y=bj;
				while ((x>=0)&&(x<m)&&(y>=0)&&(y<n)&&(a[x][y]!='#'))
				{
					x+=neigh[i][0];
					y+=neigh[i][1];
				}
				x-=neigh[i][0];
				y-=neigh[i][1];
				if (z+best<d[x][y])
				{
					d[x][y]=z+best;
				}
			}
		}
		if (d[ex][ey]==2000000000)
		{
			printf("Case #%d: THE CAKE IS A LIE\n",l+1);
		}
		else
		{
			printf("Case #%d: %d\n",l+1,d[ex][ey]);
		}
	}
	return 0;
}

