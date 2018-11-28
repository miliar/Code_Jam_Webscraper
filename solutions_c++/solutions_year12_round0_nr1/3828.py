#include <iostream>
#include <string>
using namespace std;

char map[26];
int main() {
  map['a'-'a'] = 'y';
  map['b'-'a'] = 'h';
  map['c'-'a'] = 'e';
  map['d'-'a'] = 's';
  map['e'-'a'] = 'o';
  map['f'-'a'] = 'c';
  map['g'-'a'] = 'v';
  map['h'-'a'] = 'x';
  map['i'-'a'] = 'd';
  map['j'-'a'] = 'u';
  map['k'-'a'] = 'i';
  map['l'-'a'] = 'g';
  map['m'-'a'] = 'l';
  map['n'-'a'] = 'b';
  map['o'-'a'] = 'k';
  map['p'-'a'] = 'r';
  map['q'-'a'] = 'z';
  map['r'-'a'] = 't';
  map['s'-'a'] = 'n';
  map['t'-'a'] = 'w';
  map['u'-'a'] = 'j';
  map['v'-'a'] = 'p';
  map['w'-'a'] = 'f';
  map['x'-'a'] = 'm';
  map['y'-'a'] = 'a';
  map['z'-'a'] = 'q';

  int ct; cin>>ct; string s; getline(cin, s);
  for (int i = 1; i <= ct; ++i) {
    getline(cin, s);
    for (int j = 0; j < s.length(); ++j) {
      if (s[j] == ' ') continue;
      s[j] = map[s[j]-'a'];
    }
    cout << "Case #" << i << ": " << s << endl;
  }
}
