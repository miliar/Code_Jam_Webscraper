#define DBGLEVEL 1

#include "std.h"

char buf[8192];

int main() {
  int N;
  cin >> N; cin.getline(buf, sizeof buf);
  FOR(t, N) {
    cout << "Case #"<<(t+1)<<": ";
    DBG(1,"CASE " << (t+1));
    int T; cin >> T;
    cin.getline(buf,sizeof buf);
    int na, nb;
    cin >> na >> nb;
    cin.getline(buf,sizeof buf);
    VI arra, depa, arrb, depb;
    int h, m; char c;
    FOR(i, na) {
      cin >> h >> c >> m;
      depa.pb(h*60+m);
      cin >> h >> c >> m;
      arrb.pb(h*60+m+T);
      cin.getline(buf,sizeof buf);
    }
    FOR(i, nb) {
      cin >> h >> c >> m;
      depb.pb(h*60+m);
      cin >> h >> c >> m;
      arra.pb(h*60+m+T);
      cin.getline(buf,sizeof buf);
    }
    sort(depa); sort(depb); sort(arra); sort(arrb);
    int reta = 0, retb = 0;
    int inv = 0;
    for(int i = 0, j = 0; i < depa.size(); i++) {
      int t = depa[i];
      while (j < arra.size() && arra[j] <= t) inv++, j++;
      if (!inv) inv++, reta++;
      inv--;
    }
    inv = 0;
    for(int i = 0, j = 0; i < depb.size(); i++) {
      int t = depb[i];
      while (j < arrb.size() && arrb[j] <= t) inv++, j++;
      if (!inv) inv++, retb++;
      inv--;
    }
    cout << reta << ' ' << retb;
    cout << endl;
  }
  return 0;
}
