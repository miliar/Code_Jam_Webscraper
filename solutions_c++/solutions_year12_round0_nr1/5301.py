#include <string>
#include <iostream>
#include <cassert>
using namespace std;

string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv yeqz";
string b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up aozq";

string m(26, '.');

int main(int argc, char* argv[]) {
  for (int i = 0; i < a.length(); ++i) {
    if (a[i] == ' ') continue;
    const int j = a[i] - 'a';
    if (m[j] != '.' &&  m[j] != b[i]) cout << i << " " << a[i] << " " << m[j] << " " << b[i] << endl;
    m[j] = b[i];
  }
  // cout << m << endl;
  int N; cin >> N >> ws;
  for (int t = 1; t <= N; ++t) {
    string s;
    getline(cin, s);
    string o;
    for (int i = 0; i < s.length(); ++i)
      o += s[i] != ' ' ? m[s[i] - 'a'] : ' ';
    cout << "Case #" << t << ": " << o << endl;
  }
  return 0;
}