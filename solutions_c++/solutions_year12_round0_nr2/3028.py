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

int T, N, S, p;
#define MAX_N 128
int t[MAX_N];

int best_wo_sup(int x)
{
  switch(x % 3)
  {
  case 0:
    return x / 3;
  case 1:
    return (x - 1) / 3 + 1;
  case 2:
    return (x - 2) / 3 + 1;
  default:
    assert(false);
  }
}

bool cansup(int x)
{
  return 2 <= x && x <= 28;
}

int supeffect(int x)
{
  switch(x % 3)
  {
  case 0: return 1;
  case 1: return 0;
  case 2: return 1;
  default: assert(false);
  }
}

int solve()
{
  int rest_S = S;
  int ans = 0;
  for(int i=0; i<N; ++i)
  {
    const int best = best_wo_sup(t[i]);
    if(best >= p) { ++ans; continue; }
    if(rest_S > 0 && cansup(t[i]) && supeffect(t[i]) + best >= p)
    {
      --rest_S;
      ++ans;
    }
  }
  return ans;
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);

  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> N >> S >> p;
    for(int i=0; i<N; ++i) { cin >> t[i]; }
    cout << "Case #" << X << ": " << solve() << endl;
  }
  return 0;
}
