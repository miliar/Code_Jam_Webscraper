#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;

int n, m;
char a[30];

int main( ){
    int i, t, cas, l;
    freopen( "B-large.in", "r", stdin );
    freopen( "B-large.out", "w", stdout );
    scanf( "%d", &t );
    for( cas = 1; cas <= t; cas++ ){
        scanf( "%s", a );
        l = strlen( a );
        printf( "Case #%d: ", cas );
        if( !next_permutation( a, a + l ) ){
            int u = -1;
            for( i = 0; i < l; i++ )
                if( a[i] != '0' ){
                    u = i;
                    printf( "%c", a[i] );
                    break;
                }
            printf( "0" );
            for( i = 0; i < l; i++ )
                if( i != u ) printf( "%c", a[i] );
            printf( "\n" );
        }else{
            for( i = 0; i < l; i++ )
                printf( "%c", a[i] );
            printf( "\n" );
        }
    }
    return 0;
}
