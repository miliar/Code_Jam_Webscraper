#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdio>
using namespace std ;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n ;
    cin >> n ;
    for ( int tests = 1 ; tests <= n ; ++tests )
    {
        int ret = 0  ;
        int t, op=1, bp=1, ostore=0, bstore=0 ; char a ; int p ;
        cin >> t ;
        for ( int i = 0 ; i < t ; ++i )
        {
            cin >> a >> p ;
            int delta = 0 ;
            if ( a == 'O' )
            {
                delta = max( 0, abs(p - op)-ostore ) + 1 ;
                ret += delta ;
                op = p ;
                bstore += delta ;
				ostore = 0 ;
            }
            else
            {
                delta = max( 0, abs(p - bp)-bstore ) + 1 ;
                ret += delta ;
                bp = p ;
                ostore += delta ;
				bstore = 0 ;
            }
			//cout << ret << endl ;
        }
        printf("Case #%d: %d\n", tests, ret );
    }
    return 0 ;
}
