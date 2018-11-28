#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cctype>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <list>
#include <functional>
#include <numeric>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
#include <stdexcept>
using namespace std;
using namespace __gnu_cxx;

typedef long long ll;
const int infinity = 1000000000;

const int maxn = 20;

char poly[10000];
char words[100][64];

int value[100][32];
int k, n;

int acum[32];

const ll mod = 10009;

ll eval() {
  ll ret = 0, prod = 1;
  for (int i = 0; poly[i]; ++i) {
    if (poly[i] == '+') {
      ret = (ret + prod) % mod;
      prod = 1;
    } else {
      prod = (prod * acum[poly[i] - 'a']) % mod;
    }
  }
  return ret;
}

ll ret[11];

ll times[maxn + 1];

ll fact[maxn + 1];

void bt(int i, int next) {
  assert(i <= k);

  if (next > 0 && times[next - 1] > 0) {
    ll a = fact[i];
    for (int j = 0; j < next; ++j)
      a /= fact[times[j]];
    a %= mod;
//    printf("%lli %lli\n", a, eval());
    ret[i] = (ret[i] + a * eval()) % mod;
  }
  if (next >= n) return;

  int warra[32]={};
  for (int j = 0; j < next; ++j)
    for (int l = 0; words[j][l]; ++l)
      warra[words[j][l]-'a'] += times[j];
  for (int j = 0; j < 32; ++j)
    assert(warra[j] == acum[j]);

  bt(i, next + 1);
  for (int rep = 1; rep + i <= k; ++rep) {
    for (int j = 0; words[next][j]; ++j)
      acum[words[next][j] - 'a'] += rep;
    times[next] = rep;
    bt(i + rep, next + 1);
    for (int j = 0; words[next][j]; ++j)
      acum[words[next][j] - 'a'] -= rep;
  }
  times[next] = 0;
}

int main() {
  fact[0] = 1;
  for (int i = 1; i <= maxn; ++i)
    fact[i] = i * fact[i - 1];

  int cases;
  scanf("%i\n", &cases);
  for (int caseno = 1; caseno <= cases; ++caseno) {
    printf("Case #%i: ", caseno);
    scanf("%s %i %i", poly, &k, &n);
    strcat(poly, "+");

    for (int i = 0; i < n; ++i) {
      scanf("%s", words[i]);
      fill(&value[i][0], &value[i][32], 0);
      for (int j = 0; words[i][j]; ++j)
        ++value[i][words[i][j] - 'a'];
    }

    fill(&acum[0], &acum[32], 0);
    fill(&ret[0], &ret[k + 1], 0);
    fill(&times[0], &times[n], 0);
    bt(0, 0);
    for (int i = 1; i <= k; ++i) {
      printf("%lli", ret[i]);
      if (i < k) printf(" ");
    }
    puts("");

    fflush(stdout);
  }
  return 0;
}
