#include <cstdio>
#include <cstring>

int memo[10010][10010];
char bio[10010][10010], cookie = 0;
int p, q, cell[111];

int rec( int l, int r ) {

    int &ret = memo[l][r];
    if( bio[l][r] == cookie ) return ret;
    bio[l][r] = cookie;

    int ima = 0;
    for( int i = 0; i < q; ++i )
        if( l <= cell[i] && cell[i] <= r ) {
                ima = 1;
                break;
        }

    if( !ima ) return ret = 0;

    ret = 1000000000;
    for( int i = 0; i < q; ++i )
        if( l <= cell[i] && cell[i] <= r ) {
            ret <?= rec( l, cell[i]-1 ) + rec( cell[i]+1, r )
                    + r-l;
        }

    return ret;

}

int main( void ) {

 int test; scanf( "%d", &test );

 for( int cs = 0; cs < test; ++cs ) {
        scanf( "%d%d", &p, &q );

        for( int i = 0; i < q; ++i ) {
            scanf( "%d", cell+i );
            --cell[i];
        }

        ++cookie;
        printf( "Case #%d: %d\n", cs+1, rec( 0, p-1 ) );
 }

 return 0;
}
