#include <iostream>
#include <sstream>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;


map<char, char> m;

void translate(char c) {
  cout << m[c];
}


int main() {
  int t = 0, i;
  char c;

  m['y'] = 'a';
  m['n'] = 'b';
  m['f'] = 'c';
  m['i'] = 'd';
  m['c'] = 'e';
  m['w'] = 'f';
  m['l'] = 'g';
  m['b'] = 'h';
  m['k'] = 'i';
  m['u'] = 'j';
  m['o'] = 'k';
  m['m'] = 'l';
  m['x'] = 'm';
  m['s'] = 'n';
  m['e'] = 'o';
  m['v'] = 'p';
  m['z'] = 'q';
  m['p'] = 'r';
  m['d'] = 's';
  m['r'] = 't';
  m['j'] = 'u';
  m['g'] = 'v';
  m['t'] = 'w';
  m['h'] = 'x';
  m['a'] = 'y';
  m['q'] = 'z';
  m[' '] = ' ';

  cin >> t;getchar();

  for (i=0;i<t;i++) {
    string line;
    getline(cin, line);
    cout << "Case #" << i+1 << ": ";
    for_each(line.begin(), line.end(), translate);
    cout << endl;
  }
  return 0;
}
