#include<iostream>
#include<cstring>
#include<cstdio>
#include<cstdlib>
using namespace std;

int gcd(int a,int b){return b?gcd(b,a%b):a;}
int a[1010],b[1010];
int main(){
  int Cas,ca=0;
  scanf("%d",&Cas);
  while(Cas--){
    int i,n;
    scanf("%d",&n);
    for(i=0;i<n;++i){
      scanf("%d",a+i);
      if(i)b[i-1]=abs(a[i]-a[i-1]);
    }
    int res=b[0];
    for(i=1;i<n-1;++i){
      res=gcd(res,b[i]);
    }
    int X=(res-(a[i]%res))%res;
    printf("Case #%d: %d\n",++ca,X);
  }
  return 0;
}
