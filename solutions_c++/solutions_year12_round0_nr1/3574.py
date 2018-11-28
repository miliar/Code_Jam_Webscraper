#include <iostream>
#include <map>
#include <string>

using namespace std;

map<char, char> M;

void initialize(){
  M['y'] = 'a';
  M['n'] = 'b';
  M['f'] = 'c';
  M['i'] = 'd';
  M['c'] = 'e';
  M['w'] = 'f';
  M['l'] = 'g';
  M['b'] = 'h';
  M['k'] = 'i';
  M['u'] = 'j';
  M['o'] = 'k';
  M['m'] = 'l';
  M['x'] = 'm';
  M['s'] = 'n';
  M['e'] = 'o';
  M['v'] = 'p';
  M['z'] = 'q';
  M['p'] = 'r';
  M['d'] = 's';
  M['r'] = 't';
  M['j'] = 'u';
  M['g'] = 'v';
  M['t'] = 'w';
  M['h'] = 'x';
  M['a'] = 'y';
  M['q'] = 'z';
}

int main(){
  initialize();

  int T;

  while(cin >> T && T){
    string line;
    getline(cin, line);
    
    for(int i = 1; i <= T; i++){
      getline(cin, line);

      for(int j = 0; j < line.size(); j++){
	if(line[j] == ' ') continue;
	line[j] = M[line[j]];
      }
      cout << "Case #" << i << ": " << line << endl;
    }
  }
  return 0;
}
