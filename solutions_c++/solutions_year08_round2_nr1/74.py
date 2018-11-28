#include <cstdio>
#include <fstream>

using namespace std;

const int MaxN = 100001;

typedef long long llint;

llint x[ MaxN ], y[ MaxN ];
int main( void )
{
    ifstream in( "A-small-attempt1.in" );
    ofstream out( "A.out" );
    int t;
    in >> t;
    
    for( int T = 1; T <= t; ++T )
    {
         memset( x, 0, sizeof( x ) );
         memset( y, 0, sizeof( y ) );
         llint n, A, B, C, D, M;
         in >> n >> A >> B >> C >> D >> x[0] >> y[0] >> M;

         for( int i = 1; i < n; ++i )
         {
              x[i] = ( A * x[i - 1] + B ) % M;
              y[i] = ( C * y[i - 1] + D ) % M;
         }
         
         int ret = 0;
         for( int i = 0; i < n - 2; ++i )
              for( int j = i + 1; j < n - 1; ++j )
                   for( int k = j + 1; k < n; ++k )
                   {
                        llint sx = x[i] + x[j] + x[k], sy = y[i] + y[j] + y[k];
                        llint cx = sx / 3LL, cy = sy / 3LL;
                        if( cx * 3LL == sx && cy * 3LL == sy ) ++ret;
                   }
         out << "Case #" << T << ": " << ret << endl;
                   
    }
   // for( ; ; );
    return 0;
}

