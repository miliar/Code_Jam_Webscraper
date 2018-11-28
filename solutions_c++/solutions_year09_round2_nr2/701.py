#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
char a[77];
int main(){
  int test;
  scanf("%d",&test);
  int testi;
  for(testi=1;testi<=test;++testi){
    scanf("%s",a);
    printf("Case #%d: ",testi);
    if(!next_permutation(a,a+strlen(a))){
      char*p=a;
      while(*p==48)++p;
      putchar(*p);
      *p=48;
    }
    printf("%s\n",a);
  }
  return 0;
}