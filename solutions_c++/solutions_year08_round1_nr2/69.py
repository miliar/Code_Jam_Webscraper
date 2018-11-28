#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

VI flav[2000];
int mflav[2000];

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<":";
    DBG(1,"CASE " << (t+1));
    int n; cin >> n;
    cin.getline(buf,sizeof buf);
    int m; cin >> m;
    cin.getline(buf,sizeof buf);
    FOR(i, m) {
      int cnt, f, v;
      cin >> cnt;
      flav[i].clear();
      mflav[i] = -1;
      FOR(j, cnt) {
	cin >> f >> v;
	if (!v) flav[i].pb(f-1);
	else mflav[i] = f-1;
      }
      cin.getline(buf,sizeof buf);
    }
    VI sol(n, 0);
    while (1) {
      int chg = 0;
      FOR(i, m) {
	if (mflav[i] >= 0 && sol[mflav[i]]) continue;
	FOR(j, flav[i].size()) if (!sol[flav[i][j]]) goto ok;
	if (mflav[i] < 0) {
	  cout << " IMPOSSIBLE"<<endl;
	  goto done;
	}
	sol[mflav[i]] = 1;
	chg = 1;
      ok: continue;
      }
      if (!chg) break;
    }
    FOR(i, n) cout << ' ' << sol[i];
    cout << endl;
  done:
    continue;
  }
  return 0;
}
