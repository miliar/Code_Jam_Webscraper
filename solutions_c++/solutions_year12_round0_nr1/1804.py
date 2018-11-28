#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cassert>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); i++)

typedef vector<int> VI;

char trans[30] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
  
  int T;
  scanf(" %d ", &T);

  REP(tc, T) {
    char s[128];
    fgets(s, 128, stdin);
    int len = strlen(s);
    REP(i, len) if(s[i] != ' ') s[i] = trans[s[i] - 'a'];
    printf("Case #%d: %s\n", tc + 1, s);
  }

  return 0;
}
