#include <cstdio>
#include <fstream>
#include <iostream>
#include <cstring>
#include <string>

using namespace std;

const int MaxN = 1001;

string a[ MaxN ], b[ MaxN ];
char c[ MaxN ];

int main( void )
{
    ifstream in( "A-large.in" );
    ofstream out( "A-large.out" );
    int t;
    in >> t; 
    //cout << t << endl;
    for( int h = 1; h <= t; ++h )
    {
         int n, m;
         in >> n;
         in.getline( c, sizeof( c ) );
         for( int i = 0; i < n; ++i )
         {
              in.getline( c, sizeof( c ) );
              a[i].clear();
              for( int j = 0; j < strlen( c ); ++j )
                   a[i].push_back( c[j] );
         }
         
         in >> m;    
         in.getline( c, sizeof( c ) );
         for( int i = 0; i < m; ++i )
         {
              in.getline( c, sizeof( c ) );
              b[i].clear();
              for( int j = 0; j < strlen( c ); ++j )
                   b[i].push_back( c[j] );
         }
        // cout << n << " " << m << endl;
         int now = -1, ret = 0;
         
         for( int i = 0; i < m; ++i )
         {
              if( now == -1 || a[now] == b[i] )
              {
                  int maks = -1, maksi = -1;
                  for( int j = 0; j < n; ++j )
                       for( int k = i; k <= m; ++k )
                            if( k == m || a[j] == b[k] )
                            {
                                if( k > maks )
                                {
                                    maks = k;
                                    maksi = j;
                                }
                                break;
                            }
                  if( now != -1 ) ++ret;
                  now = maksi;
              }
         }
         out << "Case #" << h << ": " << ret << endl;
    }
    return 0;
}
                        
                  
         
              
