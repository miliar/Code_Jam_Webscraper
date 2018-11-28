#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <iostream>
#include <map>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#include <fstream>

using namespace std;
typedef long long LL;

#define INF 2000000000
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define FS first
#define SD second
#define MP make_pair
#define RESET(t) memset(t, -1, sizeof(t))
#define MAX 10000050


int main() {
  std::vector<std::string> v, u;
  v.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
  v.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  v.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

  u.push_back("our language is impossible to understand");
  u.push_back("there are twenty six factorial possibilities");
  u.push_back("so it is okay if you want to just give up");
  
  char mapp[256];
  memset(mapp, 0, sizeof(mapp));
  FOR(i,0,3) {
    FOR(j,0,SZ(v[i])) {
      mapp[v[i][j]] = u[i][j];
    }
  }
  //for (char c = 'a'; c <= 'z'; ++c) printf("%c=%c\n",c, mapp[c]);
  mapp['z'] = 'q';
  mapp['q'] = 'z';
  
  int test;scanf("%d\n",&test);
  char s[200];
  FORE(T,1,test) {
    gets(s);
    printf("Case #%d: ", T);
    FOR(i,0,200) {
      if (s[i] == 0) break;
      printf("%c",mapp[s[i]]);
    }
    printf("\n");
  }
}