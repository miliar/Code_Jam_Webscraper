#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int gcd(int a, int b)
{
  if (a < 0) a = -a;
  if (b < 0) b = -b;
  int tmp;
  while (a != 0)
    {
      tmp = a;
      a = b % a;
      b = tmp;
    }
  return b;
}

int main(void)
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N; int P_D, P_G; cin >> N >> P_D >> P_G;
    bool possible = true;
    if (P_G == 0) {
      possible = P_D == 0;
    }
    else if (P_G == 100) {
      possible = P_D == 100;
    }
    else {
      possible = 100 / gcd(P_D, 100) <= N;
    }
    printf("Case #%d: %s\n", t, possible ? "Possible" : "Broken");
  }
}
