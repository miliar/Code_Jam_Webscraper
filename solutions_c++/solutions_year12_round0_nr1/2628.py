#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string GOO = "ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv q z";

const string ENG = "our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up z q";

int main() {
  vector<char> tra(128, '?');
  for (int i = 0; i < int(GOO.size()); ++i) {
    tra[GOO[i]] = ENG[i];
  }
  int T;
  cin >> T;
  string s;
  getline(cin, s);
  for (int ca = 1; ca <= T; ++ca) {
    getline(cin, s);
    cout << "Case #" << ca << ": ";
    for (int i = 0; i < int(s.size()); ++i) {
      cout << tra[s[i]];
    }
    cout << endl;
  }
}
