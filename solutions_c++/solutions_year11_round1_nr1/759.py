#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <set>
#include <deque>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

ull gcd(ull x, ull y)
{
  while( y )
  {
    x %= y;
    swap(x, y);
  }
  return x;
}

int main()
{
  cin.sync_with_stdio(false);
  
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    int pd, pg;
    ull n;
    cin >> n >> pd >> pg;
    char const* msg[] = { "Broken", "Possible" };

    ull g = gcd(100, pd);
    bool rv = !pd || ((100/g) <= n);
    if( rv )
    {
      if((pd < 100 && pg == 100)
      || (pd > 0 && pg == 0) )
        rv = false;
    }    
    cout << "Case #" << C << ": " << msg[rv] << '\n';
  }
  return 0;
}