#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <set>
#include <iostream>
using namespace std;

const int maxn = 10011;
int n;
int ed;
int d[maxn],l[maxn];
int f[maxn];

void readdata() {
     d[0] = 0;
     l[0] = 0;

     scanf( "%d", &n );
     for ( int i=1; i<=n; i++ ) scanf( "%d%d", &d[i], &l[i] );
     scanf( "%d", &ed );
}

void work() {
     memset( f, 255, sizeof(f) );
     f[1] = 0;
     
     int j = 1;
     for ( int i=1; i<=n; i++ ) {
         j = max( j, i+1 );
         while ( f[i]!=-1 && j<=n && abs( d[i]-d[j] )<=min( l[i], abs( d[i]-d[f[i]] ) ) ) {
               f[j] = i;
               j++;
         }
         if ( f[i]!=-1 && abs( d[i]-ed )<=min( l[i], abs( d[i]-d[f[i]] ) ) ) {
              printf( "YES\n" );
              return;
         }                  
     }
     printf( "NO\n" );
}

int main() {
    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );
    
    int T;
    scanf( "%d", &T );
    for ( int t=1; t<=T; t++ ) {
        printf( "Case #%d: ", t );
        readdata();
        work();
    }
    return 0;
}
