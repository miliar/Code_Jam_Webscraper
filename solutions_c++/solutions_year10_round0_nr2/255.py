#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

int gcd(int a,int b){
  int mem;
  if(a<b)swap(a,b);
  while((mem=a%b)>0){
    a=b;
    b=mem;
  }
  return b;
}

int main(){
  int c;
  scanf(" %d",&c);
  for(int i=0;i<c;++i){
    int n;
    int t[1000];
    scanf(" %d",&n);
    for(int j=0;j<n;++j){
      scanf(" %d",t+j);
    }
    int buf;
    for(int j=1;j<n;++j){
      if(t[j]!=t[0]){
        buf=abs(t[j]-t[0]);
        break;
      }
    }
    for(int j=1;j<n;++j){
      if(t[j]==t[0])continue;
      buf=gcd(buf,abs(t[j]-t[0]));
    }
    printf("Case #%d: %d\n",i+1,(buf-t[0]%buf)%buf);
  }
  return 0;
}
