#include <map>
#include <iostream>
#include <string>

using namespace std;

int main() {
  int T; cin >> T;
  char m[256];
  m['a'] = 'y';
  m['b'] = 'h';
  m['c'] = 'e';
  m['d'] = 's';
  m['e'] = 'o';
  m['f'] = 'c';
  m['g'] = 'v';
  m['h'] = 'x';
  m['i'] = 'd';
  m['j'] = 'u';
  m['k'] = 'i';
  m['l'] = 'g';
  m['m'] = 'l';
  m['n'] = 'b';
  m['o'] = 'k';
  m['p'] = 'r';
  m['q'] = 'z';
  m['r'] = 't';
  m['s'] = 'n';
  m['t'] = 'w';
  m['u'] = 'j';
  m['v'] = 'p';
  m['w'] = 'f';
  m['x'] = 'm';
  m['y'] = 'a';
  m['z'] = 'q';
  m[' '] = ' ';

  cin.ignore();
  for (int tc = 1; tc <= T; ++tc) {
    string s;
    getline(cin, s);
    cout << "Case #" << tc << ": ";
    for(int i = 0; i < s.size(); ++i) {
      cout << m[s[i]];
    }
    cout << endl;
  }
  return 0;
}
