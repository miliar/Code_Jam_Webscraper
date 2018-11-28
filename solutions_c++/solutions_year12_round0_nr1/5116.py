#include <iostream>
#include <string>
#include <map>
#include <set>
using namespace std;

map<char, char> m;
set<char> used;

void init() {
  string in =
    "yeq"
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string out =
    "aoz"
    "our language is impossible to understand"
    "there are twenty six factorial possibilities"
    "so it is okay if you want to just give up";
  for (int i = 0; i < in.length(); ++i) {
    m[in[i]] = out[i];
    used.insert(out[i]);
  }
  char unused;
  for (char ch = 'a'; ch <= 'z'; ++ch) {
    if (used.find(ch) == used.end()) {
      unused = ch;
      break;
    }
  }
  for (char ch = 'a'; ch <= 'z'; ++ch) {
    if (m.find(ch) == m.end()) {
      m[ch] = unused;
      cerr << ch << " -> " << unused << endl;
      break;
    }
  }
  for (char ch = 'a'; ch <= 'z'; ++ch) {
    cerr << ch << " -> " << m[ch] << endl;
  }
  //cerr << m.size() << endl;
}

int main() {
  init();
  int t;
  string s;
  cin >> t;
  getline(cin, s);
  for (int i = 1; i <= t; ++i) {
    getline(cin, s);
    for (int j = 0; j < s.length(); ++j) {
      if (s[j] >= 'a' && s[j] <= 'z') {
        s[j] = m[s[j]];
      } else if (s[j] != ' ') {
        cerr << "invalid char " << s[j];
      }
    }
    cout << "Case #" << i << ": " << s << endl;
  }
}
