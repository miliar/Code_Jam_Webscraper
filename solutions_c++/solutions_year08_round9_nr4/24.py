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
char a[40][40];
int shortest[40][40];
int zhan[2000][2];

int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);

	int i,j,l,t,ans,x,y,xx,yy,top,bottom,m,n,z,tmp,b1;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&m,&n);
		for (i=0;i<m;i++)
			scanf("%s",a[i]);
		b1=0;
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				if (((i!=0)||(j!=0))&&(a[i][j]=='T'))
				{
					x=i;y=j;b1=1;
				}
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				shortest[i][j]=2000000000;
		zhan[0][0]=0;
		zhan[0][1]=0;
		shortest[0][0]=0;
		top=0;bottom=1;
		while (top<bottom)
		{
			z=shortest[zhan[top][0]][zhan[top][1]];
			for (i=0;i<4;i++)
			{
				xx=zhan[top][0]+neigh[i][0];
				yy=zhan[top][1]+neigh[i][1];
				if ((xx>=0)&&(xx<m)&&(yy>=0)&&(yy<n)&&(a[xx][yy]!='.')&&(z+1<shortest[xx][yy]))
				{
					shortest[xx][yy]=z+1;
					zhan[bottom][0]=xx;
					zhan[bottom][1]=yy;
					bottom++;
				}
			}
			top++;
		}
		if (b1==1)
		{
			tmp=shortest[x][y];
			zhan[0][0]=x;
			zhan[0][1]=y;
			shortest[x][y]=0;
			top=0;bottom=1;
			while (top<bottom)
			{
				z=shortest[zhan[top][0]][zhan[top][1]];
				for (i=0;i<4;i++)
				{
					xx=zhan[top][0]+neigh[i][0];
					yy=zhan[top][1]+neigh[i][1];
					if ((xx>=0)&&(xx<m)&&(yy>=0)&&(yy<n)&&(a[xx][yy]!='.')&&(z+1<shortest[xx][yy]))
					{
						shortest[xx][yy]=z+1;
						zhan[bottom][0]=xx;
						zhan[bottom][1]=yy;
						bottom++;
					}
				}
				top++;
			}
		}
		ans=0;
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				if (a[i][j]!='.') ans+=shortest[i][j];
		if (b1==1)
		{
			for (i=0;i<=tmp;i++)
			{
				if (i>tmp-i) ans+=i-(tmp-i);
			}
		}
		printf("Case #%d: %d\n",l+1,ans);
	}
	return  0;
}
