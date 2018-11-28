#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define ascii(X) (X)
#define alpha(X) (X)
short int comb[256][256];
bool opp[256][256];
char str[105], ans[105];

int main()
{
  int T, C, D, len, N;
  scanf("%d", &T);
  for(int cas = 1 ; cas <= T ; cas ++) {
    memset(comb, -1, sizeof comb), memset(opp, 0, sizeof opp);
    scanf("%d", &C);
    while(C --) {
      scanf("%s", str);
      int A = alpha(str[0]), B = alpha(str[1]), X = alpha(str[2]);
      comb[A][B] = comb[B][A] = X;
    }

    scanf("%d", &D);
    while(D --) {
      scanf("%s", str);
      int A = alpha(str[0]), B = alpha(str[1]);
      opp[A][B] = opp[B][A] = 1;
    }

    scanf("%d %s", &N, str);
    len = 0;
    for(int i = 0 ; i < N ; i ++) {
      ans[len ++] = str[i];
      if(len > 1)
        if(comb[ans[len - 2]][ans[len - 1]] != -1)
          ans[len - 2] = comb[ans[len - 2]][ans[len - 1]], len --;
      
      for(int j = 0 ; j < len - 1 ; j ++)
        if(opp[ans[j]][ans[len - 1]])
          len = 0;
    }

    printf("Case #%d: ", cas);
    printf("[");
    for(int i = 0 ; i < len - 1; i ++)
      printf("%c, ", ans[i]);

    if(len)
      printf("%c", ans[len - 1]);
    printf("]\n");
  }
}
