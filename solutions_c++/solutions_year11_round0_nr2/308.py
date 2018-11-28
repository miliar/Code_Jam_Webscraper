#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <cassert>
#include <algorithm>
using namespace std;

#define maxn 33

char comg[maxn][maxn];
bool oppg[maxn][maxn];
int T, n, C, D;
char invoke[200];

string doit(string invoke) {

  string ret;
  
  for(int i = 0; i < invoke.length(); i++) {
    char ch = invoke[i];
    ret += ch;
    while (ret.length() > 1 && comg[*(ret.end()-1)-'A'][*(ret.end()-2)-'A']) {
      char tch = comg[*(ret.end()-1)-'A'][*(ret.end()-2)-'A'];
      ret.erase(ret.length()-2, 2);
      ret += tch;
    }
    char lastchar = ret[ret.length()-1];
    for(int j = 0; j < ret.length()-1; j++)
      if (oppg[ret[j]-'A'][lastchar-'A']) {ret.clear(); break; }
  }
  
  return ret;

}

int main() {

  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);
  
  scanf("%d\n", &T);
  for(int cT = 0; cT < T; cT++) {
    
    memset(comg,0,sizeof(comg));
    memset(oppg,0,sizeof(oppg));
    scanf("%d", &C);
    char tmp[5];
    for(int i = 0; i < C; i++) {
      scanf("%s", tmp);
      comg[tmp[0]-'A'][tmp[1]-'A'] = comg[tmp[1]-'A'][tmp[0]-'A'] = tmp[2];
    }
    scanf("%d", &D);
    for(int i = 0; i < D; i++) {
      scanf("%s", tmp);
      oppg[tmp[0]-'A'][tmp[1]-'A'] = oppg[tmp[1]-'A'][tmp[0]-'A'] = true;
    }
    scanf("%d", &n);
    scanf("%s\n", invoke);
    
    string ret = doit(invoke);
    printf("Case #%d: [", cT+1);
    if (!ret.empty()) putchar(ret[0]);
    for(int i = 1; i < ret.length(); i++)
      printf(", %c", ret[i]);
    printf("]\n");
    
  }
  
  return 0;

}
