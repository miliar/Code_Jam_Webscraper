// welcome to code jam

#include <stdio.h>
#include <string.h>
#define MAXLEN 550
#define MOD 10000

const int tlen = 19;
char tar[20] = "welcome to code jam";

int n;
char s[MAXLEN];
int w[MAXLEN][tlen];

inline int Count(void)
{
  int i,j;
  for(j=0;j<tlen;j++)
    w[0][j]=0;
  for(i=1;i<=n;i++) {
    for(j=0;j<tlen;j++)
      w[i][j]=w[i-1][j];
    if(s[i]==tar[0]) w[i][0]++;
    for(j=1;j<tlen;j++) {
      if(s[i]==tar[j]) w[i][j]+=w[i][j-1];
    }
    for(j=0;j<tlen;j++)
      w[i][j]%=MOD;
  }
  return w[n][tlen-1];
}

int main(void)
{
  int t,casenum;
  gets(s);
  sscanf(s,"%d",&t);
  for(casenum=1;casenum<=t;casenum++) {
    gets(s+1);
    n=strlen(s+1);
    printf("Case #%d: %04d\n",casenum,Count());
  }
  return 0;
}
