#include <iostream>
#include <algorithm>
#include <iterator>
#include <set>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

char tmap[100];

void initMap(){

  tmap['a'] = 'y';
  tmap['b'] = 'h';
  tmap['c'] = 'e';
  tmap['d'] = 's';
  tmap['e'] = 'o';
  tmap['f'] = 'c';
  tmap['g'] = 'v';
  tmap['j'] = 'u';
  tmap['h'] = 'x';
  tmap['k'] = 'i';
  tmap['i'] = 'd';
  tmap['l'] = 'g';
  tmap['m'] = 'l';
  tmap['n'] = 'b';
  tmap['o'] = 'k';
  tmap['p'] = 'r';
  tmap['q'] = 'z';
  tmap['r'] = 't';
  tmap['s'] = 'n';
  tmap['t'] = 'w';
  tmap['u'] = 'j';
  tmap['v'] = 'p';
  tmap['w'] = 'f';
  tmap['x'] = 'm';
  tmap['y'] = 'a';
  tmap['z'] = 'q';
  tmap[' '] = ' ';
}

int main () {
  int T;
  int N;
  int tmp;
  string G;
  char GO[100];

  initMap();
  cin >> T;
  cin.ignore();
  for(int t=0;t<T;t++){
    
    std::getline(cin,G);
    //scanf("%s",G);

    int i;
    for(i=0;i<G.length();i++){
      GO[i] = tmap[G[i]];
    }

    GO[i] = '\0';
 
    cout << "Case #" << (t+1)  << ": " << GO << endl;

  }
  return 0;
}
