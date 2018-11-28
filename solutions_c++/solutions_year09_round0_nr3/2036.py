#include <cstdio>

int T;
char S[500];
int M[2][500];
char K[] = "welcome to code jam";

int main() {
  scanf("%d\n", &T);
  for(int t = 0; t < T; t++) {
    int l=0, i, j, c;
    while(1) {
      c = getchar();
      if(c == '\n') break;
      M[0][l] = (l > 0 ? M[0][l-1] : 0) + (c == 'w' ? 1 : 0);
      S[l] = c;
      l++;
    }
    for(i = 1; i < 19; i++) {
      for(j = 0; j < l; j++) M[i%2][j] = 0;
      for(j = 0; j < l; j++) {
        M[i%2][j] = (M[i%2][j-1] + (S[j] == K[i] ? M[(i+1)%2][j-1] : 0)) % 10000;
      }
    }
    printf("Case #%d: %04d\n", t+1, M[19%1][l-1]);
  }
  return 0;
}

