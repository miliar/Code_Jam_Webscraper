/*
 * =====================================================================================
 *
 *       Filename:  prog.cc
 *
 *    Description:  j
 *
 *        Version:  1.0
 *        Created:  14.04.2012 12:40:16
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>





#include <cstdio>
#include <iostream>
#include <string>


using namespace std;


int tab[300];

int main() {
tab[97] = 121;
tab[98] = 104;
tab[99] = 101;
tab[100] = 115;
tab[101] = 111;
tab[102] = 99;
tab[103] = 118;
tab[104] = 120;
tab[105] = 100;
tab[106] = 117;
tab[107] = 105;
tab[108] = 103;
tab[109] = 108;
tab[110] = 98;
tab[111] = 107;
tab[112] = 114;
tab[113] = 122;
tab[114] = 116;
tab[115] = 110;
tab[116] = 119;
tab[117] = 106;
tab[118] = 112;
tab[119] = 102;
tab[120] = 109;
tab[121] = 97;
tab[122] = 113;


  string s;
  int i = 0;
  int n;

  getline(cin, s);
  while(!cin.fail()) {
    getline(cin, s);
    if(cin.fail())
      break;
    ++i;
    for(int j = 0; j <= s.size(); ++j) {
      if(s[j] != ' ')
        s[j] = tab[s[j]];
    }

    cout << "Case #" << i << ": " << s << endl;
  }

  return 0;
}
