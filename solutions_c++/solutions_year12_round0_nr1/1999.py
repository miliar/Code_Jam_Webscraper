#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int maxn=102;
int f[26]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};
char a[maxn];
int n;

int main(){
  int i,k;
  scanf("%d\n",&n);
  for (k=1;k<=n;k++){
    gets(a);
    printf("Case #%d: ",k);
    for (i=0;i<strlen(a);i++)
      if (a[i]==' ') printf(" ");
      else printf("%c",f[a[i]-'a']);
    printf("\n");
  }
  return 0;
}
