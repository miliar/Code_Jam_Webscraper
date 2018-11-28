#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

typedef long long LL;

int gcd(int x, int y)
{
  return y ? gcd(y, x%y) : x;
}

int main()
{
  int pg, pd;
  LL n;

  int t;
  scanf("%d", &t);
  for (int l = 1; l <= t; ++l) {
    scanf("%lld%d%d", &n, &pd, &pg);
    printf("Case #%d: ", l);

    if (pg == 100 && pd != 100) {
      puts("Broken");
      continue;
    }
    if (pg == 0 && pd != 0) {
      puts("Broken");
      continue;
    }

    if (n < 100/gcd(100 ,pd))
      puts("Broken");
    else 
      puts("Possible");
    
  }

  return 0;
}
