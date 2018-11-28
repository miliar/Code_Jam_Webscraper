#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define N 30
char s[N], s2[N];

int out(char *s){
  int i=0;
  while (s[i]=='0')i++;
  return i;
}

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    scanf("%s",s2);
    int n = strlen(s2);
    memset(s,'0',sizeof(s));
    for (int i=0;i<n;i++)s[N-n+i]=s2[i];
    next_permutation(s,s+N);
    int x = out(s);
    printf("Case #%d: ",ti);
    for (int i=x;i<N;i++)printf("%c",s[i]);
    puts("");
  }
  
  return 0;
}
