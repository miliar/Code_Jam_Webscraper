#define DBGLEVEL 1

#include "std.h"

char buf[8192];

int go(VS& s, VS& q) {
  int n = s.size();
  map<string, int> res;
  FOR(qi, q.size()) {
    FOR(i, n) if (s[i] != q[qi]) res[s[i]] <?= res[q[qi]] + 1;
    res[q[qi]] = 9999;
  }
  int ret = 9999;
  FOR(i, n) ret <?= res[s[i]];
  return ret;
}

int main() {
  int N;
  cin >> N; cin.getline(buf, sizeof buf);
  FOR(t, N) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int S; cin >> S; 
    cin.getline(buf,sizeof buf);
    VS s;
    FOR(i, S) {
      cin.getline(buf,sizeof buf);
      s.pb(buf);
    }
    int Q; cin >> Q;
    cin.getline(buf,sizeof buf);
    VS q;
    FOR(i, Q) {
      cin.getline(buf,sizeof buf);
      q.pb(buf);
    }
    int r = go(s, q);
    cout << r;
    cout << endl;
  }
  return 0;
}
