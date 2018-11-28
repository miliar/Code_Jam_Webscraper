#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
using namespace std;
int main() {
  int T; cin>>T;
  cin.ignore();

  for (int t = 1 ; t <= T ; ++t) {
    string s;
    getline(cin,s);
    string u = s;
    string res;
    if (next_permutation(u.begin(), u.end())) {
      res = u;
    } else {
      char smallest = '9';
      for (int i = 0 ; i < s.size() ; i++) {
	if (s[i] == '0') continue;
	smallest = min(smallest, s[i]);
      }
      int pos = s.find(smallest);
      s = s.replace(pos, 1, "");
      sort(s.begin(), s.end());
      res += smallest;
      res += "0";
      res += s;
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  
}
