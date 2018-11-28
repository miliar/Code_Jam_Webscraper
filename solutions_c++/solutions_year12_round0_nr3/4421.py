#include <set>
#include <map>
#include <sstream>
#include <iostream>

using namespace std;

inline int str2int(string s) {
  stringstream ss(s);
  int b;
  ss >> b;
  return b;
}

inline string int2str(int n) {
  stringstream ss;
  ss << n;
  return ss.str();
}

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    int A, B;
    cin >> A >> B;
    set<pair<int, int> > s;
    for (int i = A; i <= B; ++i) {
      string ns = int2str(i);
      string ms = ns;
      do {
        rotate(ms.begin(), ms.begin() + 1, ms.end());
        if (ms[0] == '0') continue;
        int m = str2int(ms);
        if (m <= B && m > i) s.insert(make_pair(i, m));
      } while (ms != ns);
    }
    printf("Case #%d: %ld\n", t, s.size());
  }
}
