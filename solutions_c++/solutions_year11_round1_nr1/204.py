#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <complex>
using namespace std;

// begin insert defines
typedef long long LL;
// end insert defines

LL n;
int pd, pg;

inline LL gcd(LL a, LL b) {return b ? gcd(b, a % b) : a;}

bool work()
{
  if (pg == 0) return pd == 0;
  if (pg == 100) return pd == 100;
  LL g = gcd(pd, 100);
  return n >= 100 / g;
}

void myin()
{
  scanf("%lld%d%d", &n, &pd, &pg);
}

int main()
{
  int tests;
  scanf("%d", &tests);
  for (int Ca = 0; Ca < tests; Ca++) {
    printf("Case #%d: ", Ca + 1);
    myin();
    work() ? puts("Possible") : puts("Broken");
  }
  return 0;
}

