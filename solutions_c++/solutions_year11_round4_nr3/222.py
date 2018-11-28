#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

bool ipr[1000000 + 5];
int pr[500000];
int ct;

void init() {
  int n = 1000000 + 3;
  for (int i = 2; i < 1024; ++i)
    if (!ipr[i])
      for (int j = i * i; j <= n; j+=i)
	ipr[j] = true;
  ct = 0;
  for (int i = 2; i < n; ++i)
    if (!ipr[i]) pr[ct++] = i;
}

long long solve(long long n) {
  if (n == 1) return 0;
  long long ans = 1;
  for (int i = 0; i < ct; ++i) {
    long long p = pr[i], q = n;
    if (p * p > n) break;
    int u = -1;
    while (q) {
      q /= p; ++u;
    }
    ans += u - 1;
  }
  return ans;
}

int main() {
  init();
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; ++tc) {
    long long n;
    cin >> n;
    printf("Case #%d: %lld\n",tc, solve(n));
  }
  return 0;
}
