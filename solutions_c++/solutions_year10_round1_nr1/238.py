#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
const int M = 105;

char s[M][M];
char t[M][M];
int n, k;

int main() {
  int d;
  scanf("%d\n",&d);
  for(int tc=1;tc<=d;++tc) {
    scanf("%d %d\n",&n,&k);
    for(int i=1;i<=n;++i) {
      scanf("%s\n",s[i]+1);
    }
/*    printf("s:\n");
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n;++j) {
        printf("%c",s[i][j]);
      }
      printf("\n");
    }*/
    for(int i=1;i<=n;++i)
      for(int j=1;j<=n;++j)
        t[i][j]='.';
    for(int i=1;i<=n;++i){
      int ptr=0;
      for(int j=n;j>=1;--j) {
        if(s[i][j]!='.') {
          t[++ptr][i]=s[i][j];
        }
      }
    }
/*    printf("t:\n");
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n;++j) {
        printf("%c",t[i][j]);
      }
      printf("\n");
    }*/
    bool red=false,blue=false;
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i][j+p]!='R') jest=false;
        if(jest) red=true;
      }
    }
    for(int i=1;i<=n;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i][j+p]!='B') jest=false;
        if(jest) blue=true;
      }
    }
    for(int i=1;i<=n-k+1;++i) {
      for(int j=1;j<=n;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i+p][j]!='B') jest=false;
        if(jest) blue=true;
      }
    }
    for(int i=1;i<=n-k+1;++i) {
      for(int j=1;j<=n;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i+p][j]!='R') jest=false;
        if(jest) red=true;
      }
    }
    for(int i=1;i<=n-k+1;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i+p][j+p]!='R') jest=false;
        if(jest) red=true;
      }
    }
    for(int i=1;i<=n-k+1;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i+p][j+p]!='B') jest=false;
        if(jest) blue=true;
      }
    }
    for(int i=k;i<=n;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i-p][j+p]!='B') jest=false;
        if(jest) blue=true;
      }
    }
    for(int i=k;i<=n;++i) {
      for(int j=1;j<=n-k+1;++j) {
        bool jest=true;
        for(int p=0;p<k;++p)
          if(t[i-p][j+p]!='R') jest=false;
        if(jest) red=true;
      }
    }
    printf("Case #%d: ",tc);
    if(blue && red) printf("Both\n");
    else if(blue) printf("Blue\n");
    else if(red) printf("Red\n");
    else printf("Neither\n");
  }
  return 0;
}