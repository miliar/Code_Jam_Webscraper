#include <iostream>
using namespace std;
typedef long long ll;
const ll llinf = (1LL<<60);

ll sz, n, G[1010];
int S[1010];

ll cycle(ll p, ll &e) {
  memset(S, 0, sizeof S);
  ll k = 0;
  while (!S[p]) {
    S[p] = 1;
    if (G[p] > sz)
      return llinf;
    ++k;
    ll sp = p, s = G[p];
    while ((p+1)%n != sp && s+G[(p+1)%n] <= sz)
      s += G[(p+1)%n], p = (p+1)%n;
    
    p = (p+1)%n;
  }
  e = p;
  return k;
}

ll run(ll p, ll k) {
  ll m = 0;
  for (ll i = 0; i < k; ++i) {
    if (G[p] > sz)
      break;
    ll sp = p, s = G[p];
    while ((p+1)%n != sp && s+G[(p+1)%n] <= sz)
      s += G[(p+1)%n], p = (p+1)%n;
    m += s;
    p = (p+1)%n;
  }
  return m;
}

int main() {
  int nt, C = 1;
  cin >> nt;
  ll nr;
  while (nt-- && cin >> nr >> sz >> n) {
    for (int i = 0; i < n; ++i)
      cin >> G[i];

    ll m;
    ll e, f;
    ll tcsz = cycle(0, e);
    if (tcsz < llinf) {
      ll csz = cycle(e, f);
      ll tsz = tcsz - csz;
      
      if (nr < tsz)
	m = run(0, nr);
      else
	nr -= tsz, m = run(0, tsz) + run(e, csz) * (nr/csz) + run(e, nr % csz);
    } else
      m = run(0, nr);

    cout << "Case #" << C++ << ": " << m << endl;
  }
}
