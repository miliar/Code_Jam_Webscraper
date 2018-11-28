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

int L, D, N;
char dict[5000][16];
char str[500];
bool valid[15][26];

int solve ()
{
  memset(valid, false, sizeof(valid));
  int n = strlen(str);
  for (int i = 0, dx = 0; i < n; ++dx)
  {
    if (str[i] == '(')
    {
      int j;
      for (j = i + 1; j < n && str[j] != ')'; ++j);
      for (int k = i + 1; k < j; ++k)
        valid[dx][str[k] - 'a'] = true;
      i = j + 1;
    }
    else
    {
      valid[dx][str[i] - 'a'] = true;
      ++i;
    }
  }
  
  int ret = 0;
  for (int i = 0; i < D; ++i)
  {
    bool ok = true;
    for (int j = 0; j < L; ++j)
      if (!valid[j][dict[i][j] - 'a'])
      {
        ok = false;
        break;
      }
    if (ok)
      ++ret;
  }
  return ret;
}

int main ()
{
  scanf("%d%d%d", &L, &D, &N);
  for (int i = 0; i < D; ++i)
    scanf("%s", dict[i]);
  for (int i = 0; i < N; ++i)
  {
    scanf("%s", str);
    printf("Case #%d: %d\n", i + 1, solve());
  }
}
