#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
  map<char, char> char_to_char;

  char_to_char['a'] = 'y';
  char_to_char['b'] = 'h';
  char_to_char['c'] = 'e';
  char_to_char['d'] = 's';
  char_to_char['e'] = 'o';
  char_to_char['f'] = 'c';
  char_to_char['g'] = 'v';
  char_to_char['h'] = 'x';
  char_to_char['i'] = 'd';
  char_to_char['j'] = 'u';
  char_to_char['k'] = 'i';
  char_to_char['l'] = 'g';
  char_to_char['m'] = 'l';
  char_to_char['n'] = 'b';
  char_to_char['o'] = 'k';
  char_to_char['p'] = 'r';
  char_to_char['q'] = 'z';
  char_to_char['r'] = 't';
  char_to_char['s'] = 'n';
  char_to_char['t'] = 'w';
  char_to_char['u'] = 'j';
  char_to_char['v'] = 'p';
  char_to_char['w'] = 'f';
  char_to_char['x'] = 'm';
  char_to_char['y'] = 'a';
  char_to_char['z'] = 'q';
  char_to_char[' '] = ' ';

  int n, count = 0;
  cin >> n;
  cin.ignore(1);

  while (n--) {
    ++count;

    string input;
    getline(cin, input);

    cout << "Case #" << count << ": ";

    for (int i = 0; i < input.size(); ++i)
      cout << char_to_char[input[i]];

    cout << endl;
  }

  return 0;
}
