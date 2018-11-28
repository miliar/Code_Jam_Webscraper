#include <iostream>
#include <algorithm>
using namespace std ;

#define N 1002
double p[N], f[N];
double fact[N] ;

inline double g( int n, int x ) { return p[n-x]/fact[x]; }

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	fact[0]=1; 
	for ( int i=1 ; i<N ; ++i ) 
		fact[i] = min( fact[i-1]*i, 1e100 ) ;

	p[0]=1; p[1]=0; p[2]=0.5;
	for ( int i=3; i<N ; ++i ) p[i]=p[i-2]/i+p[i-1]*double(i-1)/i ;

	f[0]=0 ;
	f[1]=0 ;
	f[2]=2 ;
	for ( int i=3 ; i<N ; ++i )
	{
		for ( int j=2 ; j<i ; ++j )
			f[i] += f[j] * g(i, i-j) ;
		f[i] += 1 ;
		f[i] /= ( 1 - g(i,0) ) ;
	}

	int t ;
	cin >> t ;
	for ( int tests = 1 ; tests <= t ; ++tests ) 
	{
		int u ;
		cin >> u ;
		int n = 0, a ;
		for ( int i=1;i<=u;++i) 
		{
			cin >> a ;
			if ( a!=i ) ++n ;
		}
		printf("Case #%d: %.6lf\n",tests, f[n]);
	}
}