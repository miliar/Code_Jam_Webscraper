#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

#define D(x) cout << #x " is " << x << endl

int main(){
  int T;
  cin >> T;
  string line;
  getline(cin, line);
  map<char, char> m;
  m['e'] = 'o';
  m['j'] = 'u';
  m['p'] = 'r';
  m[' '] = ' ';
  m['m'] = 'l';
  m['y'] = 'a';
  m['s'] = 'n';
  m['l'] = 'g';
  m['j'] = 'u';
  m['y'] = 'a';
  m['l'] = 'g';
  m['c'] = 'e';
  m[' '] = ' ';
  m['k'] = 'i';
  m['d'] = 's';
  m[' '] = ' ';
  m['k'] = 'i';
  m['x'] = 'm';
  m['v'] = 'p';
  m['e'] = 'o';
  m['d'] = 's';
  m['d'] = 's';
  m['k'] = 'i';
  m['n'] = 'b';
  m['m'] = 'l';
  m['c'] = 'e';
  m[' '] = ' ';
  m['r'] = 't';
  m['e'] = 'o';
  m[' '] = ' ';
  m['j'] = 'u';
  m['s'] = 'n';
  m['i'] = 'd';
  m['c'] = 'e';
  m['p'] = 'r';
  m['d'] = 's';
  m['r'] = 't';
  m['y'] = 'a';
  m['s'] = 'n';
  m['i'] = 'd';
  m['r'] = 't';
  m['b'] = 'h';
  m['c'] = 'e';
  m['p'] = 'r';
  m['c'] = 'e';
  m[' '] = ' ';
  m['y'] = 'a';
  m['p'] = 'r';
  m['c'] = 'e';
  m[' '] = ' ';
  m['r'] = 't';
  m['t'] = 'w';
  m['c'] = 'e';
  m['s'] = 'n';
  m['r'] = 't';
  m['a'] = 'y';
  m[' '] = ' ';
  m['d'] = 's';
  m['k'] = 'i';
  m['h'] = 'x';
  m[' '] = ' ';
  m['w'] = 'f';
  m['y'] = 'a';
  m['f'] = 'c';
  m['r'] = 't';
  m['e'] = 'o';
  m['p'] = 'r';
  m['k'] = 'i';
  m['y'] = 'a';
  m['m'] = 'l';
  m[' '] = ' ';
  m['v'] = 'p';
  m['e'] = 'o';
  m['d'] = 's';
  m['d'] = 's';
  m['k'] = 'i';
  m['n'] = 'b';
  m['k'] = 'i';
  m['m'] = 'l';
  m['k'] = 'i';
  m['r'] = 't';
  m['k'] = 'i';
  m['c'] = 'e';
  m['d'] = 's';
  m['d'] = 's';
  m['e'] = 'o';
  m[' '] = ' ';
  m['k'] = 'i';
  m['r'] = 't';
  m[' '] = ' ';
  m['k'] = 'i';
  m['d'] = 's';
  m[' '] = ' ';
  m['e'] = 'o';
  m['o'] = 'k';
  m['y'] = 'a';
  m['a'] = 'y';
  m[' '] = ' ';
  m['k'] = 'i';
  m['w'] = 'f';
  m[' '] = ' ';
  m['a'] = 'y';
  m['e'] = 'o';
  m['j'] = 'u';
  m[' '] = ' ';
  m['t'] = 'w';
  m['y'] = 'a';
  m['s'] = 'n';
  m['r'] = 't';
  m[' '] = ' ';
  m['r'] = 't';
  m['e'] = 'o';
  m[' '] = ' ';
  m['u'] = 'j';
  m['j'] = 'u';
  m['d'] = 's';
  m['r'] = 't';
  m[' '] = ' ';
  m['l'] = 'g';
  m['k'] = 'i';
  m['g'] = 'v';
  m['c'] = 'e';
  m[' '] = ' ';
  m['j'] = 'u';
  m['v'] = 'p';
  m['z'] = 'q';
  m['q'] = 'z';

  for(int C=0;C<T;++C){
    getline(cin, line);
    int n = line.size();
    printf("Case #%d: ", C + 1);
    for(int i=0;i<n;++i){
      cout << m[line[i]];
    }
    puts("");
  }
  return 0;
}
