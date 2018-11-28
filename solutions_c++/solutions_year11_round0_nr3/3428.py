#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <list>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

int solve()
{
  int n, m;
  int add_total = 0;
  int xor_total = 0;
  int smallest = 1 << 30;
  
  cin >> n;
  while(n>0) {
    --n;
    cin >> m;
    add_total += m;
    xor_total ^= m;
    if (m < smallest)
      smallest = m;
  }

  if (xor_total != 0)
    return 0;
  return add_total - smallest;
}

int main(int ac, char **av)
{
  int cases;

  cin >> cases;
  for (int i=1; i <= cases; ++i) {
    int n = solve();
    cout << "Case #" << i << ": ";
    if (n > 0)
      cout << n;
    else
      cout << "NO";
    cout << endl;
  }
  return 0;
}

