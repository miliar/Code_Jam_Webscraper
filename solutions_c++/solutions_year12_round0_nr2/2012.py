#include <iostream>

using namespace std;

const int maxn = 100;

void printCase( int i )
{
   printf( "Case #%d: ", i );
}

int solve()
{
   int n, s, p;
   cin >> n >> s >> p;
   int ans = 0, x;
   for( int i = 0; i < n; ++i )
   {
      cin >> x;
      if( (x+2)/3 >= p )
         ++ans;
      else
         if( s > 0 )
            if( x > 0 && x % 3 == 0 && x / 3 + 1 >= p && x / 3 + 1 <= 10 )
            {
               ++ans;
               --s;
            }
            else if( x % 3 == 2 && ( x + 2 ) / 3 + 1 >= p && ( x + 2 ) / 3 + 1 <= 10)
            {
               ++ans;
               --s;
            }
   }
   return ans;
}

int main()
{
   
   freopen( "blarge.in", "r", stdin );
   freopen( "blarge.out", "w", stdout );
   int t;
   cin >> t;
   for( int i = 1; i <= t; ++i )
   {
      printCase(i);
      printf( "%d\n", solve());
   }
   return 0;
}