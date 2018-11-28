#include <stdio.h>
#include <string.h>
int i,j,n,m,tt,T;
char s[44][111],t[111],a[222];
int main() {
  freopen("a.in","r",stdin);
  scanf("%d\n",&n);
  for (i=0; i<n; i++) gets(s[i]);
  for (i=0; i<n; i++) {
    gets(t);
    m=strlen(t);
    for (j=0; j<m; j++) a[s[i][j]]=t[j];
  }
  a['z']='q'; a['q']='z';
  freopen("a-small.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d\n",&tt);
  for (T=1; T<=tt; T++) {
    gets(t);
    printf("Case #%d: ",T);
    m=strlen(t);
    for (i=0; i<m; i++) putchar(a[t[i]]);
    puts("");
  }
  return 0;
}
