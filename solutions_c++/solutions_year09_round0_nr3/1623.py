#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

const char w[22]="\0welcome to code jam\0";
const int m=19;
const int maxn=505;

int test,testcase,n,i,j,x,ans;
char ch,a[maxn];
int d[maxn][m+5];

int main() {
  freopen("poj.in","r",stdin);
  freopen("poj.out","w",stdout);
  scanf("%d\n",&testcase);
  for (test=1; test<=testcase; ++test) {
    printf("Case #%d: ",test);
    n=0;
    scanf("%c",&ch);
    while (ch!='\n') {
      a[++n]=ch;
      if (scanf("%c",&ch)!=EOF) continue;
      else break;
    }
    memset(d,0,sizeof(d));
    for (i=1; i<=n; ++i)
      if (a[i]==w[1]) d[i][1]=1;
    for (i=1; i<=n; ++i)
      for (x=2; x<=m; ++x)
        for (j=1; j<i; ++j)
          if (w[x]==a[i]) d[i][x]=(d[i][x]+d[j][x-1])%10000;
    ans=0;
    for (i=1; i<=n; ++i)
      ans=(ans+d[i][m])%10000;
    if (ans<10) printf("000%d\n",ans);
    else if (ans<100) printf("00%d\n",ans);
    else if (ans<1000) printf("0%d\n",ans);
    else printf("%d\n",ans);
  }
  return 0;
}
