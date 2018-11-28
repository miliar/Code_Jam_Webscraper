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

int TC, TN;
int N;
char line[50];

int num[40];

int solve ()
{
  int ret = 0;
  for (int i = 0; i < N; ++i)
  {
    int j;
    for (j = i; j < N && !(num[j] <= i + 1); ++j);
    for (int k = j; k > i; --k)
    {
      swap(num[k], num[k - 1]);
      ++ret;
    }
  }
  return ret;
}

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d ", &N);
    for (int i = 0; i < N; ++i)
    {
      gets(line);
      int n = strlen(line);
      num[i] = 0;
      for (int j = 0; j < n; ++j)
        if (line[j] == '1')
          num[i] = j + 1;
    }
    int ans = solve();
    printf("Case #%d: %d\n", TC, ans);
  }
}
