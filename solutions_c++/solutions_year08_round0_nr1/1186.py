#include <iostream>
#include <string>
#include <vector>
#include <set>
using namespace std;

int main() {
  int casos;
  cin >> casos;
  for (int k=0; k<casos; ++k) {
    cout << "Case #" << k+1 << ": ";
    set<string> ciutats;
    int n;
    cin >> n;
    string ss; getline(cin, ss);
    while (n--) {
      string s;
      getline(cin, s);
      ciutats.insert(s);
    }
    cin >> n;
    getline(cin, ss);
    vector<string> v(n);
    for (int i=0; i<n; ++i)
      getline(cin, v[i]);
    set<string> queden = ciutats;
    int i = 0;
    int sol = 0;
    while (i < n) {
      if (queden.find(v[i]) != queden.end()) {
        if (queden.size() == 1) {
          ++sol;
          queden = ciutats;
          --i;
        }
        else queden.erase(v[i]);
      }
      ++i;
    }
    cout << sol << endl;
  }
}
