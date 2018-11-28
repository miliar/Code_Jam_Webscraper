#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
const int N = 510 ;
const int M = 100005 ;
typedef __int64 ll ;
int n , m ;
const double eps = 1e-8;
int prime[M], flag ;
int cnt[M] ;
bool vst[M] ;

void init()
{
	flag = 0 ;
	int i, j ;

	for( i = 2 ; i < M ; ++i )
	{
		if ( vst[i] == 1 ) continue ; 
		prime[flag++] = i ;
		for( j = i*2 ; j < M ; j += i ) 
		{
			vst[j] = 1 ;
		}
	}
}

int main()
{
	int t, i, j, k, Q, x , y, cas = 1 ;
	ll n, ans1, ans2 ;

	freopen("D:\\C-small-attempt0.in","r",stdin ) ;
	freopen("D:\\out.txt","w",stdout ) ;

	init() ;
	scanf("%d",&t ) ;
	while ( t-- )
	{
		cin >> n ;
		printf("Case #%d: ",cas++ ) ;
		if ( n == 1 ){
			puts("0") ;
			continue ;
		}
		memset( cnt , 0, sizeof(cnt) ) ;
		ans2 = 0 ;
		ans1 = 1 ;
		for( i = 1 ; i <= n ; ++i )
		{
			for( j = 0 ; prime[j] <= i ; j++ )
			{
				if ( i%prime[j] ) continue ;
				x = 0 ;
				k = i ;
				while( k%prime[j] == 0 )
				{
					x++ ;
					k /= prime[j] ;
				}
				if ( x > cnt[j] ) cnt[j] = x, ans1++ ;
			}
		}
		for( i = 0 ; prime[i] <= n ; ++i )
		{
			if ( cnt[i] > 0 ) ans2++ ;
		}
		cout << ans1-ans2 << endl ;
	}
	return 0 ;
}