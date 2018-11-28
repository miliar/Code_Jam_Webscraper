#include <cstdio>
#include <climits>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

int main ()
{
  freopen( "C-small-attempt0.in",  "r", stdin );
  freopen( "C-small-attempt0.out", "w", stdout );

  int T = 0;
  cin >> T;
  for ( int i = 1; i <= T; i++ )
  {
      // load:
    int R, k, N, euro = 0;
    cin >> R >> k >> N;
    deque< int > q( 0 );
    for ( int j = 1; j <= N; j++ )
    {
      int size = 0;
      cin >> size;
      q.push_back( size );
    }
        
      // solve:
    for ( int j = 0; j < R; j++ )
    {
      int max = 0;
      int num = 0;
      while ( true )
      {
        if ( num + q.front() <= k &&
             max < N )
        {
          num += q.front();
          int a = q.front();
          q.pop_front();
          q.push_back( a );
          max++;
        }
        else
          break;
      }

      euro += num;
    }
    
    cout << "Case #" << i << ": " << euro << "\n";
  }

  exit( 0 );
}
