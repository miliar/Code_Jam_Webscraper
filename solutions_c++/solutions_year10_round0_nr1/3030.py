#include <cstdio>

int po(int n){
  int ans=1;
  for(int i=0;i<n;i++){
    ans*=2;
  }
  return ans;
}


int main(){
  int t;
  scanf("%d",&t);
  for(int i=0;i<t;i++){
    int n,k;
    scanf("%d%d",&n,&k);
    printf("Case #%d: ",i+1);
    if((k+1)%po(n)==0)printf("ON\n");
    else printf("OFF\n");
  }
}
