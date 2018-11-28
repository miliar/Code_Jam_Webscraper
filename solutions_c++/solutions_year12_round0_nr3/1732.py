#include <cstdio>
#include <algorithm>

using namespace std;

int when[1<<22];
int cookie = 0;

int main( void ) {
 //freopen( "out.txt", "w", stdout );
 int t; scanf( "%d", &t );
 for( int i = 0; i < t; ++i ){
    int a, b; scanf( "%d%d", &a, &b );

    int ans = 0;
    for( int j = a; j <= b; ++j ){
        ++cookie;
        int x = j;
        int lpot = 1;
        while( x > 0 ){ x /= 10; lpot *= 10; }
        x = j;

        int pot = 1;
        int suf = 0;

        while( x > 0 ){
            suf += pot*( x%10 );
            pot *= 10; x /= 10; lpot /= 10;
            if( j > x+suf*lpot && x+suf*lpot >= a && when[x+suf*lpot] != cookie ){ ++ans; when[x+suf*lpot] = cookie; }
        }
    }

    printf( "Case #%d: %d\n", i+1, ans );
 }

 return 0;
}
