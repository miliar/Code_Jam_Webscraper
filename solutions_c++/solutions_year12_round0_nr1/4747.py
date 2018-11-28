#include <iostream>
#include <string>

using namespace std;

int main(void)
{
  char ans[256];
  ans['a'] = 'y';
  ans['b'] = 'h';
  ans['c'] = 'e';
  ans['d'] = 's';
  ans['e'] = 'o';
  ans['f'] = 'c';
  ans['g'] = 'v';
  ans['h'] = 'x';
  ans['i'] = 'd';
  ans['j'] = 'u';
  ans['k'] = 'i';
  ans['l'] = 'g';
  ans['m'] = 'l';
  ans['n'] = 'b';
  ans['o'] = 'k';
  ans['p'] = 'r';
  ans['q'] = 'z';
  ans['r'] = 't';
  ans['s'] = 'n';
  ans['t'] = 'w';
  ans['u'] = 'j';
  ans['v'] = 'p';
  ans['w'] = 'f';
  ans['x'] = 'm';
  ans['y'] = 'a';
  ans['z'] = 'q';
  ans[' '] = ' ';
  int q;
  cin >> q;
  string _;
  getline(cin, _);
  for (int i = 0; i < q; ++i)
  {
    string s;
    getline(cin, s);
    for (int j = 0; j < (int)s.size(); ++j)
    {
      s[j] = ans[s[j]];
    }
    cout << "Case #" << i + 1 << ": " << s << endl;
  }
  return 0;
}
