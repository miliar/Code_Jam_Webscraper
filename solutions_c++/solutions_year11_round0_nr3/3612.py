#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std ;

int main()
{
    freopen("input.txt","r",stdin) ;
    freopen("output.txt","w",stdout);

    int T ;
    cin >> T ;
    for( int t = 1 ; t <= T ; ++t)
    {
        int N ;
        cin >> N ;

        int a ;
        cin >> a ;
        int min = a ;
        int sum = a ;
        int result = a ;
        for ( int i = 1 ; i < N ; ++i )
        {
            int a ;
            cin >> a ;
            result ^= a ;
            sum += a ;
            if( a < min )
                min = a ;
        }
        cout << "Case #" << t << ": " ;
        if ( result != 0)
            cout << "NO\n" ;
        else
            cout << sum - min << endl ;
    }
    return 0 ;
}
