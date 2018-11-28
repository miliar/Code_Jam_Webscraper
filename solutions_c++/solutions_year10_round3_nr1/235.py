#include <iostream>
#include <cmath>
#include <string>
#include <list>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>

using namespace std;

#define FOR_EACH(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).begin(), (container).end())

#define FOR_EACH_R(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).rbegin(), (container).rend())

#define FOR_EACH_RANGE(it_var, begin, end) \
  for (typeof(begin) it_var = (begin); it_var != (end); ++it_var)

void zmain() {
  int n; cin >> n;
  vector<pair<int, int> > V, V2;
  for (int i=0;i<n;++i) {
    int a, b; cin >> a >> b;
    V.push_back(make_pair(a, b));
  }
  sort(V.begin(), V.end());
  for (int i=0;i<n;++i) {
    V2.push_back(make_pair(V[i].second, i));
  }
  int s = 0;
  sort(V2.begin(), V2.end());
  for (int i=0;i<n;++i) {
    s += std::abs(V2[i].second - i);
  }
  s /= 2;
  cout << s;
}

int main() {
  int k; cin >> k;
  for (int i=0;i<k;++i) {
    cout << "Case #" << (i+1) << ": ";
    zmain();
    cout << "\n";
  }
}
