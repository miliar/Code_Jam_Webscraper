#include <iostream>
#include <cstring>
#include <cstdio>
#define MAXN ( 1 << 13 )
using namespace std;

int l, d, n, brt, sol, key, in, brm, t;
string dict[MAXN], q;

int main ()
{
    scanf ( "%d%d%d\n" , &l, &d, &n );

    for (int i=0; i < d; ++i)
    {
        getline (cin , dict[i]);
    }

    for (int i=0; i < n; ++i)
    {
        getline (cin , q);

        sol = 0;

        for (int j=0; j < d; ++j)
        {
            key = 1;
            in = brm = 0;
            for (int k=0; k < q.size(); ++k)
            {
                t = 0;
                if ( q[k] == '(' )
                    while  ( q[++k] != ')' )
                    {
                        if ( t ) continue;
                        if ( q[k] == dict[j][brm] ) brm ++ , t = 1;
                    }
                else
                {
                    t = 1;
                    if ( q[k] != dict[j][brm] ) { key = 0; break; }
                    //printf ( "%c" , q[k] );
                    brm ++;
                }
                //printf ( "\n" );
                //printf ( "%d %d\n", j, brm );
                if ( !t || !key ) { key = 0; break; }
            }
            sol += key;
        }

        printf ( "Case #%d: %d\n" , ++brt, sol );
    }
    return 0;
}
