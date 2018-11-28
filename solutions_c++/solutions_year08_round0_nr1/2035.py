#include <stdio.h>
#include <string.h>

int main () {
  int n,s,q;
  char buff[256];
  char engines[110][110];
  //char queries[1100][110];
  int queryEng[1100];

  int cases, i, j, k, w;
  
  int dp[1100][110];

  fgets(buff, 250, stdin);
  sscanf(buff, "%d", &n);

  for (cases=1; cases<=n; cases++) {
    fgets(buff, 250, stdin);
    sscanf(buff, "%d", &s);
    for (i=1; i<=s; i++)
      fgets(engines[i], 250, stdin);
    fgets(buff, 250, stdin);
    sscanf(buff, "%d", &q);
    for (i=1; i<=q; i++) {
      fgets(buff, 250, stdin);
      for (j=1; j<=s; j++) {
          if (strcmp(engines[j], buff)==0) {
             queryEng[i]=j;
             break;
          }
      }
    }

    //
    
    for (j=0;j<s;j++)
        dp[0][j]=0;
    
    for (i=1;i<=q;i++) {
        for (j=1;j<=s;j++) {
            if (queryEng[i]==j) dp[i][j]=-1;
            else {
                 w = -1;
                 for (k=1; k<=s; k++) {
                     if (dp[i-1][k]!=-1) {
                        if (w==-1) w=k;
                        else {
                             if (dp[i-1][k]+((k==j)?0:1) < dp[i-1][w]+((w==j)?0:1))
                               w=k;
                        }
                     }
                 }
                 dp[i][j]=dp[i-1][w]+((w==j)?0:1);
            }
        }
    }
    
    w=-1;
    for (j=1;j<=s;j++) {
        if ((dp[q][j]<dp[q][w] || w==-1) && dp[q][j]!=-1) w=j;
    }
    
    printf("Case #%d: %d\n",cases,dp[q][w]);
  }


  return 0;
}
