#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

const int MAXP = 1000000;
char isprime[MAXP];
int primes[MAXP];

int main(void)
{
  memset(isprime, 1, sizeof(isprime));
  int P = 0;
  for (int p = 2; p*p < MAXP; p++)
    if (isprime[p]) {
      primes[P++] = p;
      for (int kp = p*p; kp < MAXP; kp += p)
	isprime[kp] = 0;
    }

  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    long long N; cin >> N;
    int ans = 1;
    for (int i = 0; i < P && primes[i] <= N; i++) {
      int p = primes[i];
      long long n = N/p;
      while (n >= p) {
	ans++;
	n /= p;
      }
    }
    if (N == 1) ans = 0;
    printf("Case #%d: %d\n", test, ans);
  }
}
