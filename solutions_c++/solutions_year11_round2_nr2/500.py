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
pnt a[1000010];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(itt,0,test)
	{
		int c,d;
		scanf("%d%d",&c,&d);
		LL sum1=0,sum2=0;
		FOR(i,0,c)
		{
			scanf("%d%d",&a[i].first,&a[i].second);
		}
		sort(a,a+c);
		double l=0,r=1e40;
		double last;
		FOR(it,0,200)
		{
			double m=(l+r)/2.0;
			bool f=true;
			FOR(i,0,c)
			{
				int v=a[i].second;
				if (i==0)
				{
					v--;
					last=a[i].first-m;
				}
				FOR(j,0,v)
				{
					if (a[i].first+m<last+d)
					{
						f=false;
					}
					else
						last=MAX(last+d,a[i].first-m);
				}
			}
			if (f)
				r=m;
			else
				l=m;
		}
		double res=(l+r)/2.0;
		printf("Case #%d: %.10lf\n",itt+1,res);
	}
	return 0;
}