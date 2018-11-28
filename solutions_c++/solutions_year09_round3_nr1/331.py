#include <cmath>
#include <cctype>
#include <ctime>
#include <iostream>
#include <string>
#include <cstring>
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

ll t, brt, used[64], sol;
char c[64];

int main ()
{
    scanf ("%lld\n", &t );
    while ( t-- )
    {
       memset ( used , -1 , sizeof ( used ));
       scanf ( "%s" , &c );

       int n = strlen ( c ), base = 1, key = 1;
       sol = 0;

       if ( c[0] >= 'a' && c[0] <= 'z' ) used[ c[0] - 'a' +10] = 1 , base ++;
        else used[ c[0] - '0' ] = 1 , base ++;

       for ( int i=1; i < n; ++i )
       {
           int num = 0;
           if ( c[i] >= 'a' && c[i] <= 'z' ) num = (c[i] - 'a') + 10;
            else num = c[i] - '0' ;

           if ( used [ num ] == -1 )
           {
                if ( key )
                {
                    key = 0;
                    used[ num ] = 0;
                }
                else
                {
                    used[ num ] = base++;
                }
           }
       }

        //printf ( "found base %d\n" , base );

       for (int i=0; i < n; ++i)
       {
           int num = 0 ;
           if ( c[i] >= 'a' && c[i] <='z' ) num = (c[i]-'a') + 10;
           else num = c[i] - '0';
            //printf ( "%d\n" , used[num] );
           sol = sol*base + used[ num ];
           //printf ("sol is %lld\n" , sol );
       }

       printf ( "Case #%d: ", ++brt );
       printf ( "%lld\n" , sol );
    }
    return 0;
}
