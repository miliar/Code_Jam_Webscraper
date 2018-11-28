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

double const eps = 1e-9;

int n, d;
int p[201];
int q[201];

bool ok(double t)
{
  double pr = -1e100;
  for( int i = 0; i != n; ++i )
  {
    double mn = max(pr + d, p[i] - t);
    double end= mn + (q[i]-1)*d;
    if( end - p[i] + eps > t )
      return false;
      
    pr = end;
  }
  
  return true;
}

double solve()
{
  double r = 1e14;
  double l = 0;
  for( int k = 0; k != 100; ++k )
  {
    double m = (l + r) / 2;
    if( ok(m) )
      r = m;
    else
      l = m;
  }
  
  return l;
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> n >> d;
    for( int i = 0; i != n; ++i )
      cin >> p[i] >> q[i];
    cout << "Case #" << C << ": " << solve() << '\n';
  }
  return 0;
}