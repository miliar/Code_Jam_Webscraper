#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <ios>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <utility>
#include <numeric>
#include <algorithm>

#define PRT(x) #x << ' ' << (x) << ' '
#define LNG(x) (sizeof(x)/sizeof(*(x)))

using namespace std;

int T;
int A, B;
double p[100000];
double sum_p[100000];

double solve()
{
  sum_p[0] = p[0];
  for(int i=1; i < A; ++i)
  {
    sum_p[i] = sum_p[i-1] * p[i];
  }
  double ans = 2 + B;
  for(int i=0; i < A; ++i)
  {
    const int bs = A - i - 1;
    const int rest = B - i - 1;
    const int good = bs + rest + 1;
    const int bad = good + B + 1;
    ans = min(ans, sum_p[i] * good + (1-sum_p[i]) * bad);
  }
  return ans;
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(8);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> A >> B;
    for(int i=0; i<A; ++i)
    {
      cin >> p[i];
    }
    cout << "Case #" << X << ": " << solve() << endl;
  }
  return 0;
}
