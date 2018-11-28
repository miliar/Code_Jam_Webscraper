#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PROBLEM "a"
#define INFTY 0x3F3F3F3F

typedef long long i64;
typedef unsigned long long u64;

#define MAXQ 1010
#define MAXS 110
#define LEN 110

char engines[MAXS][LEN];
char queries[MAXQ][LEN];



int dp[MAXQ][MAXS];

char str[10000];

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  gets(str);
  sscanf(str,"%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int S,Q,i,j,k;
    gets(str);
    sscanf(str,"%d",&S);
    for(i=0;i<S;++i) {
      gets(engines[i]);
    }
    gets(str);
    sscanf(str,"%d",&Q);
    for(i=0;i<Q;++i) {
      gets(queries[i]);
    }
    memset(dp,0x3F,sizeof(dp));
    for(i=0;i<S;++i)
      dp[Q][i]=0;
    for(i=Q-1;i>=0;--i) {
      for(j=0;j<S;++j) {
        if(strcmp(queries[i],engines[j])) {
          dp[i][j]=dp[i+1][j];
        }
        else {
          int min=INFTY;
          for(k=0;k<S;++k) {
            if(k!=j && min>dp[i+1][k]) {
              min=dp[i+1][k];
            }
          }
          dp[i][j]=min+1;
        }
      }
    }
    int ans=INFTY;
    for(j=0;j<S;++j)
      if(dp[0][j]<ans)
        ans=dp[0][j];
    printf("Case #%d: %d\n",tst,ans);
  }


  return 0;
}
