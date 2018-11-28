#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	freopen("C-large.in","r",stdin) ;
	freopen("C-large.out","w",stdout);
	int t ;
	cin >> t ;
	for ( int tests = 1 ; tests <= t ; ++tests )
	{
		int n ; 
		cin >> n ;
		int a[1002] ;
		int sum=0, sum2=0;
		for ( int i=0;i<n;++i ) 
		{
			cin >> a[i] ;
			sum = sum^a[i] ;
			sum2 += a[i] ;
		}
		if ( sum ) printf("Case #%d: NO\n",tests);
		else 
		{
			sort( a, a+n ) ;
			printf("Case #%d: %d\n",tests, sum2-a[0]);
		}
	}
}