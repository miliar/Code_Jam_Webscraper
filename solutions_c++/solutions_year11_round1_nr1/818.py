#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <cstdio>
using namespace std;

int gcd(int a, int b)
{
  if (b == 0)
    return a;
  return gcd(b, a%b);
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    bool possible = true;
    cout << "Case #" << t << ": ";

    long long int PD, PG, N;
    cin >> N >> PD >> PG;

    if (PD != 100 && PG == 100)
      possible = false;
    if (PD > 0 && PG == 0)
      possible = false;

    int g = gcd(PD, 100-PD);
    long long int D = PD / g + (100-PD) / g;

    if (D > N)
      possible = false;

    if (possible)
      cout << "Possible" << endl;
    else
      cout << "Broken" << endl;
  }
  return 0;
}
