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

int const N = 20;
int p[N];

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    string str;
    cin >> str;

    int n = 0, m = str.size();
    ull base = 0;
    for( int i = 0; i != m; ++i )
    {
      base <<= 1;
      if( str[i] == '?' )
        p[n++] = i;
      else
        base |= str[i]-'0';
    }
    int const mx = (1<<n);
    for( int s = 0; s != mx; ++s )
    {
      ull v = base;
      for( int i = 0; i != n; ++i )
        if( s & (1<<i) )
          v |= (1LL<<(m-p[i]-1));
      
      ull r = sqrt(v);
      if( r*r == v )
      {
        for( int i = 0; i != n; ++i )
          str[p[i]] = '0' + ((s>>i) & 1);
        break;
      }
    }
    cout << "Case #" << C << ": " << str << '\n';
  }
  return 0;
}