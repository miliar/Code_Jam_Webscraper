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
int a[1000][1000];
int b[1000][1000];
int main()
{	
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		int r;
		MEMS(a,0);
		scanf("%d",&r);
		int p=0;
		FOR(c,0,r)
		{
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			FOR(i,y1,y2+1)
				FOR(j,x1,x2+1)
				{
					a[490+i][490+j]=1;
				}
		}
	
		int res=0;
		FOR(i,0,1000)
			FOR(j,0,1000)
				b[i][j]=a[i][j];
		while (1)
		{
			FOR(i,1,1000)
				FOR(j,1,1000)
				{
					if (b[i][j]==0)
					{
						if ((b[i-1][j]==1) && (b[i][j-1]==1))
							a[i][j]=1;
					}
					if (b[i][j]==1)
					{
						if ((b[i-1][j]==0) && (b[i][j-1]==0))
							a[i][j]=0;
					}
				}
			int k=0;
			FOR(i,0,1000)
				FOR(j,0,1000)
				{
					if (a[i][j]==1)
						k++;
					b[i][j]=a[i][j];
				}
			++res;
			if (k==0)
				break;
		}
		printf("Case #%d: %d\n",it+1,res);
	}
	return 0;
}