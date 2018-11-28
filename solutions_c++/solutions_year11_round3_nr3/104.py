#include <iostream>
#include <algorithm>
using namespace std ;

bool harmony( long long a, long long b ) 
{
	return ( a%b==0 || b%a == 0 ) ;
}


int a[100000];
int n,l,h;

bool harmony( int i )
{
	for ( int j=0 ; j<n ; ++j ) if ( !harmony(a[j],i) ) return false ;
	return true ;
}


int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int t,tests ;
	cin>>t;
	for ( tests=1;tests<=t;++tests)
	{
		cin>>n>>l>>h;
		int i ;
		for ( i=0 ; i<n ; ++i ) cin>>a[i] ;
		for ( i=l ; i<=h ; ++i ) 
			if ( harmony(i) ) break ;
		cout << "Case #"<<tests<<": " ;
		if ( i>h ) cout << "NO" << endl ;
		else cout << i << endl ;
	}
}