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
int dp[30];
int mod=100003;
int p[30];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	MEMS(dp,-1);
	FOR(it,0,t)
	{
		int n;
		scanf("%d",&n);
		int res=0;
		if (dp[n]!=-1)
			res=dp[n];
		else
		{
			FOR(i,0,(1<<(n-2)))
			{
				p[1]=0;
				int k=0;
				FOR(j,0,n-2)
				{
					p[j+2]=p[j+1];
					if ((i>>j)&1)
						p[j+2]++;
				}
				p[n]=p[n-1]+1;
				int c=n;
				while (1)
				{
					c=p[c];
					if (c==1)
					{
						res++;
						if (res==mod)
							res=0;
						break;
					}
					if (p[c]==p[c-1])
						break;
				}
			}
			dp[n]=res;
		}
		printf("Case #%d: %d\n",it+1,res);
	}
	return 0;
}