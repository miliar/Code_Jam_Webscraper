#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define sz(x) ((int)(x).size())

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

//int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

const int MAXI = 1e6 + 100;
bool prime[MAXI + 1];
void solve() {
  ll n;
  scanf("%I64d\n", &n);
  if (n == 1) { printf("0\n"); return; }

  int ans = 1;
  for (int i = 2; i <= MAXI; i++) if (prime[i]) {
    int cnt = 0;
    for (ll x = i; x <= n; x *= i)
      cnt++;
    if (cnt > 1)
      ans += cnt - 1;
  }
  printf("%d\n", ans);
}

int main(int argc, char* argv[]) {
  {
    string fname = "std";
    if (argc >= 2) {
      fname = argv[1];
      if (fname.length() >= 3 && string(fname, fname.length() - 3) == ".in")
        fname = string(fname, 0, fname.length() - 3);
    }
    freopen((fname + ".in").c_str(), "r", stdin);
    freopen((fname + ".out").c_str(), "w", stdout);
  }

  memset(prime, 1, sizeof prime);
  for (int i = 2; i <= MAXI; i++) if (prime[i]) {
    for (int i2 = 2 * i; i2 <= MAXI; i2 += i)
      prime[i2] = false;
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    printf("Case #%d: ", TN);
    eprintf("Case #%d\n", TN);
    solve();
  }
  return 0;
}
