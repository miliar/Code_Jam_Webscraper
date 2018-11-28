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

#define FR first
#define SC second

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
    int n;
    cin >> n;
    vector<pair<int, int> > v(n);
    for (int i = 0; i < n; ++i) {
      cin >> v[i].FR >> v[i].SC; // dist, length
    }
    //sort(v.begin(), v.end());
    int D;
    cin >> D;
    v.push_back(pair<int, int>(D, 0));
    ++n;
    vector<int> swing(n, -1);
    swing[0] = v[0].FR;
    for (int i = 0; i < n; ++i) {
      for (int j = i+1; j < n && v[j].FR <= v[i].FR+swing[i]; ++j) {
        swing[j] = max(swing[j], min(v[j].FR-v[i].FR, v[j].SC));
      }
    }
    cout << "Case #" << ca << ": ";
    if (swing[n-1] < 0) {
      cout << "NO" << endl;
    }
    else {
      cout << "YES" << endl;
    }
  }
}
