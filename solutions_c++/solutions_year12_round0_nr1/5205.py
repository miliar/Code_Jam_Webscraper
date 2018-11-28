#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
char mymap[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main() {
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int cas;
  scanf("%d",&cas);
  cin.get();
  string str;
  for(int t=1;t<=cas;t++) {
    getline(cin,str);
    printf("Case #%d: ",t);
    for(int i=0;i<str.size();i++) {
      if(str[i]==' ')printf(" ");
      else printf("%c",mymap[str[i]-'a']);
    }
    printf("\n");
  }
  return 0;
}
