
#include <iostream>
#include <cstdio>
using namespace std;

long long gcd(long long a, long long b) {
    while(b)  std::swap(a%=b, b); 
      return a;
}

void solve(int CASE) {
  bool possible = true;

  long long n, pd, pg;

  cin >> n >> pd >> pg;

  long long mind = 100/gcd(pd, 100);
  long long maxd = n/mind*mind;

  if (n < mind)
    possible = false;
  else {
    if (pd != 100 && pg == 100)
      possible = false;
    if (pg == 0 && pd > 0)
      possible = false;
  }

  if (possible)
    printf("Case #%d: Possible\n", CASE);
  else
    printf("Case #%d: Broken\n", CASE);
}

int main()
{
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
    solve(i);
  return 0;
}
