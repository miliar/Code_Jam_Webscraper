#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <cmath>
#include <ios>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <vector>
#include <utility>
#include <numeric>
#include <algorithm>

#define PRT(x) #x << ' ' << (x) << ' '
#define PRTPT(x,y) '(' << (x) << ',' << (y) << ')' << ' '
#define LNG(x) (sizeof(x)/sizeof(*(x)))
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int T;
double D;
int N, A;
double t[2000];
double x[2000];
double aval[250];

double solve(double a)
{
  double ans = sqrt(2*D/a);
  for(int i=0; i < N; ++i)
  {
    if(x[i] >= D)
    {
      const double nt = (t[i] - t[i-1]) * (D - x[i-1]) / (x[i] - x[i-1]);
      ans = max(ans, nt);
      break;
    }
    const double p = t[i] - sqrt(2*x[i]/a);
    const double nt = sqrt(2*D/a) + p;
    ans = max(ans, nt);
  }
  return ans;
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(10);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> D >> N >> A;
    for(int i=0; i < N; ++i) { cin >> t[i] >> x[i]; }
    for(int i=0; i < A; ++i) { cin >> aval[i]; }
    cout << "Case #" << X << ":\n";
    for(int i=0; i < A; ++i)
      cout << solve(aval[i]) << "\n";
  }
  return 0;
}
