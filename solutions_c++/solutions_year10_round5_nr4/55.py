#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

using namespace std;

typedef long long dbl;
typedef long long ll;
typedef pair <dbl, dbl> pnt;

ll mod = 1000000007;

ll dp[77][77][77];
ll C[77][77], fc[77], sum[77 * 177][77];

int need[77], nn;
ll n; int b;

int get (int i, int c, int h) {
  if (i == nn) {
    return c == 0 && h == 0;
  }
  ll & res = dp[i][c][h];
  if (res != -1) {
    return res;
  }
  res = 0;
  for (int nh = 0; nh <= h; nh++) {
    for (int st = ((need[i] - c) % b + b) % b; st <= b * h; st += b) {
      // no zeros
      res += (get(i + 1, (c + st) / b, nh) * sum[st][h])  % mod * C[h][nh] % mod * fc[nh] % mod;
      res %= mod;
      // 1 zero
      if (nh) {
        res += get(i + 1, (c + st) / b, nh) * sum[st][h - 1] % mod * C[h - 1][nh - 1] % mod * fc[nh] % mod;
      }
    }
  }
  return res;
}

int main( void )
{
  int tn;
  cin >> tn;

  C[0][0] = 1;
  for (int i = 0; i < 72; i++) {
    for (int j = 0; j <= i; j++) {
      C[i + 1][j] = (C[i + 1][j] + C[i][j]) % mod;
      C[i + 1][j + 1] = (C[i + 1][j + 1] + C[i][j]) % mod;
    }
  }
  fc[0] = 1;
  for (int i = 0; i < 72; i++) {
    fc[i + 1] = (fc[i] * (i + 1)) % mod;
  }

  for (int tt = 1; tt <= tn; tt++) {
    printf("Case #%d: ", tt);

    cin >> n >> b;
    nn = 0;
    while (n) {
      need[nn++] = n % b;
      n /= b;
    }

    memset(sum, 0, sizeof(sum));
    sum[0][0] = 1;
    for (int c = 1; c < b; c++) {
      for (int s = c * c; s >= 0; s--) {
        for (int i = c - 1; i >= 0; i--) {
          sum[s + c][i + 1] += sum[s][i];
        }
      }
    }

    memset(dp, -1, sizeof(dp));
    ll res = 0;
    for (int h = b; h >= 1; h--) {
      res = (res + get(0, 0, h)) % mod;
    }
    cout << res << endl;
  }
  return 0;
}

