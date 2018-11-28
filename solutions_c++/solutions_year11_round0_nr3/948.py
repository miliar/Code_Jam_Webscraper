#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

int v[1001];

int main()
{
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    int n, w = 0, s = 0;
    cin >> n;
    for( int i = 0; i != n; ++i )
    {
      cin >> v[i];
      w ^= v[i];
      s += v[i];
    }
    if( w != 0 )
      cout << "Case #" << C << ": " << "NO" << '\n';
    else
      cout << "Case #" << C << ": " << s - *min_element(v,v+n) << '\n';
  }
  return 0;
}