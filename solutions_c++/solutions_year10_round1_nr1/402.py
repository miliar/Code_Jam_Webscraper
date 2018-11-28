#include <stdio.h>

int main()
{
  int T, N, K;
  char tab[60][60];
  scanf("%i", &T);
  for(int t = 0; t < T; t++) {
    scanf("%i %i", &N, &K);
    for(int i = 0; i < N; i++)
      scanf("%s", tab[i]);
    /*
    printf("before:\n");
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++)
        printf("%c", tab[i][j]);
      printf("\n");
    }//*/
    for(int i = 0; i < N; i++) {
      bool first = false;
      int fi;
      for(int j = N - 1; j >= 0; j--) {
        if(tab[i][j] == '.' && !first) {
          first = true;
          fi = j;
        } else if(tab[i][j] != '.' && first) {
          tab[i][fi--] = tab[i][j];
          tab[i][j] = '.';
        }
      }
    }
    /*
    printf("after:\n");
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++)
        printf("%c", tab[i][j]);
      printf("\n");
    }//*/
    
    bool red = false, blue = false;
    int dx[4] = {0, 1, 1, 1}, dy[4] = {1, 1, 0, -1};
    for(int i = 0; i < N; i++) {
      for(int j = 0; j < N; j++) {
        if(tab[i][j] == '.') continue;
        for(int d = 0; d < 4; d++) {
          int z;
          for(z = 1; z < K; z++) {
            int x = i + z * dx[d], y = j + z * dy[d];
            //printf("%i %i %i %i %i\n", i, j, z, x, y);
            if(x < 0 || x >= N || y < 0 || y >= N) break;
            if(tab[x][y] != tab[i][j]) break;
          }
          if(z == K) {
            if(tab[i][j] == 'R') red = true;
            else blue = true;
          }
        }
      }
    }
    printf("Case #%i: %s\n", t + 1, red && blue ? "Both" : red ? "Red" : blue ? "Blue" : "Neither");
  }
  return 0;
}
