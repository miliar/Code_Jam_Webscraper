#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>
#include <deque>

using namespace std;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define MEMSET(v, h) memset((v), h, sizeof(v))

void solve();
int main() {
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    printf("Case #%d: ", test_case);
    solve();
  }
}

int c, d, n;
char str[100];
char combine[200][200];
int oppose[200][200];
deque<char> deq;

void Push(char c) {
  if (!deq.empty()) {
    char nc = combine[(int)deq.back()][(int)c];
    if (nc != 0) {
      deq.pop_back();
      Push(nc);
      return;
    }
  }
  FORIT(it, deq) {
    if (oppose[(int)*it][(int)c]) {
      deq.clear();
      return;
    }
  }
  deq.push_back(c);
}

void solve() {
  deq.clear();
  MEMSET(combine, 0);
  MEMSET(oppose, 0);
  scanf("%d", &c);
  REP(i, c) {
    scanf("%s", str);
    combine[(int)str[0]][(int)str[1]] = str[2];
    combine[(int)str[1]][(int)str[0]] = str[2];
  }
  scanf("%d", &d);
  REP(i, d) {
    scanf("%s", str);
    oppose[(int)str[0]][(int)str[1]] = 1;
    oppose[(int)str[1]][(int)str[0]] = 1;
  }
  scanf("%d %s", &n, str);
  REP(i, n) { Push(str[i]); }
  printf("[");
  REP(i, deq.size()) {
    if (i != 0) { printf(", "); }
    putchar(deq[i]);
  }
  printf("]\n");
}
