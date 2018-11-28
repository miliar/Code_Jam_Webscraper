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

const char *match = "welcome to code jam";

int N;
char str[550];
int dp[19][500];

int gdp (int dx, int pos)
{
  if (dx == 19)
    return 1;
  if (pos == N)
    return 0;
  int &ret = dp[dx][pos];
  if (ret != -1)
    return ret;
  ret = gdp(dx, pos + 1);
  if (str[pos] == match[dx])
    ret += gdp(dx + 1, pos + 1);
  ret %= 10000;
  return ret;
}

int solve ()
{
  memset(dp, -1, sizeof(dp));
  return gdp(0, 0);
}

int main ()
{
  scanf("%d ", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    gets(str);
    N = strlen(str);
    printf("Case #%d: %04d\n", TC, solve());
  }
}
