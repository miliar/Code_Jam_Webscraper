#include <sstream>
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
#include <boost/unordered_set.hpp>

using namespace std;
#define AUTO(a, b) typeof(b) a = (b)

typedef unsigned long long ull;
typedef unsigned uint;

/*double solve(int n)
{
  // f(2) = 1 + (1/2 f(2) + 1/2 f(0))
  // f(2) = 1 / (1/2) = 2
  
  // f(3) = 1 + (1/3 f(3) + 1/2 f(2))
  // f(3) = (2) (3/2)
  // f(3) = 3
  
  // 2 3 4 1
  // 2 3 1 4 -> 2 + f(3)
  // 0: 9/24
  // 1: 4 !(3) -> 8/24
  // 2: 6 !(2) -> 6/24
  // 3: 0
  // 4: 1/24
  // (24/15)(1 + 1/3 f(3) + 1/4 f(2))
  // (24/15)(5/2)
  // (12/3) = 4
  
  // 0: 0
  // 1: 0
  // 2: 2
  // 3: 15/4
  // 4: 66/15
  // 5: 
  // n deranged elements
  f(n)(1-p(deranged)) = 1 + sum( p(i)*f(n-i), i = 1..n )
}*/

int main()
{
  int T;
  cin >> T;
  for( int C = 1; C <= T; C++ )
  {
    int n;
    cin >> n;
    
    int rv = 0;
    for( int i = 0; i != n; ++i )
    {
      int x;
      cin >> x;
      if( x != (1 + i) )
        ++rv;
    }
    cout << "Case #" << C << ": " << rv << ".000000\n";
  }
  return 0;
}