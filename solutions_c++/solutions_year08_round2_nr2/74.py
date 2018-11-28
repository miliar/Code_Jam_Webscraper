#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

const int MaxN = 1005;

bool a[ MaxN ];
vector< int > prime;
vector< vector< int > > v;
bool as[ MaxN ][ MaxN ];

void sito( int g )
{
     memset( a, 0, sizeof( a ) );
     for( int i = 2; i < g; i += 2 )
          if( !a[i] )
          {
              for( int j = 2; i * j < g; ++j )
                   a[i * j] = 1;
              prime.push_back( i );
              if( i == 2 ) --i;
          }
}

void merge( int i, int j )
{
     vector< int > tmp;
     tmp = v[j];
     v[j] = v[v.size() - 1];
     for( int k = 0; k < tmp.size(); ++k )
          v[i].push_back( tmp[k] );
     v.resize( v.size() - 1 );
}

int main( void )
{
    sito( MaxN );
    int t, a, b, P;
    ifstream in( "B-small-attempt1.in" );
    ofstream out( "B2.out" );
    
    in >> t;
    
    for( int T = 1; T <= t; ++T )
    {
         v.resize( 0 );
         in >> a >> b >> P;
         v.resize( b - a + 1 );
         for( int i = a; i <= b; ++i )
              v[i - a].push_back( i );
              memset( as, 0, sizeof( as ) );
         int g = lower_bound( prime.begin(), prime.end(), P ) - prime.begin();
         for( int i = a; i < b; ++i )
              for( int j = i + 1; j <= b; ++j )
                   for( int p = g; p < prime.size(); ++p ) 
                        if( !( i % prime[p] ) && !( j % prime[p] ) ) 
                        {
                            as[i][j] = as[j][i] = 1;
                            break;
                        }                 
         while( 1 )
         {
                bool ok = 1;
               for( int i = 0; ok && i < v.size() - 1; ++i )
                    for( int j = i + 1; ok && j < v.size(); ++j )
                         for( int e1 = 0; ok && e1 < v[i].size(); ++e1 )
                              for( int e2 = 0; ok && e2 < v[j].size(); ++e2 )
                                    if( as[v[i][e1]][v[j][e2]] )
                                    {
                                            merge( i, j );
                                            ok = 0;
                                    }
               if( ok ) break;
         }
         out << "Case #" << T << ": " << v.size() << endl;
                   
    }
    return 0;
}
