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
int N, K;

int main ()
{
  scanf("%d", &TN);
  for (TC = 1; TC <= TN; ++TC)
  {
    scanf("%d%d", &N, &K);
    K %= (1 << N);
    printf("Case #%d: ", TC);
    if (K == ((1 << N) - 1))
      printf("ON\n");
    else
      printf("OFF\n");
  }
}
