#define DBGLEVEL 0

#include "std.h"

char buf[1024*1024];

int main() {
  int T;
  cin >> T; cin.getline(buf, sizeof buf);
  FOR(t, T) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int n, k; cin >> n >> k;
    cin.getline(buf,sizeof buf);
    unsigned mod = 1u << n;
    k %= mod;
    cout << (k == mod - 1 ? "ON" : "OFF");
    cout << endl;
  }
  return 0;
}
