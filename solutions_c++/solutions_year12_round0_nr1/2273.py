#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){
  map < char, char > mp;
  mp[' '] = ' ';
  mp['a'] = 'y';
  mp['b'] = 'h';
  mp['c'] = 'e';
  mp['d'] = 's';
  mp['e'] = 'o';
  mp['f'] = 'c';
  mp['g'] = 'v';
  mp['h'] = 'x';
  mp['i'] = 'd';
  mp['j'] = 'u';
  mp['k'] = 'i';
  mp['l'] = 'g';
  mp['m'] = 'l';
  mp['n'] = 'b';
  mp['o'] = 'k';
  mp['p'] = 'r';
  mp['q'] = 'z';
  mp['r'] = 't';
  mp['s'] = 'n';
  mp['t'] = 'w';
  mp['u'] = 'j';
  mp['v'] = 'p';
  mp['w'] = 'f';
  mp['x'] = 'm';
  mp['y'] = 'a';
  mp['z'] = 'q';
  int n;
  cin >> n >> ws;
  for(int test = 1; test <= n; ++test){
    string s;
    getline(cin, s);
    for(int i = 0, l = s.size(); i < l; ++i)
      s[i] = mp[s[i]];
    cout << "Case #" << test << ": " << s << endl;
  }
}
