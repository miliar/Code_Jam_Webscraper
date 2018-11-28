#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

const int MaxN = 10002;
const int INF = 30000;

int n, k;       
string s;
int ret;

void rek( vector< int > v )
{
     if( v.size() == k ) {
         char last = '-';
         int maks = 0, curr = 0;
         int b = s.size() / k;
         for( int j = 0; j < b; ++j )
              for( int i = 0; i < k; ++i )
              {
                   char c = s[j * k + v[i] ];
                   if( c == last ) ++curr; else
                   {
                       ++maks;
                       curr = 1;
                   }
                   last = c;
              }
         ret = min( maks, ret );
         return;
     } 
     {
         bool ba[20];
         memset( ba, 0, sizeof( ba ) ); 
         for( int i = 0; i < v.size(); ++i )
              ba[v[i]] = 1;

         for( int i = 0; i < k; ++i ) 
              if( !ba[i] )
              {
                  v.push_back( i );
                  rek( v );
                  v.erase( v.end() - 1 );
              }
     }
}

int main( void )
{
    int t;
    ifstream in( "D.in" );
    ofstream out( "D.out" );
    in >> t;
    for( int R = 1; R <= t; ++R )
    {
         ret = INF;
         in >> k;
         in >> s;
         cout << s;
         vector< int > v;
         v.clear();
         rek( v );
         out << "Case #" << R << ": " << ret << endl;
    }
//for(;;);
    return 0;
}
