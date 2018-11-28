#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;



int main() {
  string out [] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

  string in [] = {"our language is impossible to understand",
                   "there are twenty six factorial possibilities",
                   "so it is okay if you want to just give up"};

  
  char inv['z'+1];
  char cmap ['z'+1];
  memset(cmap, '#', 'z'+1);
  memset(inv, '#', 'z'+1);

  inv['y'] = 'a'; inv['e'] = 'o'; inv['q'] = 'z';
  cmap['a'] = 'y'; cmap['o'] = 'e'; cmap['z'] = 'q';  

  for(int i = 0; i < 3; i++) {
    for(int j = 0; j < in[i].size(); j++) {
      inv[out[i][j]] = in[i][j];
      cmap[in[i][j]] = out[i][j];
    }
  }

  for(char i = 'a'; i <= 'z'; i++) {
    char ch = i, pr = '#';
    do {
      pr = ch;
      ch = cmap[ch]; 
    } while(ch != i && ch != '#');
    
    if(ch == '#') {
      bool exists = false;
      for(char j = 'a'; j <= 'z'; j++) {
        if(cmap[j] == i)
          exists = true;
      }
      if(!exists) {
        cmap[pr] = i;
        inv[i] = pr;
      }
    }
  }

  int T;
  cin >> T; 

  string curr;
  getline(cin, curr);

  for(int t = 1; t <= T; t++) {
    getline(cin, curr);
    for(int i = 0; i < curr.size(); i++)
      curr[i] = inv[curr[i]];
    
    cout << "Case #" << t << ": " << curr << endl;
  }
  
  return 0;
}
