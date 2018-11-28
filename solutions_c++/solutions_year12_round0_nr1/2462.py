#include <iostream>
#include <map>
#include <string>

using namespace std;

map<char, char> get_map() {
  map<char, char> mab, mba;
  string a = "yeq" 
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string b = "aoz" 
    "our language is impossible to understand"
    "there are twenty six factorial possibilities"
    "so it is okay if you want to just give up";
  for (int i = 0; i < a.size(); ++i) {
    mab[a[i]] = b[i];
    mba[b[i]] = a[i];
  }
  for (char ca = 'a'; ca <= 'z'; ++ca)
    for (char cb = 'a'; cb <= 'z'; ++cb)
      if (!mab.count(ca) && !mba.count(cb)) {
        mab[ca] = cb;
        mba[cb] = ca;
      }
  return mab;
}

int main(void) {
  ios::sync_with_stdio(false);
  map<char, char> m = get_map(); 
  int t; 
  cin >> t; cin.ignore();
  for (int i = 1; i <= t; ++i) {
    string s;
    getline(cin, s);
    for (int j = 0; j < s.size(); ++j)
      s[j] = m[s[j]];
    cout << "Case #" << i << ": " << s << '\n';
  }
  return 0;
}
