#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <deque>
#include <boost/unordered_map.hpp>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

int const N = 1000000;
int r, c, d;
string m[11];

bool ok(int i, int j, int k)
{
  double cx = j + k / 2.;
  double cy = i + k / 2.;
  
  double sx = 0, sy = 0;
  for( int y = 0; y != k; ++y )
  {
    int mnx, mxx;
    if( y == 0 || y+1 == k )
      mnx = 1, mxx = k-2;
    else
      mnx = 0, mxx = k-1;
      
    for( int x = mnx; x <= mxx; ++x )
    {
      double dx = (j + x + 0.5) - cx;
      double dy = (i + y + 0.5) - cy;
      sx += dx * (d + m[i+y][j+x]-'0');
      sy += dy * (d + m[i+y][j+x]-'0');
    }
  }
  return (fabs(sx) <= 1e-9)
      && (fabs(sy) <= 1e-9);
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> r >> c >> d;
    for( int i = 0; i != r; ++i )
      cin >> m[i];
    
    int rv = 0;
    for( int k = min(r, c); k >= 3; --k )
    {
      for( int i = 0; i+k <= r; ++i )
      for( int j = 0; j+k <= r; ++j )
        if( ok(i, j, k) )
        {
          rv = k;
          goto done;
        }
    }
  done:
    if( rv == 0 )
      cout << "Case #" << C << ": " << "IMPOSSIBLE" << '\n';
    else
      cout << "Case #" << C << ": " << rv << '\n';
  }
  return 0;
}