#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;


int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int n,k;
    scanf("%d%d",&n,&k);
    printf("Case #%d: %s\n",++ca,((k&((1<<n)-1))==(1<<n)-1)?"ON":"OFF");
  }
  return 0;
}
