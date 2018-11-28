#include <string>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
//////////////////////////////////////////

char tab[4][10];

string res;

void check(string s) {
  int o = 0, x = 0;
  REP(a, 4) 
    if (s[a]=='O') ++o;
    else 
    if (s[a]=='X') ++x;
    else 
    if (s[a]=='T') ++o, ++x;
  if (o==4)
    res = "O won";
  if (x==4)
    res = "X won";
}

void licz() {
  res = "Draw";
  REP(a, 4) REP(b, 4)
    if (tab[a][b]=='.')
      res = "Game has not completed";
  REP(a, 4) {
    string s1, s2;
    REP(b, 4) {
      s1 += tab[a][b];
      s2 += tab[b][a];
    }
    check(s1);
    check(s2);
  }
  string sa, sb;
  REP(a, 4) {
    sa += tab[a][a];
    sb += tab[a][3-a];
  }
  check(sa);
  check(sb);
}

int main() {
  int TT;
  scanf("%d ", &TT);
  REP(tt, TT) {
    REP(a, 4)
      scanf("%s", tab[a]);
    licz();
    printf("Case #%d: %s\n", tt+1, res.c_str());
  }
}
