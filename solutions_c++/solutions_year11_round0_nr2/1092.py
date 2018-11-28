#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    int c, d;
    map<string, string> combine;
    cin >> c;
    for (int i = 0; i < c; ++i) {
      string s;
      cin >> s;
      combine[s.substr(0, 2)] = s.substr(2);
      combine[s.substr(1, 1)+s.substr(0, 1)] = s.substr(2);
    }
    set<string> opposed;
    cin >> d;
    for (int i = 0; i < d; ++i) {
      string s;
      cin >> s;
      opposed.insert(s);
      opposed.insert(s.substr(1)+s.substr(0, 1));
    }
    int n;
    cin >> n;
    string res = "";
    for (int i = 0; i < n; ++i) {
      char e;
      cin >> e;
      res += e;
      while (res.size() > 1 && combine.count(res.substr(int(res.size())-2)) > 0) {
        res.replace(int(res.size())-2, 2, combine[res.substr(int(res.size())-2)]);
      }
      for (int i = 0; i < int(res.size())-1; ++i) {
        if (opposed.count(res.substr(i, 1)+res.substr(int(res.size())-1)) > 0) {
          res = "";
        }
      }
    }
    cout << "Case #" << ca << ": [";
    for (int i = 0; i < int(res.size()); ++i) {
      if (i > 0) cout << ", ";
      cout << res[i];
    }
    cout << "]" << endl;
  }
}
