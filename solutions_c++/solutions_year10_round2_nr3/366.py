#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#include <ios>
#include <istream>
#include <ostream>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <bitset>
#include <map>

#include <new>
#include <functional>
#include <string>
#include <iterator>
#include <algorithm>
#include <complex>
#include <utility>
#include <numeric>
#include <typeinfo>

using namespace std;

#define max2(a,b) (((a) > (b)) ? (a) : (b))
#define min2(a,b) (((a) < (b)) ? (a) : (b))
#define sqr(x) ((x) * (x))
#define SZ(x) (int(x.size()))

#define TIMER_A(timer) int timer = clock()
#define TIMER_B(timer) cerr << (#timer) << ": " << (double)(clock() - timer) / CLOCKS_PER_SEC << endl

#define debug(x) cerr << (#x) << ": " << (x) << endl
#define debug_array(x, N) \
cout << (#x) << ":"; \
for (int i = 0; i < N; ++i) \
  cout << " " << x[i]; \
cout << endl
#define echo(x) cerr << (#x) << endl

#define PB push_back
#define MP make_pair
#define FI first
#define SE second

const double eps = 1e-8;
const double pi = acos(-1.0);
const int oo = 0x7f7f7f7f;

typedef long long LL;

const int Pr = 100003;

int TN, TC;

int N;
int cb[501][501];
int dp[501][501];

void init ()
{
  memset(cb, 0, sizeof(cb));
  cb[0][0] = 1;
  for (int i = 1; i <= 500; ++i)
  {
    cb[i][0] = 1;
    for (int j = 1; j < i; ++j)
      cb[i][j] = (cb[i - 1][j] + cb[i - 1][j - 1]) % Pr;
    cb[i][i] = 1;
  }
}

void calc ()
{
  memset(dp, 0, sizeof(dp));
  for (int i = 2; i <= 500; ++i)
    dp[i][1] = 1;
  for (int i = 2; i <= 500; ++i)
    for (int j = 2; j < i; ++j)
    {
      dp[i][j] = 0;
      for (int k = 1; k < j; ++k)
        dp[i][j] = (dp[i][j] + dp[j][k] * cb[i - j - 1][j - k - 1] % Pr) % Pr;
    }
}

int main ()
{
  init();
  calc();
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d", &N);
    int ans = 0;
    for (int i = 1; i < N; ++i)
      ans = (ans + dp[N][i]) % Pr;
    printf("Case #%d: %d\n", TC, ans);
  }
}
