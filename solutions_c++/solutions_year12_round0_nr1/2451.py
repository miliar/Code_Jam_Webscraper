#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main() {
  ifstream cin("data.txt");
  ofstream cout("out1.txt");
  char map[256];
  map['y']='a';map['n']='b';map['f']='c';map['i']='d';map['c']='e';map['w']='f';map['l']='g';map['b']='h';map['k']='i';map['u']='j';map['o']='k';map['m']='l';map['x']='m';map['s']='n';map['e']='o';map['v']='p';map['z']='q';map['p']='r';map['d']='s';map['r']='t';map['j']='u';map['g']='v';map['t']='w';map['h']='x';map['a']='y';map['q']='z';

  int N;
  string line;
  cin >> N;
  cin.get();
  for (int i = 0; i < N; i++) {
    cout << "Case #" << i+1 << ": ";
    getline(cin, line);
    for (int j = 0; j < line.length(); j++) {
      if (line[j] == ' ') {
        cout << " ";
      } else {
        cout << (char)map[line[j]];
      }
    }
    cout << endl;
  }
}