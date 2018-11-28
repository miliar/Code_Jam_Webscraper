#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define fr first
#define sc second

using namespace std;

const int INF = 1000000000;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca = " << ca << endl;
    int p;
    cin >> p;
    vector<bool> t(1<<(p+1), false);
    vector<int> m(1<<p);
    for (int i = 0; i < int(m.size()); ++i) {
      cin >> m[i];
    }
    int one = 1;
    for (int i = 0; i < (1<<p)-1; ++i) {
      cin >> one;
    }
    for (int i = 0; i < int(m.size()); ++i) {
      int miss = m[i];
      for (int pos = (int(t.size())/2 + i)/2; pos >= 1; pos /= 2) {
        if (miss > 0) {
          --miss;
        }
        else {
          t[pos] = true;
        }
      }
    }
    int ans = 0;
    for (int i = 0; i < int(t.size()); ++i) {
      if (t[i]) ++ans;
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
}
