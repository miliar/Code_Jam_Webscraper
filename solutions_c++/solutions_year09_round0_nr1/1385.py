#include <stdio.h>

int L, D, N;
int i,j;
int n;

char dic[5000][20];
int tok[15][30];
char s[10000], *p;

int main() {

  scanf("%d %d %d", &L, &D, &N);

  for (i = 0; i < D; i++) {
    scanf("%s", dic[i]);    
  }

  //for (i = 0; i < D; i++) {
//    printf("%s\n", dic[i]);    
//  }

  for (n = 1; n <= N; n++) {

    for (i = 0; i < L; i++)
      for (j = 0; j < 26; j++)
        tok[i][j] = 0;

    scanf("%s", s);

    p = s;
    i = 0;
    while (*p != 0) {
      if (*p == '(') { 
        p++;
        while (*p != ')') {
          tok[i][(int)(*p - 'a')] = 1;
          p++; 
        }
        i++; 
        p++;  
      } else {
          tok[i][(int)(*p - 'a')] = 1;
          i++; 
          p++; 
      }
    } 
/*
    for (i = 0; i < L; i++) {
      for (j = 0; j < 26; j++) {
        printf("%d", tok[i][j]);
      }
      printf("\n");  
    }
*/
    int cnt = 0; 
    for (i = 0; i < D; i++) {
      int done = 1;
      for (j = 0; j < L; j++) {
        if (tok[j][int(dic[i][j] - 'a')] == 0) {
          done = 0; break;  
        }
      }
      if (done == 1) cnt++;  
    }

    printf("Case #%d: %d\n", n, cnt);
  } 
  return 0;
}