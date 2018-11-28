#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

map<char, char> conv;

main(){
  conv[' '] = ' ';
  conv['\n'] = '\n';
  conv['a'] = 'y';
  conv['b'] = 'h';
  conv['c'] = 'e';
  conv['d'] = 's';
  conv['e'] = 'o';
  conv['f'] = 'c';
  conv['g'] = 'v';
  conv['h'] = 'x';
  conv['i'] = 'd';
  conv['j'] = 'u';
  conv['k'] = 'i';
  conv['l'] = 'g';
  conv['m'] = 'l';
  conv['n'] = 'b';
  conv['o'] = 'k';
  conv['p'] = 'r';
  conv['q'] = 'z';
  conv['r'] = 't';
  conv['s'] = 'n';
  conv['t'] = 'w';
  conv['u'] = 'j';
  conv['v'] = 'p';
  conv['w'] = 'f';
  conv['x'] = 'm';
  conv['y'] = 'a';
  conv['z'] = 'q';
  int T;
  cin >> T;
  getchar();
  for(int t=1;t<=T;t++){
    cout << "Case #" << t << ": ";
    char c;
    do{
      scanf("%c", &c);
      cout << conv[c];
    }while(c!='\n');
  }
}
