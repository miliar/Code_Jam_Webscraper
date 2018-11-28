#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1 << 6;

char ma3x[MAXN][MAXN];
int r , c;


void read() {
        scanf ( "%d%d" , &r , &c );

        int i;
        for (i = 0; i < r; ++i)
                scanf ( "%s" , &ma3x[i] );
}

void print() {
        static int i , j;
        for (i = 0; i < r; ++i) {
                for (j = 0; j < c; ++j)
                        printf ( "%c" , ma3x[i][j] );
                puts ( "" );
        }
}

bool transform() {
        static int i , j;
        for (i = 0; i < r; ++i)
                for (j = 0; j < c; ++j) {
                        if ( ma3x[i][j] == '#' ) {
                                if ( i + 1 >= r || j + 1 >= c ||
                                     ma3x[i + 1][j] != '#' || ma3x[i][j + 1] != '#' || ma3x[i + 1][j + 1] != '#' )
                                            return 0;

                                else {
                                        ma3x[i][j] = '/';
                                        ma3x[i][j + 1] = '\\';
                                        ma3x[i + 1][j] = '\\';
                                        ma3x[i + 1][j + 1] = '/';
                                }
                        }
                }
        return 1;
}

void solve ( int tCase ) {
        int i , j;

        printf ( "Case #%d:\n" , tCase );
        for (i = 0; i < r; ++i)
                for (j = 0; j < c; ++j)
                        if ( ma3x[i][j] == '#' ) {

                                if ( transform() )
                                        print();
                                else
                                        puts ( "Impossible" );

                                return;
                        }

        print();
}

int main() {
        int tests;
        scanf ( "%d" , &tests );

        for (int i = 1; i <= tests; ++i) {
                read();
                solve ( i );
        }
        return 0;
}
