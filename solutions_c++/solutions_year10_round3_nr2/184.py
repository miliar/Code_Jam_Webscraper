#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <inttypes.h>
#include <map>

using namespace std;

#define FOR_EACH(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).begin(), (container).end())

#define FOR_EACH_R(it_var, container) \
  FOR_EACH_RANGE(it_var, (container).rbegin(), (container).rend())

#define FOR_EACH_RANGE(it_var, begin, end) \
  for (typeof(begin) it_var = (begin); it_var != (end); ++it_var)

void zmain() {
  vector<int64_t> a, b;
  int64_t L, P, C; cin >> L >> P >> C;
  int64_t x = L * C;
  int64_t res = 0;
  int t = 0;
  while (x < P) {
    a.push_back(x);
    ++t;
    x *= C;
  }
  while (t >= 1) {
    res++;
    t >>= 1;
  }
  cout << res;
}

int main() {
  int k; cin >> k;
  for (int i=0;i<k;++i) {
    cout << "Case #" << (i+1) << ": ";
    zmain();
    cout << "\n";
  }
}
