#define DBGLEVEL 1

#include "std.h"

char buf[1024*1024];

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int n; cin >> n;
    cin.getline(buf,sizeof buf);
    VI v1(n), v2(n);
    FOR(i, n) cin >> v1[i];
    cin.getline(buf,sizeof buf);
    FOR(i, n) cin >> v2[i];
    cin.getline(buf,sizeof buf);
    sort(v1);
    sort(v2);
    LL r = 0;
    FOR(i, n) r += LL(v1[i]) * v2[n-1-i];
    cout << r;
    cout << endl;
  }
  return 0;
}
