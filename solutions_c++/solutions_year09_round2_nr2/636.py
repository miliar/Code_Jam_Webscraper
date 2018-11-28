#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

using namespace std;

#define MAX 100

int cnt[10];

char str[MAX];

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int tests;
  scanf("%d",&tests);
  for(int test=1;test<=tests;++test) {
    scanf("%s",str);
    memset(cnt,0,sizeof(cnt));
    int l=strlen(str);
    for(int i=0;i<l;++i)
      cnt[str[i]-'0']++;
    printf("Case #%d: ",test);
    if(l==1) {
      printf("%s0\n",str);
      continue;
    }
    int ok=0;
    for(int k=l-1;k>0;--k) {
      if(str[k-1]<str[k]) {
        ok=1;
        char m=str[k];
        int j=k;
        for(int i=k+1;i<l;++i)
          if(str[i]<m && str[i]>str[k-1]) {
            m=str[i];
            j=i;
          }
        str[j]=str[k-1];
        str[k-1]=m;
        sort(str+k,str+l);
        break;
      }
    }
    if(!ok) {
      int k;
      for(k=1;k<10 && !cnt[k];++k);
      printf("%d",k);
      --cnt[k], ++cnt[0];
      for(int i=0;i<10;++i)
        for(int j=0;j<cnt[i];++j)
          printf("%d",i);
    }
    else printf("%s",str);
    printf("\n");
  }
  return 0;
}
