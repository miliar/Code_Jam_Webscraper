#include <algorithm>
#include <cstdio>

using namespace std;

typedef long long ll;

const int kMaxK = 20;
const int kMaxPrime = 1000000 + 10;

int D, K;
ll s[kMaxK];

int di[kMaxPrime];

int pn;
ll prime[kMaxPrime];
int check[kMaxPrime];

void Init() {
  for (int d = 1, top = 10, i = 1; d <= 6; ++d, top *= 10)
    for (; i < kMaxPrime && i < top; ++i) di[i] = d;
}

void MakePrimeTable() {
  ll i;
  pn = 0;
  for (i = 2; i * i < kMaxPrime; ++i)
    if (check[i] == 0) {
      prime[pn++] = i;
      for (ll j = i * i; j < kMaxPrime; j += i)
        check[j] = 1;
    }
  for (; i < kMaxPrime; ++i)
    if (check[i] == 0)
      prime[pn++] = i;
}

ll Mod(ll a, ll P) {
  return (a % P + P) % P;
}

ll Inv(ll a, ll P) {
  if (a == 1) return 1;
  ll t = Inv(P % a, a);
  return (1 - t * P) / a;
}

ll GetA(ll P, ll s1, ll s2, ll s3) {
  if (s2 == s3) return 0;
  ll re = Inv(Mod(s1 - s2, P), P) * (s2 - s3);
  re %= P;
  if (re < 0) re += P;
  return re;
}

ll GetB(ll P, ll A, ll s1, ll s2) {
  ll re = (s2 - A * s1) % P;
  if (re < 0) re += P;
  return re;
}

bool TestP(ll P, ll& A, ll &B) {
  for (int i = 0; i < K; ++i)
    if (P <= s[i])
      return false;
  A = GetA(P, s[0], s[1], s[2]);
  for (int i = 1; i < K - 2; ++i) {
    ll t = GetA(P, s[i], s[i + 1], s[i + 2]);
    if (t != A) return false;
  }
  B = GetB(P, A, s[0], s[1]);
  for (int i = 1; i < K - 1; ++i) {
    ll t = GetB(P, A, s[i], s[i + 1]);
    if (t != B) return false;
  }
  return true;
}

ll Solve() {
  ll re = -1;
  ll A, B;
  if (K == 1) return -1;
  if (K == 2) {
    if (s[0] == s[1]) return s[0];
    else return -1;
  }
  for (int i = 0; i < pn && di[prime[i]] <= D; ++i) {
    //printf("%lld\n", prime[i]);
    if (TestP(prime[i], A, B)) {
      ll t = (A * s[K - 1] + B) % prime[i];
      if (re != -1 && t != re) return -1;
      else re = t;
    }
  }
  return re;
}

int main() {
  Init();
  MakePrimeTable();
  int cases;
  scanf("%d", &cases);
  for (int e = 1; e <= cases; ++e) {
    printf("Case #%d: ", e);
    scanf("%d %d", &D, &K);
    for (int i = 0; i < K; ++i)
      scanf("%lld", s + i);
    ll re = Solve();
    if (re == -1) {
      printf("I don't know.\n");
    } else {
      printf("%lld\n", re);
    }
  }
  return 0;
}
