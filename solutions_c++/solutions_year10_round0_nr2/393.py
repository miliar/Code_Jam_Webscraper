
#include <algorithm>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <vector>

#define LI long long
#define MP make_pair
#define PB push_back
#define SQ(a) ((a)*(a))
#define SZ size()
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

#define BASE 1000000000

struct big {
  vector<int> V;
  big(): V(1, 0) {}
  big(int n): V(1, n) {}
  big(const big &b): V(b.V) {}
  bool operator==(const big &b) const { return V==b.V; }
  int &operator[](int i) { return V[i]; }
  int operator[](int i) const { return V[i]; }
  int size() const { return V.SZ; }
  void resize(int i) { V.resize(i); }
  bool operator<(const big &b) const {
    for (int i = b.SZ-1; V.SZ == b.SZ && i >= 0; i--)
      if (V[i] == b[i]) continue;
      else return (V[i] < b[i]);
    return (V.SZ < b.SZ);
  }
  void add_digit(int l) {
    if (l > 0) V.PB(l);
  }
  void fix() {
    while (V[V.SZ-1] == 0 && V.SZ > 1)
      resize(V.SZ-1);
  }
};
inline big suma(const big &a, const big &b, int k) {
  LI l = 0;
  int size = MAX(a.SZ, b.SZ+k);
  big c;  c.resize(size);
  for (int i = 0; i < size; ++i) {
    l += i < a.SZ ? a[i] : 0;
    l += (k <= i && i < k + b.SZ) ? b[i-k] : 0;
    c[i] = l%BASE;
    l /= BASE;
  }
  c.add_digit(int(l));
  return c;
}
inline big operator*(const big &a, int b) {
  if (b == 0) return big(0);
  big c;  c.resize(a.SZ);
  LI l = 0;
  for (int i = 0; i < a.SZ; ++i) {
    l += (LI)b*a[i];
    c[i] = l%BASE;
    l /= BASE;
  }
  c.add_digit(int(l));
  return c;
}
inline big operator-(const big &a, const big &b) {
  assert(b < a || a == b);
  big c;
  LI l = 0, r = 0;
  c.resize(a.SZ);
  for (int i = 0; i < a.SZ; ++i) {
    l += a[i] - r;
    l -= i < b.SZ ? b[i] : 0;
    if (l < 0) {
      r = 1;
      l += BASE;
    }
    else r = 0;
    c[i] = l%BASE;
    l /= BASE;
  }
  while (c[c.SZ-1] == 0 && c.SZ > 1)
    c.resize(c.SZ-1);
  return c;
}
inline void divmod(const big &a, int b, big &div, int &mod) {
  div.resize(a.SZ);
  LI l = 0;
  for (int i = a.SZ-1; i >= 0; --i) {
    l *= BASE;
    l += a[i];
    div[i] = l/b;
    l %= b;
  }
  while (div[div.SZ-1] == 0 && div.SZ > 1)
    div.resize(div.SZ-1);
  mod=int(l);
}
inline big operator+(const big &a, const big &b) {
  return suma(a, b, 0);
}
inline big operator+(const big &a, int b) {return a+big(b);}
inline big operator+(int b, const big &a) {return a+big(b);}
inline big operator-(const big &a, int b) {return a-big(b);}
inline big operator*(int b, const big &a) {return a*b;}
inline big operator*(const big &a, const big &b) {
  big res;
  for (int i = 0; i < b.SZ; ++i)
    res = suma(res, a*b[i], i);
  return res;
}
inline big operator/(const big &a, int b) {
  big div;  int mod;
  divmod(a, b, div, mod);
  return div;
}
inline int operator%(const big &a, int b) {
  big div;  int mod;
  divmod(a, b, div, mod);
  return mod;
}

inline istream &operator>>(istream &is, big &b) {
  string s;
  is >> s;
  b.resize((s.SZ-1)/9 + 1);
  for (int n = s.SZ, k = 0; n > 0; n -= 9, k++) {
    b[k] = 0;
    for (int i = MAX(n-9, 0); i < n; i++)
      b[k] = 10*b[k] + s[i]-'0';
  }
  return is;
}

inline ostream &operator<<(ostream &os, const big &b) {
  os << b[b.SZ-1];
  for (int k = b.SZ-2; k >= 0; k--)
    os << setw(9) << setfill('0') << b[k];
  return os;
}

big bigmod(big &a, big &b) {
  big x = 0, y = a;
  while (x < y) {
    big m = (x + y + 1)/2;
    if (a < b*m) y = m-1;
    else x = m;
  }
  big p = x*b;
  p.fix();
  return a - p;
}

big gcd(big &a, big &b) {
  if (a < b) return gcd(b, a);
  big m = bigmod(a, b);
  if (m == 0) return b;
  else return gcd(b, m);
}

int main() {
  int C, N;
  cin >> C;
  for (int i = 1; i <= C; i++) {
    cin >> N;
    vector<big> v(N);
    for (int j = 0; j < N; j++)
      cin >> v[j];
    sort(v.rbegin(), v.rend());

    big m = 0, g;
    int k = N-2;
    while (k >= 0 && v[k] == v[N-1]) k--;
    if (k >= 0) {
      g = v[k] - v[N-1];
      for (int j = N-k+1; j <= N; j++) {
	big t = v[N-j] - v[N-1];
	//cout << g << "," << t << "\n";
	g = gcd(t, g);
      }
      m = bigmod(v[N-1], g);
    }
    if (m == 0)
      cout << "Case #" << i << ": 0\n";
    else
      cout << "Case #" << i << ": " << g - m << "\n";
  }
}
