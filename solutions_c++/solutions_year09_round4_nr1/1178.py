#include <cmath>
#include <cctype>
#include <ctime>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <algorithm>
#include <utility>

#define forn(a,b,c) for (int a=b; a < c; ++a)
#define x first
#define y second
#define pb push_back
#define mp make_pair
#define set(a,b) memset ((a) , b , sizeof(a) )

using namespace std;

typedef pair <int , int> pii;
typedef long long ll;
typedef vector <int> vi;

int brt, t, n;
int a[64][64], r[64], sol;
string s ;

int main ()
{
    scanf ( "%d\n" , &t );

    while ( t-- )
    {
        scanf ("%d\n" , &n );

        set ( a , 0 );
        set ( r , 0 );

        forn ( i , 0 , n )
        {
            int ch = 0;

            cin >> s;

            forn ( j , 0 , n )
            {
                a[i][j] = s[j] - '0';
                ch += ( a[i][j] << j );
            }
            r[ i ] = ch;
        }

        int p = 0; sol = 0;
        forn (i , 0 , n )
        {
            p |= ( 1 << i );
            if ( r[i] > p )
            {
                for (int j=i+1; j < n; ++j)
                    if ( r[j] <= p )
                    {
                        for (int k=j-1; k >= i; --k)
                            swap( r[k] , r[k+1] );

                        sol += j-i;
                        break;
                    }
            }
        }

        printf ( "Case #%d: %d\n" , ++brt, sol );
    }

    return 0;
}
