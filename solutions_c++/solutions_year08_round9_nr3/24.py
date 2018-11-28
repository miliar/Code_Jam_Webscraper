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

int m,n,best;
int d[10][10];
int a[10][10];
int neigh[9][2]={{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1},{-1,0},{-1,1},{0,0}};

int check(int x,int y)
{
	int xx,yy,tot,i;
	tot=0;
	for (i=0;i<9;i++)
	{
		xx=x+neigh[i][0];
		yy=y+neigh[i][1];
		if ((xx>=0)&&(xx<m)&&(yy>=0)&&(yy<n))
			tot+=d[xx][yy];
	}
	if (tot!=a[x][y]) return 0;
	else return 1;
}

void search(int x,int y)
{
	int i,tmp,b1;
	if (x==m)
	{
		b1=1;
		for (i=0;i<n;i++)
			if (check(m-1,i)==0) b1=0;
		if (b1==1)
		{
			tmp=0;
			for (i=0;i<n;i++)
				tmp+=d[m/2][i];
			if (tmp>best) best=tmp;
		}
		return;
	}
	if (y==n)
	{
		if ((x==0)||(check(x-1,n-1)==1))
			search(x+1,0);
		return;
	}
	for (i=0;i<2;i++)
	{
		d[x][y]=i;
		if ((x==0)||(y==0)||(check(x-1,y-1)==1))
		{
			search(x,y+1);
		}
		d[x][y]=0;
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int i,j,l,t;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&m,&n);
		for (i=0;i<m;i++)
			for (j=0;j<n;j++)
				scanf("%d",&a[i][j]);
		best=0;
		search(0,0);
		printf("Case #%d: %d\n",l+1,best);
	}
	return  0;
}
