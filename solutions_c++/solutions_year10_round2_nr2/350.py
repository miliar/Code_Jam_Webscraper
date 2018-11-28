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

int TN, TC;
int N, K, B, T;
int X[50], V[50];

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d%d%d%d", &N, &K, &B, &T);
    for (int i = 0; i < N; ++i)
      scanf("%d", &X[i]);
    for (int i = 0; i < N; ++i)
      scanf("%d", &V[i]);
    int red_duck = 0;
    int green_duck = 0;
    int swap_sum = 0;
    for (int i = N - 1; i >= 0; --i)
    {
      if (B - X[i] <= T * V[i])
      {
        swap_sum += red_duck;
        ++green_duck;
        if (green_duck == K)
          break;
      }
      else
        ++red_duck;
    }
    printf("Case #%d: ", TC);
    if (green_duck < K)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", swap_sum);
  }
}
