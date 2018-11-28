#include <cstdio>
#include <cstring>
#define C_MAX 36
#define D_MAX 28
#define DEBUG 0

void combine(char *list, char comb[C_MAX][4], int C) {
  int list_len = strlen(list);
  if (list_len < 2)
    return;
  for (int i = 0; i < C; i++) {
    if ((list[list_len-2] == comb[i][0] && list[list_len-1] == comb[i][1])
      || (list[list_len-1] == comb[i][0] && list[list_len-2] == comb[i][1])) {
      list[list_len-2] = comb[i][2];
      list[list_len-1] = '\0';
      #if 0
        printf("Comb:- %s\n", list);
      #endif
      break;
    }
  }
}

void delete1(char *list, char oppose[D_MAX][4], int D) {
  int list_len = strlen(list);
  char to_find;
  for (int i = 0; i < D; i++) {
    if (list[list_len-1] == oppose[i][0] || list[list_len-1] == oppose[i][1]) {
      to_find = (list[list_len-1] == oppose[i][0])?oppose[i][1]:oppose[i][0];
      for (int j = 0; j < list_len-1; j++) {
        if (list[j] == to_find) {
          list[0] = '\0';
          #if 0
            printf("Del:- %s\n", list);
          #endif
          break;
        }
      }
      if (list[0] == '\0') break;      
    }
  }
}

int main () {
  int kases;
  scanf("%d", &kases);
  for (int i = 1; i <= kases; i++) {
    int C, D, N;
    scanf("%d", &C);
    char comb[C_MAX][4] = {};
    for (int j = 0; j < C; j++) {
      scanf("%s", comb[j]);
    }
    scanf("%d", &D);
    char oppose[D_MAX][4] = {};
    for (int j = 0; j < D; j++) {
      scanf("%s", oppose[j]);
    }
    scanf("%d", &N);  
    char input[110] = {};
    scanf("%s", input);
    #if DEBUG
      for (int j = 0; j < C; j++)
        printf("%s, ", comb[j]);
      printf("\n");
      for (int j = 0; j < D; j++)
        printf("%s, ", oppose[j]);
      printf("\n");
      printf("%d %s\n", N, input);  
    #endif
    // INPUTTING DONE
    char list[110] = {};
    list[0] = input[0];
    for (int j = 1; j < N; j++) {
      int len = strlen(list);
      #if 0
        printf("len = %d\n", len);
      #endif
      list[len] = input[j];
      list[len+1] = '\0';
      combine(list, comb, C);
      #if DEBUG
        printf("Main: %d %s\n", j, list);
      #endif
      delete1(list, oppose, D);
      #if DEBUG
        printf("Main: %d %s\n", j, list);
      #endif
    }
    int len = strlen(list);
    // Output format
    printf("Case #%d: [", i);
    for (int j = 0; j < len-1; j++) {
        printf("%c, ", list[j]);
    }
    if (len > 0)
      printf("%c]\n", list[len-1]);
    else
      printf("]\n");
  }
}
