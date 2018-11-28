#include <iostream>
#include <string>

using namespace std;

int main() {
  char map[300];
  map['a'] = 'y';
  map['b'] = 'h';
  map['c'] = 'e';
  map['d'] = 's';
  map['e'] = 'o';
  map['f'] = 'c';
  map['g'] = 'v';
  map['h'] = 'x';
  map['i'] = 'd';
  map['j'] = 'u';
  map['k'] = 'i';
  map['l'] = 'g';
  map['m'] = 'l';
  map['n'] = 'b';
  map['o'] = 'k';
  map['p'] = 'r';
  map['q'] = 'z';
  map['r'] = 't';
  map['s'] = 'n';
  map['t'] = 'w';
  map['u'] = 'j';
  map['v'] = 'p';
  map['w'] = 'f';
  map['x'] = 'm';
  map['y'] = 'a';
  map['z'] = 'q';

  int N;
  cin >> N;
  string f;
  getline(cin, f);

  string a, b;
  for (int X = 0; X < N; X++) {
    getline(cin, a);
    cout << "Case #" << (X+1) << ": ";
    for (int y = 0; y < a.length(); y++) {
      if (a[y] == ' ') {
        cout << ' ';
        continue;
      }
      cout << map[a[y]];
    }
    cout << endl;
  }

  return 0;
}
