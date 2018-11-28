#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int vals[111];
int d,i,m,n;

int dp[111][260][2];
int OO = (1<<25);

int calc( int ind, int last , bool frst)
{
	if ( ind == n )
		return 0;
	int &r = dp[ind][last][frst];
	if ( r != -1 )
		return r;

	int r1 = OO,r2= OO, r31 = OO, r32 = OO,r41 = OO,r42 = OO;
	//leave
	if ( frst || abs(vals[ind]-last) <= m)
		r1 = calc(ind+1,vals[ind],0);

	//delete
		r2 = calc (ind+1,last,frst) + d;

	//insert
	if ( !frst && m && abs(vals[ind]-last) > m )
		if ( vals[ind] > last )
			r31 = calc(ind,min(last+m,255),0) + i;
		else
			r32 = calc(ind,max(last-m,0  ),0) + i;


	//change
	if ( frst )
	{
		for ( int j = 0 ; j < 256 ; j ++ )
		{
			r31 = calc(ind+1,j,0) + abs(j-vals[ind]);
			r32 = min (r32,r31) ;
		}
	}
	else
	{
		int fedg = max(last-m,0);
		int sedg = min(last+m,255);

		int dif1 = abs(vals[ind] - fedg);
		int dif2 = abs(vals[ind] - sedg);

		r41 = calc(ind+1,fedg,0) + dif1;
		r42 = calc(ind+1,sedg,0) + dif2;

	}
	return r = min (r1,min(r2,min(r31,min(r32,min(r41,r42)))));
}

int main()
{
	freopen("B-small-attempt4.in","rt",stdin);
	freopen("B-small-attempt4.out","wt",stdout);
	int tt;
	scanf("%d",&tt);
	for ( int t = 1; t<=tt ; t++)
	{
		scanf("%d %d %d %d", &d,&i,&m,&n);
		for ( int j = 0 ; j <n ; j ++ )
			scanf("%d", &vals[j]);
		memset(dp,-1,sizeof(dp));
		int res = calc (0,0,1);
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
