#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 10086 ;
const int M = 100100 ;
const double EPS = 1e-8;

struct node{
	double len;
	int b, e, w ;
	bool operator < ( const node&a)const{
		return a.w > w;
	}
}way[N] ;

//bool vst[100005] ;

bool cmp( const node &a ,  const node&b ){
	return b.b > a.b ;
}

int main()
{
	
	double time, tmp ;

	//freopen("D:\\A-large.in","r",stdin ) ;
//	freopen("D:\\out.txt","w",stdout ) ;
   int t, cas = 1;
	scanf("%d",&t ) ;
	while ( t-- )
	{
          printf("Case #%d: ",cas++);
          int n , m ;
          int s, r ;
          int k, Q, x , y;
		scanf("%d %d %d %lf %d", &m, &s, &r, &time, &n ) ;
		for(int i = 0 ; i < n ; i++ )
		{
			scanf("%d %d %d", &x, &y, &way[i].w ) ;
			way[i].b = x , way[i].e = y ;
			way[i].len = y-x ;
		}
		sort( way, way+n, cmp ) ;
		x = 0 ;
		y = 0 ;
		for(int i = 0 ; i < n ; i++ )
		{
			y += way[i].b-x ;
			x = way[i].e ;
		}
		y += m-x ;
		way[n].len = y ;
		way[n].w = 0 ;
		sort( way, way+n+1 ) ;
		double ans = 0 ;
		for( int i = 0 ; i <= n ; i++ )
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
		printf("%.7f\n",ans ) ;
	}
	return 0 ;
}
