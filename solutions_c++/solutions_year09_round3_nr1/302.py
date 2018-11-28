#include<iostream>
#include<string.h>
#include<map>
using namespace std;

char a[100];
map< char, int > r;
map< char, int > r1;
__int64 b[100];

int main( ){
    int i, t, l, cas;
	__int64 num;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout ) ;
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        r.clear( );
        r1.clear( );
		memset( b, 0, sizeof( b ) ); 
        scanf( "%s", &a );
        l = strlen( a );
        num = 0;
        for( i = 0; i < l; i++ )
            if( r[a[i]] == 0 ){
                r[a[i]] = 1;
                num++;
            }
		if( num == 1 ) num = 2;
        r1[a[0]] = 1;
        int cur = 0;
        for( i = 1; i < l; i++ ){
            if( r1[a[i]] == 0 ){
				if( cur == 0 ){ r1[a[i]] = -1; cur = 2; }
                else{
					r1[a[i]] = cur;
					cur++;
				}
            }
        }
        for( i = 0; i < l; i++ )
			if( r1[a[i]] == -1 ) b[i] = 0;
            else b[i] = r1[a[i]];
        __int64 p = 0;
        __int64 k = 1;
        for( i = l - 1; i >= 0; i-- ){
            p += b[i] * k;
            k = k * num;
        }
        printf( "Case #%d: %I64d\n", cas, p );
    }
    return 0;
}
