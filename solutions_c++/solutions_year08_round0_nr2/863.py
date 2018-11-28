// Google Code Jam 2008 
// Qualification Round
// Problem B - Train Timetable

#include <cstdio>
#include <fstream>
#include <iostream>
#include <cstring>
#include <string>

#define a first
#define b second

using namespace std;

const int MaxN = 101;

pair< int, int > T[ MaxN * 2 ];
bool A[ MaxN * 2 ];
bool c[ MaxN * 2 ];
int dp[ MaxN * 2 ];
int last[ MaxN * 2];

ifstream in( "B-large.in" );
ofstream out( "B-large.out" );
    
int read()
{
    int ret = 0;
    char c1, c2;
    in >> c1 >> c2;
    ret = ( ( c1 - '0' ) * 10 + c2 - '0' ) * 60;
    in >> c1;
    in >> c1 >> c2;
    ret += ( ( c1 - '0' ) * 10 + c2 - '0' );
    return ret;
}

int main( void )
{
    
    int t;
    in >> t; 
    for( int h = 1; h <= t; ++h )
    {
         memset( A, 0, sizeof( A ) );
         
         int n, m, k;
         in >> k >> n >> m;
         
         for( int i = 0; i < n + m; ++i )
         {
              T[i].a = read();
              T[i].b = read();
              if( i < n ) A[i] = 1;
              dp[i] = 1;
         }
         
         for( int i = 0; i < n + m - 1; ++i )
              for( int j = i + 1; j < n + m; ++j )
                   if( T[i].a > T[j].a || ( T[i].a == T[j].a && T[i].b > T[j].b ) )
                   {
                       swap( A[i], A[j] );
                       swap( T[i], T[j] ); 
                   }
        memset( last, -1, sizeof( last ) );
         int ret1 = 0, ret2 = 0;
         
         memset( c, 0, sizeof( c ) );
         
         for( int i = 0; i < n + m; ++i )
         {
              if( !c[i] )
              {
                  if( A[i] ) ++ret1; else ++ret2;
              }
              int maksi = -1;
              for( int j = i; j < n + m; ++j )
                   if( !c[j] && A[i] != A[j] && T[i].b + k <= T[j].a && ( maksi == -1 || T[j].a < T[maksi].a ) ) maksi = j;
              
              if( maksi != -1 ) c[maksi] = 1;
         }
         out << "Case #" << h << ": " << ret1 << " " << ret2 << endl;
    }
    return 0;
}
                        
                  
         
              
