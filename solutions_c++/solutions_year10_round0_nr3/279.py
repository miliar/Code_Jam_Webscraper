#include<iostream>
#include<cstdio>
#include<map>

using namespace std;

int main()
{
	int T ;
	freopen ( "tpl.in","r",stdin);
	freopen( "tpl.out","w",stdout);
	scanf ( "%d", &T ) ;
	for ( int kase = 1 ; kase <=T ; kase ++ ) 
	{
		printf( "Case #%d: ", kase ) ;
		long long R , k ,N  ; 
		scanf ( "%lld%lld%lld", &R ,&k, &N );
		long long A [ 2 * N + 1  ]  ; 
		for ( long long i = 0 ; i  < N ; i ++ ) 
		   scanf ( "%lld" , & A [ i ]  ) ;
		for ( long long i = N ; i <2 * N - 1 ; i ++ ) 
		   A [ i ] = A [ i -N ] ; 
		long long maxim [ N ] ; 
		long long end [ N ] ; 
		for ( long long i = 0 ; i < N ; i ++ ) 
		{
			long long now = i ; 
			long long cost = 0 ;
			while ( now - i < N  &&  cost +  A [ now ] <= k ) 
			{
			   cost = cost + A [ now ] ; 
			   now ++ ;
			}
			maxim [ i ] = cost ; 
			end [ i ] = now % N ; 
		}
		map < long long , long long > dp,turns ; 
		dp .clear () ;
		int now = 0 ;
		long long i ; 
		long long earn = 0 ;
		for ( i = 1 ; i <= R ; i ++ )
		{
			if (dp.count ( now ) != 0 )  break; 
			dp [ now ] = earn ;
			turns [ now ] = i ;
			earn = earn + maxim [ now ] ; 
			now = end [ now ] ; 
		}
		
		long long period = i - turns [ now ] ; 
		R = R - turns [ now ] + 1 ;
		long long totaltimes = R / period  ; 
		long long remtimes = R - totaltimes * period  ; 
		earn = dp [ now ] + ( earn - dp [ now ] ) * totaltimes; 
		for ( long long i = 0 ; i < remtimes; i ++ ) 
		{
			earn = earn + maxim [ now ] ; 
			now = end [ now ] ; 
		}
		printf( "%lld\n", earn);
	}
}

