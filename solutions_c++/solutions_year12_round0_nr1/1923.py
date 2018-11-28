// Michael Lawrence,
// DATE

#include <iostream>
#include <map>

using namespace std;

int main(int argc, const char* argv[]) {
  int n_cases;
  cin >> n_cases;

  map<char, char> inverse_charmap;
  inverse_charmap['a'] = 'y';
  inverse_charmap['b'] = 'h';
  inverse_charmap['c'] = 'e';
  inverse_charmap['d'] = 's';
  inverse_charmap['e'] = 'o';
  inverse_charmap['f'] = 'c';
  inverse_charmap['g'] = 'v';
  inverse_charmap['h'] = 'x';
  inverse_charmap['i'] = 'd';
  inverse_charmap['j'] = 'u';
  inverse_charmap['k'] = 'i';
  inverse_charmap['l'] = 'g';
  inverse_charmap['m'] = 'l';
  inverse_charmap['n'] = 'b';
  inverse_charmap['o'] = 'k';
  inverse_charmap['p'] = 'r';
  inverse_charmap['q'] = 'z';
  inverse_charmap['r'] = 't';
  inverse_charmap['s'] = 'n';
  inverse_charmap['t'] = 'w';
  inverse_charmap['u'] = 'j';
  inverse_charmap['v'] = 'p';
  inverse_charmap['w'] = 'f';
  inverse_charmap['x'] = 'm';
  inverse_charmap['y'] = 'a';
  inverse_charmap['z'] = 'q';

  char line[101];
  cin.getline(line, 101);

  for (int i = 0; i < n_cases; ++i) {
    cin.getline(line, 101);

    for (int j = 0; j < 101 && line[j] != 0; j++) {
      if (line[j] != ' ') {
        line[j] = inverse_charmap[line[j]];
      }
    }

    cout << "Case #" << i+1 << ": " << line << endl;
  }
  return 0;
}
