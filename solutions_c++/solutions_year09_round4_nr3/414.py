#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <complex>
#include <ctime>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))
#define sqr(x) ((x) * (x))
#define debug(x) cout << (#x) << ": " << (x) << endl
#define echo(x) cout << (#x) << endl
#define SZ(x) (int(x.size()))

#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const double eps = 1e-8;
const double pi = acos(-1.0);
const int oo = 0x7f7f7f7f;

typedef long long LL;

int TN, TC;

int N, K;
int pri[16][25];

bool conn[16][16];
bool valid[1 << 16];

int dp[1 << 16];

bool calc_conn (int a, int b)
{
  if (pri[a][0] < pri[b][0])
    swap(a, b);
  for (int i = 0; i < K; ++i)
    if (pri[a][i] <= pri[b][i])
      return true;
  return false;
}

bool calc_valid (int mask)
{
  for (int i = 0; i < N; ++i)
    if (mask & 1 << i)
      for (int j = i + 1; j < N; ++j)
        if (mask & 1 << j)
          if (conn[i][j])
            return false;
  return true;
}

int gdp (int mask)
{
  if (mask == 0)
    return 0;
  int &ret = dp[mask];
  if (ret != -1)
    return ret;
  ret = oo;
  for (int mk = mask; mk != 0; mk = (mk - 1) & mask)
    if (valid[mk])
      ret <?= gdp(mask ^ mk) + 1;
  return ret;
}

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; ++i)
      for (int j = 0; j < K; ++j)
        scanf("%d", &pri[i][j]);
    for (int i = 0; i < N; ++i)
      for (int j = i + 1; j < N; ++j)
        conn[i][j] = conn[j][i] = calc_conn(i, j);
    for (int i = 0; i < 1 << N; ++i)
      valid[i] = calc_valid(i);
    memset(dp, -1, sizeof(dp));
    int ans = gdp((1 << N) - 1);
    printf("Case #%d: %d\n", TC, ans);
  }
}
