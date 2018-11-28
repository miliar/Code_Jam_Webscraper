#include <iostream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>

using namespace std;

map<char, char> mpp;

void func()
{
  mpp[' '] = ' ';
  mpp['a'] = 'y';
  mpp['b'] = 'h';
  mpp['c'] = 'e';
  mpp['d'] = 's';
  mpp['e'] = 'o';
  mpp['f'] = 'c';
  mpp['g'] = 'v';
  mpp['h'] = 'x';
  mpp['i'] = 'd';
  mpp['j'] = 'u';
  mpp['k'] = 'i';
  mpp['l'] = 'g';
  mpp['m'] = 'l';
  mpp['n'] = 'b';
  mpp['o'] = 'k';
  mpp['p'] = 'r';
  mpp['q'] = 'z';
  mpp['r'] = 't';
  mpp['s'] = 'n';
  mpp['t'] = 'w';
  mpp['u'] = 'j';
  mpp['v'] = 'p';
  mpp['w'] = 'f';
  mpp['x'] = 'm';
  mpp['y'] = 'a';
  mpp['z'] = 'q';
}

int main()
{
  int n;
  string str;

  func();
  while(getline(cin, str)){
    n = atoi(str.c_str());
    for(int cs = 1; cs <= n; ++cs){
      getline(cin, str);

      cout << "Case #" << cs << ": ";
      for(int i = 0; i < str.size(); ++i)
	cout << mpp[str[i]];
      cout << endl;
    }
  }

  return 0;
}
