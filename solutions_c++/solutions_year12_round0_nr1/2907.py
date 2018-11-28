#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <queue>
#include <map>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
int main() {
   map<char, char> mapping;
   mapping[' '] = ' ';
   mapping['a'] = 'y';
   mapping['b'] = 'h';
   mapping['c'] = 'e';
   mapping['d'] = 's';
   mapping['e'] = 'o';
   mapping['f'] = 'c';
   mapping['g'] = 'v';
   mapping['h'] = 'x';
   mapping['i'] = 'd';
   mapping['j'] = 'u';
   mapping['k'] = 'i';
   mapping['l'] = 'g';
   mapping['m'] = 'l';
   mapping['n'] = 'b';
   mapping['o'] = 'k';
   mapping['p'] = 'r';
   mapping['q'] = 'z';
   mapping['r'] = 't';
   mapping['s'] = 'n';
   mapping['t'] = 'w';
   mapping['u'] = 'j';
   mapping['v'] = 'p';
   mapping['w'] = 'f';
   mapping['x'] = 'm';
   mapping['y'] = 'a';
   mapping['z'] = 'q';
   
   int T;
   cin >> T;
   char line[120];
   cin.getline(line,101); //discard first line
   
   FOR(t,T) {
      cin.getline(line,101);
      printf("Case #%d: ", t+1);
      char *cur = line;
      while (*cur != '\0') {
         printf("%c",mapping[*cur]);
         cur++;
      }
      printf("\n");
   }
   return 0;
}

