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

int const N = 4;

int r, c;
int cm[128];
int m[N][N];
int ct[N][N];

//  cm['|'] = 0;
//  cm['-'] = 1;
//  cm['/'] = 2;
//  cm['\\']= 3;
int dx[4][2] = { {0, 0}, {1, -1}, {1, -1}, {-1, 1} };
int dy[4][2] = { {-1, 1}, {0, 0}, {-1, 1}, {-1, 1} };

int bit(int n, int i, int j)
{
  int d = (i*c + j);
  return (n >> d) & 1;
}

bool ok(int s)
{
  int t = r*c;
  //for( int k = 0; k != t; ++k )
  {
    memset(ct, 0, sizeof(ct));
    
    for( int i = 0; i != r; ++i )
    for( int j = 0; j != c; ++j )
    {
      int y = i + dy[m[i][j]][bit(s, i, j)];
      int x = j + dx[m[i][j]][bit(s, i, j)];
      //cout << i << ' ' << j << ' ' << y << ' ' << x << endl;
      if( y < 0 ) y = r - 1;
      if( y >= r ) y = 0;
      
      if( x < 0 ) x = c - 1;
      if( x >= c ) x = 0;
      
      if( ++ct[y][x] > 1 )
      {
        //cout << s << ": Error moving from " << i << ' ' << j << " to " << y << ' ' << x << " - " << m[i][j] << endl;
        return false;
      }
    }
  }
  
  return true;
}

int solve()
{
  int mx = 1<<(r*c);
  int rv = 0;
  for( int s = 0; s != mx; ++s )
  {
    if( ok(s) )
      ++rv;
  }
  return rv;
}

int main()
{
  cin.sync_with_stdio(false);
  cm['|'] = 0;
  cm['-'] = 1;
  cm['/'] = 2;
  cm['\\']= 3;
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> r >> c;
    for( int i = 0; i != r; ++i )
    {
      string line;
      cin >> line;
      for( int j = 0; j != c; ++j )
        m[i][j] = cm[line[j]];
    }
    
    int rv = solve();
    cout << "Case #" << C << ": " << rv << '\n';
  }
  return 0;
}