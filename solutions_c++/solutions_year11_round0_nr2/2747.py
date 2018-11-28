#include <iostream>
#include <map>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

main() {
  int T;
  cin >> T;
  for(int tc = 0; tc < T; ++tc) {
    map<pair<char, char> , char> mc;
    set<pair<char, char> > md;
    int C;
    cin >> C;
    for(int i = 0; i < C; ++i) {
      char a, b, t;
      cin >> a >> b >> t;
      if(a > b) swap(a, b);
      mc[make_pair(a, b)] = t;
    }
    int D;
    cin >> D;
    for(int i = 0; i < D; ++i) {
      char a, b;
      cin >> a >> b;
      if(a > b) swap(a, b);
      md.insert(make_pair(a, b));
    }
    int N;
    char c[2] = {'@', '@'};
    string str = "";
    cin >> N;
    for(int p = 0; p < N; c[0] = c[1], ++p) {
      cin >> c[1];
      if(c[0] == '@') continue;
      char a, b;
      map<pair<char, char> , char>::iterator it;
      a = c[0], b = c[1];
      if(a > b) swap(a, b);
      it = mc.find(make_pair(a, b));
      if(it != mc.end()) {
	c[0] = '@';
	c[1] = it->second;
	continue;
      }
      bool flag = false;
      for(int i = 0; i <= str.size(); ++i) {
	char d = i == str.size() ? c[0] : str[i];
	char e = c[1];
	if(d > e) swap(d, e);
	if(md.find(make_pair(d, e)) != md.end()) {
	  c[0] = c[1] = '@';
	  str = "";
	  flag = true;
	  break;
	}
      }
      if(flag) continue;
      str += c[0];
    }
    if(c[0] != '@') str += c[0];
    cout << "Case #" << tc+1 << ": [";
    for(int i = 0; i < str.size(); ++i) {
      if(i) cout << ", ";
      cout << str[i];
    }
    cout << "]" << endl;
  }
}
