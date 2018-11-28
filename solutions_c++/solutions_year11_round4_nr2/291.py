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
char b[100][100];
int a[100][100];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(test,1,t+1)
	{
		int n,m,d;
		scanf("%d%d%d",&n,&m,&d);
		FOR(i,0,n)
			scanf("%s",b[i]);
		FOR(i,0,n)
			FOR(j,0,m)
				a[i][j]=b[i][j]-'0';
		int res=0;
		FOR(i,1,n-1)
			FOR(j,1,m-1)
			{
				int sz=1;
				while (1)
				{
					double x=0,y=0;
					if ((i-sz<0) || (j-sz<0) || (i+sz>=n) || (j+sz>=m))
						break;
					FOR(i1,i-sz,i+sz+1)
						FOR(j1,j-sz,j+sz+1)
						{
							if ((ABS(i1-i)==sz) && (ABS(j1-j)==sz))
								continue;
							x+=(i-i1)*(d+a[i1][j1]);
							y+=(j-j1)*(d+a[i1][j1]);
						}
					if ((ABS(x)<1e-7) && (ABS(y)<1e-7))
						res=MAX(res,sz*2+1);
					sz++;
				}
			}
		FOR(i,1,n-1)
			FOR(j,1,m-1)
			{
				int sz=1;
				while (1)
				{
					double x=0,y=0;
					if ((i-sz<0) || (j-sz<0) || (i+sz>=n) || (j+sz>=m))
						break;			
					FOR(i1,i-sz,i+sz+2)
						FOR(j1,j-sz,j+sz+2)
						{
							if ((i1==i-sz) && (j1==j-sz))
								continue;
							if ((i1==i-sz) && (j1==j+sz+1))
								continue;
							if ((i1==i+sz+1) && (j1==j-sz))
								continue;
							if ((i1==i+sz+1) && (j1==j+sz+1))
								continue;
							x+=(i+0.5-i1)*(d+a[i1][j1]);
							y+=(j+0.5-j1)*(d+a[i1][j1]);
						}
					if ((ABS(x)<1e-7) && (ABS(y)<1e-7))
						res=MAX(res,sz*2+2);
					sz++;
				}
			}
		printf("Case #%d: ",test);
		if (res<3)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",res);
	}
	return 0;
}
