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

int a[32], d[32], used[32], brt, t, n, found;
char c[32];
vi b;

int cmp ( int a, int b)
{
    return a > b;
}

void solve (int lvl , int h)
{
    /*
    printf ("in solve ( %d , %d )\n" , lvl , h );
    printf ("matched: ");
    for (int i=0; i < lvl; ++i)
        printf ( "%d", d[i] );
    printf ("\n");
    cin.get ();
    */
    if ( lvl == n && h )
    {
        //for (int i=0; i < n; ++i)
        //    sol[i] = d[i] + '0';
        found = 1;
        return ;
    }

    if ( lvl >= n ) return ;

    if ( h == 0 )
        {
        for (int i=0; i <= 9; ++i)
        {
            //printf ( "checking for %d\n" , i );

            if ( i >= ( c[lvl]-'0' ) && (used[ i ] > 0) )
            {
                used[ i ]--;
                d[lvl] = i;
                solve ( lvl + 1, (i > (c[lvl]-'0'))? 1: h );
                if ( found ) return ;
                d[lvl] = 0;
                used[ i ]++;
            }
        }
        return ;
        }
    else
        for (int i=0; i <= 9; ++i)
            if ( used[i] > 0 )
            {
                used[i] --;
                d[lvl] = i;
                solve ( lvl + 1, h );
                if ( found ) return ;
                used[i] ++;
            }
}

int main ()
{
    scanf ( "%d", &t );

    while ( t -- )
    {
        memset ( a, 0, sizeof (a));
        memset ( d, 0, sizeof (d));
        memset ( used, 0, sizeof (used));

        found = 0;

        scanf ( "%s", c );
        n = strlen (c);

        for (int i=0; i < n; ++i)
        {
            a[ c[i]-'0' ] ++;
            used[ c[i]-'0' ] ++;
        }

        solve ( 0 , 0 );

        if ( found ) { printf ( "Case #%d: ", ++brt ); for (int i=0; i < n; ++i) printf ( "%d" , d[i] ); printf ( "\n" ); }
        else
        {
            vi b;
            b.clear ();

            for (int i=0; i < n; ++i)
                b.push_back ( c[i] - '0' );

            sort ( b.begin () , b.end () );

            int minn = 10 , ind = -1;
            for (int i=0; i < n; ++i)
            {
                if ( b[i] > 0 && b[i] < minn )
                {
                    minn = b[i];
                    ind = i;
                }
            }
            b[ind] = 0;

            printf ( "Case #%d: ", ++brt );
            printf ( "%d", minn );
            sort ( b.begin () , b.end () );
            for (int i=0; i < n; ++i)
                printf ( "%d", b[i] );

            printf ( "\n" );
        }
    }
    return 0;
}
