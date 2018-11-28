#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

int g[1000];

int turn[1000];
int riders[1000];

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int n, k, b, t; cin >> n >> k >> b >> t;
    cin.getline(buf,sizeof buf);
    VI x(n), v(n);
    FOR(i, n) cin >> x[i];
    cin.getline(buf,sizeof buf);
    FOR(i, n) cin >> v[i];
    cin.getline(buf,sizeof buf);
    VI ok(n);
    FOR(i, n) ok[i] = x[i] + t * v[i] >= b;
    DBG(1,V(ok));
    int bad = 0, good = 0, swap = 0;
    for (int i = n-1; i >= 0 && good < k; i--) {
	if (ok[i]) swap += bad, good++;
	else bad++;
	DBG(1, V(i)<<V(swap)<<V(bad)<<V(good));
    }
    if (good < k) cout << "IMPOSSIBLE";
    else cout << swap;
    cout << endl;
  }
  return 0;
}
