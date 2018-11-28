#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
using namespace std;

//<macros>
#define rep(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define aout std::cout << "Case #" << (case_id+1) << ": "
//</macros>

//<libs>
//</libs>
typedef long long ll;

int num_cases, case_id=0;

#define MAXN 501

ll nck[MAXN][MAXN];
ll ways[MAXN][MAXN];

void precomp()
{
  memset(nck, 0, sizeof(nck));

  for (int n = 0; n < MAXN; ++n)
    nck[n][0] = 1;
  
  for (int n = 1; n < MAXN; ++n)
  {
    for (int k = 1; k <= n; ++k)
    {
      nck[n][k] = (nck[n-1][k-1] + nck[n-1][k])%100003;
//      std::cout << nck[n][k];

    }
//    std::cout << std::endl;
  }

  memset(ways, 0, sizeof(ways));

  for (int n = 2; n < MAXN; ++n)
    ways[n][1] = 1;

  for (int k = 2; k < MAXN; ++k)
  {
  for (int n = k+1; n < MAXN;  ++n)
  {
    int p = k;
//    for (int p = 2; p < n; ++p)
    for (int l = 1; l < k; ++l)
    {
      if (n-p >= k-l)
        ways[n][k] += (ways[p][l] * nck[n-p-1][k-l-1])%100003;
/*      if (n == 5 && k == 2)
      {
        std::cout << "p=" << p << "l=" << l << std::endl;
        std::cout << nck[n-p-1][k-l-1] << std::endl;
        std::cout << ways[p][l] << std::endl;
        }*/

    }
  }
  }
/*  for (int n = 0; n < 6; ++n)
  {
    for (int k = 0; k < 25; ++k)
      std::cout << ways[n][k];
    std::cout << std::endl;
    }*/
}

void solve()
{
  int n; cin >> n;
  int k;
  ll res = 0;
  rep(k, n) res += ways[n][k];
  aout << res%100003 << std::endl;
}

int main()
{
  precomp();

  std::cin >> num_cases;

  rep(case_id, num_cases)
  {
    solve();
  }
}

