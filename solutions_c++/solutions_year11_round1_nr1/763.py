#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int gcd(int x,int y){
 if (x%y==0)   
  return y;
 return gcd(y,x%y);  
}
long long pd,pg,n;
int main(){
  int t,i,j,k;
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  scanf("%d",&t);
  for (k=1;k<=t;k++){
      cin>>n>>pg>>pd;
      printf("Case #%d: ",k);
      if (pd==pg&&pg==0){
        printf("Possible\n");  
        continue;              
      }
      if (pd==0&&pg>0){
        printf("Broken\n");  
        continue;                             
      }
      if (pg<100&&pd==100){
        printf("Broken\n");  
        continue;                             
      }
      j=100/(gcd(100,pg));
      if (j<=n) printf("Possible\n"); 
      else printf("Broken\n");
  }  
  return 0;   
}
