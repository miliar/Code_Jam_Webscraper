#include <fstream>
#include <cstring>

using namespace std;

int freq [ 512 ];
char tr [ 55 ] [ 4 ];
char el [ 55 ] [ 4 ];
char s [ 128 ], coada [ 128 ];
int c, d, n, csize;

void init (){
    csize = 0;
    memset ( freq, 0, sizeof ( freq ) );
}

void solve (){
    int i, j;
    for ( i = 0; i < n; ++ i ){
        coada [ csize ++ ] = s [ i ];
        ++ freq [ ( int ) s [ i ] ];
        if ( csize > 1 ) {
            for ( j = 0; j < c; ++ j ){
                if ( coada [ csize - 1 ] == tr [ j ] [ 0 ] && coada [ csize - 2 ] == tr [ j ] [ 1 ]
                || coada [ csize - 1 ] == tr [ j ] [ 1 ] && coada [ csize - 2 ] == tr [ j ] [ 0 ] ){
                    -- freq [ ( int ) coada [ csize - 1 ] ];
                    -- freq [ ( int ) coada [ csize - 2 ] ];
                    csize -= 2;
                    coada [ csize ++ ] = tr [ j ] [ 2 ];
                    ++ freq [ ( int ) tr [ j ] [ 2 ] ];
                    break;
                }
            }
            if ( j == c ){
                for ( j = 0; j < d; ++ j ){
                    if ( s [ i ] == el [ j ] [ 0 ] && freq [ ( int ) el [ j ] [ 1 ] ] || s [ i ] == el [ j ] [ 1 ] && freq [ ( int ) el [ j ] [ 0 ] ] ){
                        init();
                        break;
                    }
                }
            }
        }
    }
}

int main(){
    int i, j, t;
    ifstream f ( "magicka.in" );
    ofstream g ( "magicka.out" );
    f >> t;
    for ( j = 1; j <= t; ++ j ){
        init ();
        f >> c;
        for ( i = 0; i < c; ++ i ){
            f >> tr [ i ];
        }
        f >> d;
        for ( i = 0; i < d; ++ i ){
            f >> el [ i ];
        }
        f >> n;
        f >> s;
        solve();
        g << "Case #" << j << ": ";
        g << "[";
        for ( i = 0; i < csize - 1; ++ i )
            g << coada [ i ] << ", ";
        if ( csize - 1 >= 0 )
            g << coada [ csize - 1 ];
        g << "]\n";
    }
    f.close();
    g.close();
    return 0;
}
