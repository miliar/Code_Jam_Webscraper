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
#include <cassert>

#define x first
#define y second
#define pb push_back
#define mp make_pair
#define forit(i, s) for(__typeof(s.begin()) i = s.begin(); i != s.end(); i++)

using namespace std;

typedef long long dbl;
typedef long long ll;
typedef pair <dbl, dbl> pnt;

#define maxn 2000000
int f[maxn], p[maxn], pn;

set <int> res;

ll mod;

ll upd(ll &x) {
  x %= mod;
  if (x < 0) {
    x += mod;
  }
  return x;
}

ll mul (ll a, ll b) {
  upd(a), upd(b);
  return (a * b) % mod;
}

ll mpow(ll x, ll p) {
  ll res = 1;

  while (p) {
    if (p & 1) {
      res = mul(res, x);
    }
    x = mul(x, x);
    p >>= 1;
  }
  return res;
}

ll rev(ll x) {
  upd(x);
  return mpow(x, mod - 2);
}

void check (ll A, ll B, vector <int> v) {
  if (v[0] >= mod) {
    return;
  }
  for (int i = 0; i + 1 < (int)v.size(); i++) {
    if ((v[i] * A + B) % mod != v[i + 1]) {
      return;
    }
  }
  res.insert((v.back() * A + B) % mod);
}

int main( void )
{
  for (int i = 2; i < maxn; i++) {
    if (!f[i]) {
      p[pn++] = i;
      for (long long j = (long long)i * i; j < maxn; j += i) {
        f[j] = 1;
      }
    }
  }
  int tn;
  cin >> tn;
  for (int tt = 0; tt < tn; tt++) {
    printf("Case #%d: ", tt + 1);
    int d, k;
    scanf("%d%d", &d, &k);
    vector <int> v(k);
    for (int i = 0; i < k; i++) {
      cin >> v[i];
    }


    if (k == 1 || (k == 2 && v[0] != v[1])) {
      printf("I don't know.\n");
      continue;
    }
    if (v[0] == v[1]) {
      printf("%d\n", v[0]);
      continue;
    }

    int mx = 1;
    while (d--) {
      mx *= 10;
    }
    
    res.clear();

    int i = 0;
    while (p[i] <= mx) {
      mod = p[i++];
  //    cerr << mod << endl;
      ll dv = rev(v[0] - v[1]);
      ll a = dv, b = -dv,
         c = mul(-v[1], dv), d = mul(v[0], dv);
      ll A = v[1] * a + v[2] * b, B = v[1] * c + v[2] * d;
      upd(A), upd(B);
      check(A, B, v);
    }
    assert(res.size() > 0);
    if (res.size() == 1) {
      printf("%d\n", *res.begin());
    } else {
      printf("I don't know.\n");
    }
  }
  return 0;
}

