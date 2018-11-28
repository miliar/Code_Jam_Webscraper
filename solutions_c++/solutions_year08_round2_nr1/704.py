#include <stdio.h>
#include <set>

typedef std::pair<unsigned long long int, unsigned long long int>  coords;
typedef std::set<coords>    trees;

int main ( int argc, char * argv [] )
{
    if ( argc < 2 )
        return -1;

    printf ( "%s\n", argv[1] );

    FILE * fp = fopen (argv[1], "r" );
    FILE * fo = fopen ("t1.output", "w" );

    int T = 0;
    fscanf ( fp, "%d", &T );
    printf ( "Numbet of tests: %d\n", T );

    for ( int t = 1; t <= T; t++ )
    {
        int _n, _A, _B, _C, _D, _x_0, _y_0, _M;

        fscanf ( fp, "%d %d %d %d %d %d %d %d",
                &_n,
                &_A, &_B, &_C, &_D,
                &_x_0, &_y_0, &_M
               );        

        unsigned long long int n, A, B, C, D, x_0, y_0, M;
        n = _n;
        A = _A;
        B = _B;
        C = _C;
        D = _D;
        x_0 = _x_0;
        y_0 = _y_0;
        M = _M;

        trees Tr;
        Tr.insert ( coords(x_0,y_0) );
        printf ( "(%d,%d)\n", x_0, y_0 );
        for ( unsigned long long int i = 1; i <= n-1; i++ )
        {
            x_0 = ((A%M) * (x_0%M) + (B%M))%M;
            y_0 = ((C%M) * (y_0%M) + (D%M))%M;
            printf ( "(%d,%d)\n", x_0, y_0 );

            Tr.insert ( coords(x_0,y_0) );
        }
        printf ( "---------------------------\n" );

        unsigned long long int total = 0; 
        for ( trees::iterator it1 = Tr.begin(); it1 != Tr.end(); it1++ )
        {
            for ( trees::iterator it2 = it1; it2 != Tr.end(); it2++ )
            {
                for ( trees::iterator it3 = it2; it3 != Tr.end(); it3++ )
                {
                    if ( it1 == it2 || it2 == it3 || it3 == it1 )
                        continue;
                    unsigned long long int X1 = it1->first;
                    unsigned long long int Y1 = it1->second;
                    unsigned long long int X2 = it2->first;
                    unsigned long long int Y2 = it2->second;
                    unsigned long long int X3 = it3->first;
                    unsigned long long int Y3 = it3->second;

                    if ( (X1+X2+X3)%3 == 0 && (Y1+Y2+Y3)%3 == 0 )
                    {
//                        printf ( "(%d,%d) (%d,%d) (%d,%d)\n", X1,Y1, X2,Y2, X3,Y3 );
                        total++;
                    }
                }

            }
        }
        printf ( "************************************\n" );

        int _total = total;
        fprintf ( fo, "Case #%d: %d\n", t, _total );
    }

    fclose (fp);
    fclose (fo);

    return 0;
}
