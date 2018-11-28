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

int const N = 10;
int const M = 10000;
int n;
int v[N+1];

int solve()
{
  if( n == 0 )
    return 0;
    
  sort(v, v+n);
  int rv = 0;
  do
  {
    int pr = v[0];
    int q = 1<<29;
    for( int i = 0; i != n; )
    {
      int j = i;
      while( j < n && v[j] == v[i]+(j-i) )
        ++j;
      q = min(q, j - i);
      i = j;
    }
    rv = max(rv, q);
  } while( next_permutation(v, v+n) );
  return rv;
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    cin >> n;
    for( int i = 0; i != n; ++i )
      cin >> v[i];
    
    int rv = solve();
    cout << "Case #" << C << ": " << rv << '\n';
  }
  return 0;
}