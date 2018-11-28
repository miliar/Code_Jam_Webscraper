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
#define LNG(x) (sizeof(x)/sizeof(*(x)))
#define MP make_pair
#define PB push_back
#define ALL(x) (x).begin(), (x).end()
#define INF 100000000

using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int T;
int N;
int s[200];

void solve()
{
  vector<bool> zero(N, false);
  vector<double> ans(N);
  bool update = true;
  int X=0;
  for(int i=0; i < N; ++i)
  {
    X += s[i];
  }
  while(update)
  {
    update = false;
    int tX=0;
    int tN=0;
    for(int i=0; i < N; ++i)
    {
      if(zero[i]) { continue; }
      ++tN;
      tX += s[i];
    }
    for(int i=0; i < N; ++i)
    {
      if(zero[i]) { continue; }
      double val = 100. * (((double)tX + X)/tN - (double)s[i])/X;
      if(val < 0)
      {
        zero[i] = true;
        update = true;
        val = 0.0;
      }
      ans[i] = val;
    }
  }
  for(int i=0; i < N; ++i)
  {
    cout << " " << ans[i];
  }
}

int main(int argc, char ** argv)
{
  std::ios_base::sync_with_stdio(false);
  cout.precision(8);
  cin >> T;
  for(int X=1; X<=T; ++X)
  {
    cin >> N;
    for(int i=0; i<N; ++i)
    {
      cin >> s[i];
    }
    cout << "Case #" << X << ":";
    solve();
    cout << "\n";
  }
  return 0;
}
