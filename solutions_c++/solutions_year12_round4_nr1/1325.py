#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int N = 10000;

int D, n;
int d[N];
int l[N];
map<pair<int, int>, bool> m;

bool go(int idx, int span) {
  if (d[idx] + span >= D) return true;
  pair<int, int> key = make_pair(idx, span);
  if (m.find(key) != m.end()) return m[key];
  for (int i = idx+1; i < n; i++) {
    if (d[idx] + span < d[i]) break;
    if (go(i, min(l[i], d[i]-d[idx]))) return m[key] = true;
  }
  return m[key] = false;
}

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    m.clear();
    cin >> n;
    for (int i = 0; i < n; i++) cin >> d[i] >> l[i];
    cin >> D;
    cout << "Case #" << tt << ": " << (go(0, d[0]) ? "YES" : "NO") << endl;
  }
  return 0;
}
    
