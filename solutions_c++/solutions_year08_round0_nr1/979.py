#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 110
#define INF 99999
#define min(a,b) ((a)<(b)?(a):(b))
struct Engin 
{
  char name[N];
} engin[N];
char query[N];
int sw[2][110];

void trim(char *s) 
{
  int i;
  for(i = strlen(s)-1; i>=0 && s[i] <= 32; i--)
    s[i] = 0;
}

int main()
{
  int n, index;
  int s, q, i, j, k, fst, new_fst;
  
  scanf("%d\n", &n);
  for(index = 1; index <= n; index++) {
    scanf("%d\n", &s);
    for(i = 0; i < s; i++) {
      fgets(engin[i].name, N, stdin);
      trim(engin[i].name);
    }
    for(j = 0; j < s; j++)
      sw[0][j] = 0;
    fst = 0;
    scanf("%d\n", &q);
    for(i = 1; i <= q; i++) {
      fgets(query, N, stdin);
      trim(query);
      for(k = 0; k < s && strcmp(query, engin[k].name); k++);
      new_fst = 0;
      for(j = 0; j < s; j++) {
        if(j == k) sw[i&1][j] = INF;
        else sw[i&1][j] = min(sw[(i&1)^1][j], sw[(i&1)^1][fst]+1);
        if(sw[i&1][j] < sw[i&1][new_fst])
          new_fst = j;
      }
      fst = new_fst;
    }
    printf("Case #%d: %d\n", index, sw[q&1][fst]);
  }
  return 0;
}
