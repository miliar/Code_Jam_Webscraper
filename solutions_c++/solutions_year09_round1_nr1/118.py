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

const int maxn = 100010;
bool happy[maxn + 1][11];
int sumsqr[maxn + 1][11], first[1 << 9];

int calcsumsqr(int i, int j) {
  int sum = 0, a = i;
  while (a) {
    int d = a % j;
    sum = (sum + d * d);
    a /= j;
    if (a <= maxn && sumsqr[a][j] >= 0) {
      sum += sumsqr[a][j];
      break;
    }
  }
  return sum;
}

int main() {
  fill(&happy[0][0], &happy[maxn + 1][0], false);
  for (int i = 2; i <= 10; ++i) happy[1][i] = true;

  fill(&sumsqr[0][0], &sumsqr[maxn + 1][0], -1);
  for (int i = 0; i <= maxn; ++i)
    for (int j = 2; j <= 10; ++j)
      sumsqr[i][j] = calcsumsqr(i, j);

  bool done;
  for (;;) {
    done = true;
    for (int i = 1; i <= maxn; ++i)
      for (int j = 2; j <= 10; ++j) if (!happy[i][j]) {
        int s = sumsqr[i][j];
        if (s <= maxn && happy[s][j]) {
          happy[i][j] = true;
          done = false;
        }
      }
    if (done) break;
  }

  int rem = 1 << 9;
  for (int i = 2; rem > 0; ++i) {
    int j, subset = 0;
/*    if (i % 100000 == 0)
      printf("trying %i,  %i remaining\n", i, rem);*/
    for (j = 2; j <= 10; ++j) {
      int p = min(i, calcsumsqr(i, j));
      if (happy[p][j]) subset |= 1 << (j - 2);
    }
    int s = subset;
    for (;;) {
      if (first[s] == 0) {
        first[s] = i;
        printf("s[%i] = %i;\n", s, i);
        --rem;
      }
      if (!s) break;
      s = (s - 1) & subset;
    }
  }
  return 0;
}
