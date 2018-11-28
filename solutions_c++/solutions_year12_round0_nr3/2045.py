#include <iostream>
#include <cmath>
#include <set>

using namespace std;

void printCase( int i )
{
   printf( "Case #%d: ", i );
}

int digitsInNum( int x )
{
   int ans = 0;
   while( x > 0 )
   {
      ++ans;
      x /= 10;
   }
   return ans;
}


   set<pair<int, int> > st;

int solve()
{
   st.clear();
   int n, m;
   cin >> n >> m;
   int t;
   int i;
   int ans = 0;
   int x;
   int j;
   int pr;
   for( i = n; i <= m; ++i )
   {
      int d = digitsInNum( i );
      t = 10;
      j = (int)pow(10., (double)d);
      x = i;
      while( t < x )
      {
         int n1 = x / t;
         int n2 = x % t;
         if( n2 >= t / 10 )
         {
            pr = n2 * ( j / t ) + n1;
            if( pr >= n && pr <= m && pr != i )
            {
               ++ans;
               st.insert( make_pair( min( i, pr ), max( i, pr )));
          //     cout << i << ' ' << pr << endl;
            }
         }
         t *= 10;
      }
   }
   return st.size();
   return ans / 2;
}

int main()
{
   freopen( "clarge.in", "r", stdin );
   freopen( "clarge.out", "w", stdout );
   int t;
   cin >> t;
   for( int i = 1; i <= t; ++i )
   {
      printCase(i);
      printf( "%d\n", solve());
   }
   return 0;
}