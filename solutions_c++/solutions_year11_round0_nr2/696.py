#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()

char comb[26][26];
bool opps[26][26];

int main() {
  int T; scanf("%d", &T);
  
  for(int t=1; t<=T; t++) {
    rep(i, 26) rep(j, 26) comb[i][j] = opps[i][j] = 0;
    int C, D, N;
    scanf("%d", &C);
    rep(i, C) {
      char s[4]; scanf("%s", s);
      comb[s[0]-'A'][s[1]-'A'] = s[2];
      comb[s[1]-'A'][s[0]-'A'] = s[2];
    }
    scanf("%d", &D);
    rep(i, D) {
      char s[3]; scanf("%s", s);
      opps[s[0]-'A'][s[1]-'A'] = true;
      opps[s[1]-'A'][s[0]-'A'] = true;
    }
    scanf("%d", &N);
    char s[101]; scanf("%s", s);
    
    
    int size = 0;
    char res[101];
    int in[26]; rep(i, 26) in[i] = 0;
    
    rep(i, N) {
      res[size++] = s[i];
      in[res[size-1]-'A']++;
      if(size >= 2) {
        if(comb[res[size-1]-'A'][res[size-2]-'A']) {
          in[res[size-1]-'A']--;
          in[res[size-2]-'A']--;
          res[size-2] = comb[res[size-1]-'A'][res[size-2]-'A'];
          size--;
          in[res[size-1]-'A']++;
        }
      }
      rep(i, 26) {
        if(opps[res[size-1]-'A'][i] &&
           in[res[size-1]]-'A' && in[i]) {
          size = 0;
          rep(i, 26) in[i] = 0;
        }
      }
    }
    
    printf("Case #%d: [", t);
    rep(i, size-1) printf("%c, ", res[i]);
    if(size) printf("%c", res[size-1]);
    printf("]\n");
  }
  
  return 0;
}
