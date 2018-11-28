#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 10005 ;
const int M = 100005 ;
typedef __int64 ll ;
int n , m ;
int s, r ;
struct node{
	double len;
	int b, e, w ;
	bool operator < ( const node&a)const{
		return w < a.w;
	}
}way[N] ;

//bool vst[100005] ;

bool cmp( node &a , node&b ){
	return a.b < b.b ;
}

int main()
{
	int t, i, j, k, Q, x , y, cas = 1 ;
	double time, tmp ;

	freopen("D:\\A-large.in","r",stdin ) ;
	freopen("D:\\out.txt","w",stdout ) ;

	scanf("%d",&t ) ;
	while ( t-- )
	{
		scanf("%d %d %d %lf %d", &m, &s, &r, &time, &n ) ;
		//memset( vst, 0, sizeof(vst) ) ;
		for( i = 0 ; i < n ; i++ )
		{
			scanf("%d %d %d", &x, &y, &way[i].w ) ;
			way[i].b = x , way[i].e = y ;
			//for( j = x ; j < y ; j++ ){
			//	vst[j] = 1 ;
			//}
			way[i].len = y-x ;
		}
		sort( way, way+n, cmp ) ;
		x = 0 ;
		y = 0 ;
		for( i = 0 ; i < n ; i++ )
		{
			y += way[i].b-x ;
			x = way[i].e ;
		}
		y += m-x ;
		way[n].len = y ;
		way[n].w = 0 ;
		sort( way, way+n+1 ) ;
		double ans = 0 ;
		for( i = 0 ; i <= n ; i++ )
		{
			if ( time < 1e-9 )
			{
				ans += (double)way[i].len/(way[i].w+s) ;
				continue ;
			}
			tmp  = (double)way[i].len/(way[i].w+r) ;
			if ( tmp <= time )
			{
				time -= tmp ;
				ans += tmp ;
			}
			else
			{
				way[i].len -= (way[i].w+r)*time ;
				ans += time ;
				time = 0 ;
				ans += (double)way[i].len/(way[i].w+s) ;
			}
		}
		printf("Case #%d: %f\n",cas++, ans ) ;
	}
	return 0 ;
}