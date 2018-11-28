#include <iostream>
#include <cstring>
#include <cmath>
#define N 1100
  using namespace std; 
int main(){
  freopen("c.in","r",stdin);freopen("c.out","w",stdout);
  int tc,tt;
  int i,j,k,x,sum,min,all;
  int n;
  scanf("%d",&tc);
  for(tt=1;tt<=tc;tt++){
    printf("Case #%d: ",tt);
    scanf("%d",&n);
    sum=all=0;
    min=10000000;
    while(n--){
      scanf("%d",&x);
      sum+=x;
      all^=x;
      if(x<min)min=x;
      }
    if(all!=0)printf("NO\n");
    else printf("%d\n",sum-min);
    }
  return 0;
}
    
