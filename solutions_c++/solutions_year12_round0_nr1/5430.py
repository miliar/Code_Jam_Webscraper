#include <cstdio>
#include <cstring>
#include <map>
#include <iostream>

using namespace std;

int main()
{
  map <char, char> alphabet;

  alphabet['a'] = 'y';
  alphabet['b'] = 'h';
  alphabet['c'] = 'e';
  alphabet['d'] = 's';
  alphabet['e'] = 'o';
  alphabet['f'] = 'c';
  alphabet['g'] = 'v';
  alphabet['h'] = 'x';
  alphabet['i'] = 'd';
  alphabet['j'] = 'u';
  alphabet['k'] = 'i';
  alphabet['l'] = 'g';
  alphabet['m'] = 'l';
  alphabet['n'] = 'b';
  alphabet['o'] = 'k';
  alphabet['p'] = 'r';
  alphabet['q'] = 'z';
  alphabet['r'] = 't';
  alphabet['s'] = 'n';
  alphabet['t'] = 'w';
  alphabet['u'] = 'j';
  alphabet['v'] = 'p';
  alphabet['w'] = 'f';
  alphabet['x'] = 'm';
  alphabet['y'] = 'a';
  alphabet['z'] = 'q';

  int test_cases;
  cin >> test_cases;
  getchar();
  for (int i = 1; i <= test_cases; ++i) {
    cout << "Case #" << i << ": ";
    char line[102];
    gets(line);
    for (int j = 0; j < strlen(line); ++j) {
      if (line[j] >= 'a' && line[j] <= 'z')
        cout << alphabet[line[j]];
      else
        cout << line[j];
    }
    cout << endl;
  }

  return 0;
}
