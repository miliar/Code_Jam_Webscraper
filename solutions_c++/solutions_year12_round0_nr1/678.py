#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

char text[3][105] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char trans[3][105] = {
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"
};

char has[300];
char str[33][300];
int N;
void Print() {
  for (int i = 0; i < N; i++) {
    printf("Case #%d: ", i + 1);
    int len = strlen(str[i]);
    for (int j = 0; j < len; j++) {
      printf("%c", has[str[i][j]]);
    }
    printf("\n");
  }
}
int main() {
  memset(has, 'A', sizeof(has));
  has[' '] = ' ';
  for (int i = 0; i <3; i++) {
    int len = strlen(text[i]);
    for (int j = 0; j < len; j++) {
      has[text[i][j]] = trans[i][j];
    }
  }
  // for (int i = 'a'; i <= 'z'; i++) {
  //   printf("%c", has[i]);
  // }
  // printf("\n");
  scanf("%d", &N);
  getchar();
  for (int i = 0; i < N; i++) {
    gets(str[i]);
  }
  // has['z'] = 'z';
  // has['q'] = 'q';
  // Print();
  // printf("\n\n");
  has['z'] = 'q';
  has['q'] = 'z';
  Print();
  return 0;
}
