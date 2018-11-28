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
  freopen( "A-small-attempt2.in",  "r", stdin );
  freopen( "A-small-attempt2.out", "w", stdout );

  int T = 0;
  cin >> T;
  for ( int i = 1; i <= T; i++ )
  {
      // load:
    int N, K;
    cin >> N >> K;
    vector< bool > snapper( 0 );
    vector< bool > power( 0 );
    power.push_back( true );
    for ( int j = 1; j <= N; j++ )
    {
      snapper.push_back( false );
      power.push_back( false );
    }
        
      // solve:
    for ( int j = 0; j < K; j++ )
    { 
      for ( int m = 0; m < N; m++ )
        if ( power[m] )
          snapper[m] = !snapper[m];
      
      for ( int m = 0; m < N; m++ )
      {
        if ( power[m] && snapper[m] )
          power[m+1] = true;
        else
          power[m+1] = false;
      }
    }
    
    if ( power.back() )
      cout << "Case #" << i << ": ON\n";
    else
      cout << "Case #" << i << ": OFF\n";      
  }

  exit( 0 );
}
