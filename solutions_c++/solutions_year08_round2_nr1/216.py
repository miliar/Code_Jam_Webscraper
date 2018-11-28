#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

struct Point
{
	int x , y ;
};
Point point[100006];
int main(void)
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int cases ;
	scanf("%d",&cases);
	int f = 0;
	while( cases -- )
	{
		long long A, B, C, D, x0, y0, M ,i,j,k,n;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&A,&B,&C,&D,&x0,&y0,&M);
		point[0].x = x0 ;
		point[0].y = y0;
		for( i = 1 ; i < n ; i ++)
		{
			point[i].x = (A * point[i-1].x + B) % M ;
			point[i].y = (C * point[i-1].y + D) % M;
		}
		int ans = 0;
		for( i = 0 ; i < n ; i ++)
		{
			for(j = i + 1 ; j < n ; j ++)
			{
				for(k = j + 1 ; k < n ; k ++)
				{
					if( (point[i].x + point[j].x +point[k].x ) % 3 == 0
						&& ( point[i].y + point[j].y +point[k].y ) % 3 == 0)
						ans ++;
				}
			}
		}
		printf("Case #%d: %d\n",++f,ans);
	}
	return 0;
}
