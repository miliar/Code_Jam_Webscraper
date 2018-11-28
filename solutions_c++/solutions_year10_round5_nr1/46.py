#include <cstdio>
#include <cassert>
#include <set>
using namespace std;

inline int mod(long long x, int p)
{
  return (x%p+p)%p;
}

inline bool prime(int x)
{
  if (x == 2) return true;
  if (x % 2 == 0) return false;
  int d = 3;
  while (d*d <= x) {
    if (x % d == 0) return false;
    d += 2;
  }
  return true;
}

typedef long long ll;

inline void ext_euclid(ll a, ll b, ll& p, ll& q, ll& d)
{
  if (a == 0) {
    d = b;
    p = 0;
    q = 1;
  } else if (b == 0) {
    d = a;
    p = 1;
    q = 0;
  } else {
    ext_euclid(b % a, a, p, q, d);
    ll tmp = p;
    p = q - (b / a) * p;
    q = tmp;
  }
}

int inv(int a, int p)
{
  a = mod(a, p);
  ll x, y, z;
  ext_euclid(a, p, x, y, z);
  assert(z == 1);
  assert(mod(a*x, p) == 1);
  return mod(x, p);
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int case_ = 1; case_ <= T; case_++) {
    int d, k;
    scanf("%d %d", &d, &k);
    int n = 1;
    for (int i = 0; i < d; i++) n *= 10;
    long long tab[42];
    long long M = 0;
    for (int i = 0; i < k; i++) {
      scanf("%lld", &tab[i]);
      M = max(M, tab[i]);
    }
    set<int> next;
    if (k > 2) {
      for (int P = M+1; P <= n; P++) {
        if (!prime(P)) continue;
        int A;
        if (tab[0] == tab[1]) A = 0;
        else A = mod((tab[2]-tab[1])*inv(tab[1]-tab[0], P), P);
        int B = mod(tab[1] - tab[0]*A, P);
        assert(mod(A*tab[0] + B, P) == tab[1]);
        assert(mod(A*tab[1] + B, P) == tab[2]);
        bool ok = true;
        for (int i = 1; i < k; i++) {
          int x = mod(A*tab[i-1] + B, P);
          if (tab[i] != x) {
            ok = false;
            break;
          }
        }
        if (ok) next.insert(mod(tab[k-1]*A + B, P));
      }
    } else if (tab[0] == tab[1]) {
      next.insert(tab[0]);
    }
    printf("Case #%d: ", case_);
    if (next.size() == 1) printf("%d\n", *next.begin());
    else printf("I don't know.\n");
  }
}
