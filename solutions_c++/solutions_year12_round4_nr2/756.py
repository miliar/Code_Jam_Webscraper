#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <set>
#include <ctime>
#include <iostream>
using namespace std;

const int maxn = 150;
int r[maxn];
int x[maxn];
int y[maxn];

bool inter( int i, int j ) {
     long long R = r[i]+r[j];
     R = R*R;
     long long X = x[i]-x[j];
     X = X*X;
     long long Y = y[i]-y[j];
     Y = Y*Y;
     if ( X+Y<R ) return true;
     else return false;
}

int main() {
    freopen( "in.txt", "r", stdin );
    freopen( "out.txt", "w", stdout );
    srand(time(0));
    
    int T;
    scanf( "%d", &T );
    
    for ( int t=1; t<=T; t++ ) {
        printf( "Case #%d: ", t );
        int n,w,l;
        scanf( "%d%d%d", &n, &w, &l );
        for ( int i=0; i<n; i++ ) scanf( "%d", &r[i] );
        
        for ( int i=0; i<n; i++ ) {
            while ( true ) {
                  long long r1 = rand();
                  long long r2 = rand();
                  long long r3 = rand();
                  long long r4 = rand();
                  r2 = r2*r2%(w+1);
                  r4 = r4*r4%(l+1);
                  x[i] = r2;
                  y[i] = r4;
                  if ( i==0 ) {
                     x[i]=0;
                     y[i]=0;
                  }
                  bool flag = false;
                  for ( int j=0; j<i; j++ )
                  if ( inter( i, j ) ) { flag = true; break; }
                  if ( !flag ) break;
            }
            printf( " %d %d", x[i], y[i] );
        }
        printf( "\n" );
        
    }
}
