#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int nt;
  cin >> nt;
  for (int tt = 1; tt <= nt; tt++) {
    cout << "Case #" << tt << ": ";
    int n;
    cin >> n;
    vector <int> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    sort(a.begin(), a.end());
    vector <int> b, c;
    for (int i = 0; i < n; i++) {
      if (i == 0 || a[i] != a[i - 1]) {
        b.push_back(a[i]);
        c.push_back(1);
      } else {
        c[c.size() - 1]++;
      }
    }
    vector <int> cur;
    int ans = n;
    for (int i = 0; i < (int)b.size(); i++) {
      if (i == 0 || b[i] != b[i - 1] + 1) {
        for (int j = 0; j < (int)cur.size(); j++) {
          ans = min(ans, cur[j]);
        }
        cur.resize(0);
      }
      int cnt = min((int)cur.size(), c[i]);
      for (int j = 0; j < cnt; j++) {
        cur[j]++;
      }
      int tok = (int)cur.size() - cnt;
      for (int j = 0; j < tok; j++) {
        ans = min(ans, cur[cur.size() - 1]);
        cur.pop_back();
      }
      int toa = c[i] - cnt;
      for (int j = 0; j < toa; j++) {
        cur.push_back(1);
      }
      sort(cur.begin(), cur.end());
    }
    for (int i = 0; i < (int)cur.size(); i++) {
      ans = min(ans, cur[i]);
    }
    cout << ans << endl;
  }
  return 0;
}

