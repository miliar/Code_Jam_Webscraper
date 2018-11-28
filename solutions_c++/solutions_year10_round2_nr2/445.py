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
double x[100],v[100];
double t2[100];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		int n,k,b;
		double t1;
		scanf("%d%d%d%lf",&n,&k,&b,&t1);
		FOR(i,0,n)
			scanf("%lf",&x[i]);
		FOR(i,0,n)
			scanf("%lf",&v[i]);
		bool f=false;
		int p=0,res=0;
		int c=0;
		for (int i=n-1; i>=0; --i)
		{
			if (v[i]*t1>=b-x[i])
			{
				p++;
				res+=c;
				if (p==k)
				break;
			}
			else
				c++;
		}
		printf("Case #%d: ",it+1);
		if (p==k)
			printf("%d\n",res);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}