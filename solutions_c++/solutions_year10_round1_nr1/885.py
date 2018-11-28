#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <set>
#include <list>
#include <queue>
#include <memory.h>
#include <stdio.h>
#include <time.h>
 
using namespace std;
 
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
char a[110][110],b[110][110];
int n,k;
bool dothis1(char a[110][110], char c)
{
	FOR(i,0,n)
		FOR(j,0,n)
			if (a[i][j]==c)
			{
				bool f=true;
				FOR (j1,j+1,j+k)
				{
					if (j1==n)
					{
						f=false;
						break;
					}
					if (a[i][j1]!=c)
					{
						f=false;
						break;
					}
				}
				if (f)
					return f;
				f=true;
				FOR (i1,i+1,i+k)
				{
					if (i1==n)
					{
						f=false;
						break;
					}
					if (a[i1][j]!=c)
					{
						f=false;
						break;
					}
				}
				if (f)
					return f;
				int x=i+1,y=j+1;
				f=true;
				FOR(it,0,k-1)
				{
					if ((x==n) || (y==n))
					{
						f=false;
						break;
					}
					if (a[x][y]!=c)
					{
						f=false;
						break;
					}
					++x;
					++y;
				}
				if (f)
					return f; 
				x=i+1;
				y=j-1;
				f=true;
				FOR(it,0,k-1)
				{
					if ((x==n) || (y<0))
					{
						f=false;
						break;
					}
					if (a[x][y]!=c)
					{
						f=false;
						break;
					}
					++x;
					--y;
				}
				if (f)
					return f;
			}
		return false;
}
void dothis(char a[110][110])
{
	FOR(i,0,n)
		FOR(j,0,n)
			b[j][n-i-1]=a[i][j];
	FOR(j,0,n)
		for (int i=n-2; i>=0; --i)
		{
			if (b[i][j]!='.')
			{
				int p=i+1;
				while ((p<n))
				{
					if (b[p][j]!='.')
						break;
					swap(b[p-1][j],b[p][j]);
					++p;
				}
			}
		}
	bool f1=dothis1(b,'R');
	bool f2=dothis1(b,'B');
	if ((!f1) && (!f2))
		printf("Neither\n");
		if ((f1) && (f2))
			printf("Both\n");
	if ((f1) && (!f2))
		printf("Red\n");
	if ((!f1) && (f2))
		printf("Blue\n");
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		scanf("%d%d",&n,&k);
		FOR(i,0,n)
			scanf("%s",&a[i]);
		printf("Case #%d: ",it+1);
		FOR(i,0,n)
			FOR(j,0,n)
				b[i][j]='.';
		dothis(a);
	}
	return 0;
}