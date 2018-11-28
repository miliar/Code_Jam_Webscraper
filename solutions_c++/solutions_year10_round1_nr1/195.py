#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

const int inf = 1000*1000*1000;
#define CL(x,a) memset(x,a,sizeof(x));
#define ALL(v) (v).begin(),(v).end();
typedef long long LL;
int T,n,m,res1,res2,K;
vector< vector<char> > v;
bool bound (int x,int y)
{
	return !(x<0 || x >=n || y < 0 || y >=m);
}
bool free(int x, int y)
{
	if (!bound(x,y))
		return 0;
	return v[x][y] == '.';
}
bool isCh(int x, int y, char ch)
{
	if (!bound(x,y))
		return 0;
	return v[x][y] == ch;
}
void shift()
{
	for(int i=0;i<n;i++)
	{
		for (int j=m-1;j>=0;j--)
		{
			int x=1;
			while(free(i,j+x))
			{
				x++;
			}
			swap(v[i][j],v[i][j+x-1]);
		}
	}
}
int getLen(int x, int y, int dx, int dy)
{
	int t=0;
	int k=1;
	while (bound(x+k*dx,y+k*dy) && isCh(x+k*dx,y+k*dy,v[x][y]))
	{
		k++;
	}
	t+=k-1;
	k=1;
	while (bound(x-k*dx,y-k*dy) && isCh(x-k*dx,y-k*dy,v[x][y]))
	{
		k++;
	}
	t+=k-1;
	return t+1;
}
void solve()
{
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			if (v[i][j] == '.')
				continue;
			int tres = 0;
			tres = max(tres,getLen(i,j,0,1));
			tres = max(tres,getLen(i,j,1,0));
			tres = max(tres,getLen(i,j,1,1));
			tres = max(tres,getLen(i,j,-1,1));
			if (v[i][j] == 'R')
				res1= max(res1,tres);
			else
				res2= max(res2,tres);
		}
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d%d",&n,&K);
		m = n;
		res1 = res2 = 0;
		v.clear();
		v.resize(n,vector<char>(n));
		scanf("\n");
		for (int j=0;j<n;j++)
		{
			for (int k=0;k<m;k++)
			{
				scanf("%c",&v[j][k]);
			}
			if (j< n-1)
				scanf("\n");
		}
		shift();
		solve();
		/*
		for (int j=0;j<n;j++)
		{
			for (int k=0;k<m;k++)
			{
				printf("%c",v[j][k]);
			}
			printf("\n");
		}
		n=n;*/
		printf("Case #%d: ",i+1);
		if (res1 >= K && res2 >= K)
			printf("Both");
		if (res1 < K && res2 < K)
			printf("Neither");
		if (res1 >= K && res2 < K)
			printf("Red");
		if (res1 < K && res2 >= K)
			printf("Blue");
		printf("\n");
	}
	return 0;
}