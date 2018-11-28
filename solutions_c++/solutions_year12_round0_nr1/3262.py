#include <iostream>
#include <map>
using namespace std;

int main(){
  int T;
  cin >> T;
  string lines[T];
  string new_lines[T];
  string dummy;

  map<char,char> mapa2;
  mapa2[' '] = ' ';
  mapa2['a'] = 'y';
  mapa2['b'] = 'h';
  mapa2['c'] = 'e';
  mapa2['d'] = 's';
  mapa2['e'] = 'o';
  mapa2['f'] = 'c';
  mapa2['g'] = 'v';
  mapa2['h'] = 'x';
  mapa2['i'] = 'd';
  mapa2['j'] = 'u';
  mapa2['k'] = 'i';
  mapa2['l'] = 'g';
  mapa2['m'] = 'l';
  mapa2['n'] = 'b';
  mapa2['o'] = 'k';
  mapa2['p'] = 'r';
  mapa2['q'] = 'z';
  mapa2['r'] = 't';
  mapa2['s'] = 'n';
  mapa2['t'] = 'w';
  mapa2['u'] = 'j';
  mapa2['v'] = 'p';
  mapa2['w'] = 'f';
  mapa2['x'] = 'm';
  mapa2['y'] = 'a';
  mapa2['z'] = 'q';

  getline(cin, dummy);
  for (int i=0; i<T; i++){
    getline(cin,lines[i]);

  }

  for (int i=0; i<T; i++){
    new_lines[i] = "";
    for (int j=0; j<lines[i].length(); j++){

      new_lines[i].push_back(mapa2[lines[i][j]]);
    }
  }

  for (int i=0; i<T; i++){
    cout << "Case #" << i + 1 << ": " <<  new_lines[i] << endl;
  }

}



