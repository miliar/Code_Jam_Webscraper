#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <utility>
using namespace std;

int main() {
  int T, CN = 1;
  cin >> T;
  while (T--) {
    int nc, nd, n;
    string s;
    map<pair<char, char>, char> C;
    set<pair<char, char> > D;
    cin >> nc;
    while (nc-- && cin >> s)
      C[make_pair(s[0], s[1])] = C[make_pair(s[1], s[0])] = s[2];
    cin >> nd;
    while (nd-- && cin >> s)
      D.insert(make_pair(s[0], s[1])), D.insert(make_pair(s[1], s[0]));

    cin >> n >> s;
    vector<char> V;
    for (int i = 0; i < n; ++i) {
      if (V.size() >= 1 && C.find(make_pair(s[i], V.back())) != C.end())
        V[V.size()-1] = C[make_pair(s[i], V.back())];
      else {
        bool f = false;
        for (int j = 0; !f && j < int(V.size()); ++j)
          if (D.find(make_pair(s[i], V[j])) != D.end())
            f = true;
        if (f)
          V.clear();
        else
          V.push_back(s[i]);
      }
    }
    
    cout << "Case #" << CN++ << ": [";
    for (int i = 0; i < int(V.size()); ++i)
      cout << (i ? ", " : "") << V[i];
    cout << "]" << endl;
  }
}
