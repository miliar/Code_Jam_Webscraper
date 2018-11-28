#include <iostream>
#include <algorithm>
#include <vector>
using namespace std ;

struct walkway 
{
	int b, e, w ;
	walkway() { b=e=w=0; }
	walkway(int b, int e, int w) { this->b=b; this->e=e; this->w=w; }
} ;
bool cmp( const walkway &a, const walkway &b ) { return a.w < b.w ; }
bool cmp2( const walkway &a, const walkway &b ) { return a.b < b.b ; }

vector<walkway> a, b ;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int tt, tests ;
	cin >> tt ;
	for ( tests = 1 ; tests <= tt ; ++tests ) 
	{
		int x, s, r, n ; 
		double t ;
		cin >> x >> s >> r >> t >> n ;
		a.clear() ; 
		for ( int i = 0 ; i < n ; ++i ) 
		{
			int b, e, w ;
			cin >> b >> e >> w ;
			walkway ww ;
			ww.b = b; ww.e = e ;  ww.w = w ;
			a.push_back(ww);
		}
		sort( a.begin(), a.end(), cmp2 ) ;
		b.clear() ;
		b.push_back( walkway(0, a.front().b, 0) ) ;
		b.push_back( walkway(a.back().e, x, 0) ) ;
		for ( int i = 0 ; i < int(a.size())-1 ; ++i ) 
			b.push_back( walkway( a[i].e, a[i+1].b, 0 ) ) ;
		for ( int i = 0 ; i < b.size() ; ++i ) 
			a.push_back( b[i] ) ;
		sort( a.begin(), a.end(), cmp ) ;

		double res = 0 ; 
		cout.precision(12);
		for ( int i = 0 ; i < a.size() ; ++i ) 
		{
			double run = min( double(t), double(a[i].e-a[i].b)/(r+a[i].w) ) ;
			t -= run ;
			double rem = double(a[i].e-a[i].b-run*(r+a[i].w))/(a[i].w+s) ;
			res += run + rem;
		}
		cout << "Case #" << tests << ": " << res << endl ;
	}
}