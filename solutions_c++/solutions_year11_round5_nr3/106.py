#include <iostream>
#include <set>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <math.h>
#include <cstdlib>
#include <memory.h>
#include <sstream>
#include <assert.h>

using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)>(0)?(a):(-(a)))
#define mp make_pair
#define pnt pair<int,int>
#define MEMS(a,b) memset((a),(b),sizeof(a))
#define pb push_back
#define LL long long
#define U unsigned
char a[10][10];
int was[5][5];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,1,t+1)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		FOR(i,0,n)
			scanf("%s",&a[i]);
		int p=n*m;
		int step=(1<<p);
		int res=0;
		FOR(it,0,step)
		{
			MEMS(was,-1);
			bool f=true;
			int cnt=-1;
			FOR(i,0,n)
				FOR(j,0,m)
					if (was[i][j]==-1)
					{
						cnt++;
						int x=i,y=j;
						while (1)
						{
							if (was[x][y]!=-1)
							{
								if ((x!=i) || (y!=j))
								{
									f=false;
								}
								break;
							}
							was[x][y]=cnt;
							int bit=x*m+y;
							if (a[x][y]=='|')
							{
								if ((it>>bit)&1)
									x--;
								else
									x++;
							}
							else
							if (a[x][y]=='-')
							{
								if ((it>>bit)&1)
									y++;
								else
									y--;
							}
							else
							if (a[x][y]=='/')
							{
								if ((it>>bit)&1)
								{
									x--;
									y++;
								}
								else
								{
									x++;
									y--;
								}
							}
							else
							{
								if ((it>>bit)&1)
								{
									x--;
									y--;
								}
								else
								{
									x++;
									y++;
								}
							}
							if (x<0)
								x=n-1;
							if (x>n-1)
								x=0;
							if (y<0)
								y=m-1;
							if (y>m-1)
								y=0;
						}
					}
			res+=f;
		}
		printf("Case #%d: %d\n",test,res);
	}
	return 0;
}