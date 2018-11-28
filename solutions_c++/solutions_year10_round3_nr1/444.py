#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std ;
struct pp
{
	int x , y ;
};
pp used[2000] ;
int n ;
bool cmp( pp a , pp b )
{
	return a.x < b.x ;
}
int main()
{
	int cas ;
	int cass = 1 ;
	freopen("A-large1.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	while ( cas -- )
	{
		scanf("%d",&n) ;
		for ( int i = 0 ; i < n ; i ++ )
		{
			scanf("%d %d",&used[i].x,&used[i].y) ;
		}
		sort(used,used+n,cmp) ;
		int ans = 0;
		for ( int i = 0 ; i < n ; i ++ )
		{
			for ( int j = i+1 ; j < n ; j ++ )
			{
				if ( used[i].y > used[j].y )
					ans++ ;
			}
		}
		printf("Case #%d: %d\n",cass++,ans);
	}
	return 0 ;
}