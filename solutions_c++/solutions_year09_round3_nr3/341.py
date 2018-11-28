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

int a[128], t, brt, n , k, sol , best;
vi b;

int main ()
{
    scanf ( "%d", &t );

    while ( t --)
    {
        memset ( a , 0 , sizeof ( a ) );
        scanf ( "%d%d", &n , &k );

        sol = 0; best = -1;
        b.clear ();

        for (int i=0; i < k; ++i)
        {
            int tmp ;
            scanf ("%d" , &tmp );

            b.push_back ( tmp );
        }

        do
        {
            memset ( a , 0 , sizeof ( a ));

            sol = 0;

            for (int i=0; i < k; ++i)
            {
                int tmp = b[i] ;

                a[tmp] = 1;
                int br = tmp;
                while ( (++br) <= n )
                {
                    if ( a[br] == 1 ) break;
                    sol ++;
                }
                br = tmp;
                while ( (--br) >= 1 )
                {
                    if ( a[br] == 1 ) break;
                    sol ++;
                }
            }

            if ( sol < best || ( best == -1 ) )
                best = sol;

        }while ( next_permutation ( b.begin () , b.end () ) );

        printf ("Case #%d: %d\n", (++brt) , best );
    }
    return 0;
}
