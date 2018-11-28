#include <stdio.h>
#include <string.h>

char agulha[] = " welcome to code jam";
char palheiro[510];
int qtd[30];
int main() {
  int N;
  scanf("%d", &N);
  for (int t = 0; t < N; t++) {
    scanf(" %[^\n]", palheiro);
    memset(qtd, 0, sizeof(qtd));
    qtd[0] = 1;
    for (int i = 0; palheiro[i]; i++) {
      for (int j = 1; agulha[j]; j++) {
        if (palheiro[i] == agulha[j])
          qtd[j] = (qtd[j] + qtd[j-1])%10000;
      }
    }
    printf("Case #%d: %04d\n", t+1, qtd[strlen(agulha)-1]);
  }
  return 0;
}
