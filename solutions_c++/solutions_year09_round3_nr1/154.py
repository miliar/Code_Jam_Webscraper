#include <iostream>
#include <stdio.h>

using namespace std;

long long solve(char* l) {
  int len = strlen(l);
  int a[256];
  for (int i=0;i<256;++i)
    a[i]=-1;
  int cur = 0;
  a[l[0]] = 1;  
  for (int i=1;i<len;++i) {
    if (a[l[i]]==-1) {
      a[l[i]] = cur;
      if (!cur) { ++cur; }
      ++cur;
    }
  }
  if (cur < 2) {
    cur = 2;
  }
  long long res = 0;
  for (int i=0;i<len;++i) {
      res *= cur;
     res += a[l[i]];
    }
 return res;
       }
  
int main() {
  int T;
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d\n",&T);
  char l[100];
  for (int i=1;i<=T;++i) {
    gets(l);
    printf("Case #%d: %ld\n",i,solve(l));
  }
  return 0;
}
