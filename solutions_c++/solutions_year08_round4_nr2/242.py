#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
using namespace std;
typedef unsigned U;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;

inline LL cp(LL x1, LL y1, LL x2, LL y2)
{
	return (x1*y2-x2*y1);
}

inline LL mod(LL x)
{
	if (x<0) return -x;
	return x;
}



void single_case(int cas)
{
	LL n,m,a;
	scanf("%lld %lld %lld",&n,&m,&a);
	
	for (LL x1=0; x1<=n; x1++)
	for (LL x2=x1; x2<=n; x2++)
	for (LL y1=0; y1<=m; y1++)
	for (LL y2=0; y2<=m; y2++)
		if (mod(cp(x1,y1,x2,y2))==a)
		{
			printf("Case #%d: 0 0 %lld %lld %lld %lld\n",cas,x1,y1,x2,y2);
			return;
		}
	
	
	printf("Case #%d: IMPOSSIBLE\n",cas);
}


int main()
{
	int j;
	scanf("%d",&j);
	for (int i=0; i<j; i++)
		single_case(i+1);
	return 0;
}

