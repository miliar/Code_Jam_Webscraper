#include <stdio.h>
#include <queue>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <assert.h>
#include <vector>

using namespace std;
typedef long long ll;
static const double EPS = 1e-9;
static const double PI = acos(-1.0);

#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define FOREQ(i, s, n) for (int i = (s); i <= (int)(n); i++)
#define FORIT(it, c) for (__typeof((c).begin())it = (c).begin(); it != (c).end(); it++)
#define DEC(i, s) for (int i = (s); i >= 0; i--)

#define SIZE(v) (int)((v).size())
#define MEMSET(v, h) memset((v), h, sizeof(v))
#define FIND(m, w) ((m).find(w) != (m).end())


const int PRIME_SIZE = 1000000;
int psize;
bool bprime[PRIME_SIZE+1];
int prime[PRIME_SIZE+1];
int Eratosthenes(int n) {
  psize = 0;
  memset(bprime, true, sizeof(bprime));
  bprime[0] = bprime[1] = false;
  for (int i = 2; i <= n; i++) {
    if (!bprime[i]) { continue; }
    prime[psize++] = i;
    for (int j = i + i; j <= n; j += i) {
      bprime[j] = false;
    }
  }
  return psize;
}

int seq[100];
int main() {
  Eratosthenes(1000000);
  int test;
  scanf("%d", &test);
  int test_case = 0;
  while (test--) {
    test_case++;
    int d, k;
    scanf("%d %d", &d, &k);
    REP(i, k) { scanf("%d", &seq[i]); }
    int pow10 = 1;
    int ans = -1;
    if (k == 1) { goto end; }
    {
      REP(i, d) { pow10 *= 10; }
      REP(iter, psize) {
        int p = prime[iter];
        if (p >= pow10) { break; }
        REP(i, k) { if (p <= seq[i]) { goto nextprime; } }
          REP(a, p) {
            int b = (seq[1] - seq[0] * a + p * p) % p;
            int s = seq[0];
            REP(i, k) {
              s = ((ll)s * a + b) % p;
              if (i != k - 1 && s != seq[i + 1]) { goto next; }
            }
            if (ans == -1 || ans == s) { ans = s; }
            else { ans = -1; goto end; }
next:;
          }
nextprime:;
        }
      }
end:;
    if (ans != -1) {
      printf("Case #%d: %d\n", test_case, ans);
    } else {
      printf("Case #%d: I don't know.\n", test_case);
    }
  }
}
