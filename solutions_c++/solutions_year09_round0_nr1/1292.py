#include <iostream>

using namespace std;

#define for_to(i,j,k) for (i=j; i<=k; ++i)

#define MAXD 5100
#define MAXL 20

int L,N,D;
int i,j,k,test,ans;
char dic[MAXD][MAXL];
int pattern[MAXL];

int read_next() {
  int ret = 0;
  char c;
  scanf(" %c",&c);
  if (c != '(') return 1 << (c-'a');
  scanf(" %c",&c);
  while (c != ')') {
    ret += 1 << (c-'a');
    scanf(" %c",&c);
  }
  return ret;
}

int main() {
  scanf("%d %d %d",&L,&D,&N);
  for_to(i,0,D-1)
    scanf(" %s",dic[i]);
  for_to(test,1,N) {
    for_to(i,0,L-1)
        pattern[i] = read_next();
    ans = 0;
    for_to(i,0,D-1) {
      j = 0;
      while (j < L && (pattern[j] & ( 1 << (dic[i][j]-'a') ) ) ) ++j;
      if (j == L) ++ans;
    }
    printf("Case #%d: %d\n",test,ans);
  }
  return 0;
}
