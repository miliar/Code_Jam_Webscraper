#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int d[1000002] ;
struct rec
{
	int d ; int n ;
} r[1000002] ;
bool cmp( const rec& a, const rec& b ) { return a.d > b.d ; }

int n, c, L ;
long long time ;

double calc( int n, int p, int L, int mode, long long sum )
{
	sort( r, r+n, cmp ) ;
	//在p之前修建是无效的
	double res = 0 ; 
	for ( int i = 0 ; i < n ; ++i ) 
	{
		if ( r[i].n == p ) 
		{
			if ( mode ) res += (time-sum) + (d[p]-(time-sum)*0.5) ;
			else res += r[i].d * 2 ;
		}
		else if ( r[i].n < p ) res += r[i].d*2 ;
		else {
			if ( L ) res += r[i].d , --L ;
			else res += r[i].d*2 ;
		}
	}
	return res ;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t, tests ;
	cin >> t ;
	for ( tests = 1 ; tests <= t ; ++tests ) 
	{		
		cerr << tests  <<endl ;
		cin >> L >> time >> n >> c ;

		for ( int i = 0 ; i < c ; ++i ) 
		{
			int a ;   cin>>a ;
			for ( int k = i ; k <= n ; k += c )
			{
				d[k] = a ;
				r[k].d = a ;
				r[k].n = k ;
			}
		}
		int p ;
		long long sum = 0 ;
		for ( p = 0 ; p < n ; ++p ) 
		{
			if ( sum + 2*d[p] > time ) break ;
			sum += 2 * d[p] ;
		}
		double res = 1e20 ;
		if ( p < n && L > 0 )
			res = calc( n, p, L-1 , 1, sum ) ;
		res = min( res, calc( n, p, L , 0, sum ) ) ;
		long long r2 = res ;
		cout << "Case #" << tests <<": "<< r2 << endl ;
	}
}