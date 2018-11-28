#include<stdio.h>
#include<string.h>

#define MAXN 1000
#define MAXL 100

int s, q;

char engines[MAXL][MAXL];
int queries[MAXN];
int table[MAXN+1][MAXL];

int findEngine(char *q){
  for(int i = 0; i < s; i++){
    if (!strcmp(engines[i], q))
      return i;
  }
  printf("ERROR on findEngine!\n");
  return -1;
}

void solve(){
  scanf("%d\n", &s);
  for(int i = 0; i < s; i++) {
    gets(engines[i]);
  }
  scanf("%d\n", &q);
  char str[MAXL];
  for(int i = 0; i < q; i++) {
    gets(str);
    queries[i] = findEngine(str);
  }
  for(int i = 1; i <= q; i++) {
    for(int j = 0; j < s; j++) {
      if (queries[i-1] == j) {
	int c = 100000;
	for(int k = 0; k < s; k++) {
	  if (k != j)
	    c <?= table[i-1][k] + 1;
	}
	table[i][j] = c;
      } else {
	table[i][j] = table[i-1][j];
      }
    }
  }
  int ans = 100000;
  for(int j = 0; j < s; j++) {
    ans <?= table[q][j];
  }
  printf("%d\n", ans);
}

int main() {
  int ncases;
  scanf("%d", &ncases);
  for(int i = 0; i < ncases; i++) {
    printf("Case #%d: ", i+1);
    solve();
  }
  return 0;
}
