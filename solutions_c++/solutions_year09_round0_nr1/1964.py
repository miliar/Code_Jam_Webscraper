#include <cstdio>

using namespace std;

int L, D, N;
char words[5000][15];
bool allow[15][26];

int main() {
  int i, j, k;
  scanf("%d %d %d ", &L, &D, &N);
  for(i = 0; i < D; i++) {
    for(j = 0; j < L; j++)
      words[i][j] = getchar();
    getchar();   // '\n'
  }
  for(i = 0; i < N; i++) {
    for(j = 0; j < L; j++) {
      for(k = 0; k < 26; k++)
        allow[j][k] = 0;
      int a = getchar();
      if(a == '(') {
        while(1) {
          a = getchar();
          if(a == ')') break;
          allow[j][a-'a'] = 1;
        }
      }
      else {
        allow[j][a-'a'] = 1;
      }
    }
    getchar();
    int r = 0;
    for(j = 0; j < D; j++) {
      int ok = 1;
      for(k = 0; k < L; k++)
        if(!allow[k][words[j][k]-'a'])
          ok = 0;
      if(ok)
        r++;
    }
    printf("Case #%d: %d\n", i+1, r);
  }
  return 0;
}

