#include <stdio.h>

int main(){
  freopen("B-large.in","r",stdin);
  freopen("B.out","w",stdout);
  int t,t1=0;
  scanf("%d",&t);
  while(t--){
    t1++;
    int n,s,p;
    scanf("%d%d%d",&n,&s,&p);
    int sum[110];
    for(int i=0;i<n;i++){
      scanf("%d",&sum[i]);
    }
    int too = 0;
    for(int i=0;i<n;i++){
      if(sum[i] >=3)
      switch(sum[i]%3){
        case 1:
             if(((sum[i]/3) +1)>= p) too++;
             break;
        case 2:
             if(((sum[i]/3) +1)>= p) too++;
             else if(s>0 && ((sum[i]/3)+2)>=p ) {too++; s--;}
             break;
        case 0:
             if((sum[i]/3)>= p) too++;
             else if(((sum[i]/3) +1)>= p && s>0) {too++; s--;} 
             break;
        default: break;
      }
      else{
        if(sum[i]==0){
          if(p==0) too++;
        }
        else if(sum[i]==1){
          if(p<=1) too++;
        } 
        else if(sum[i]==2){
          if(s>0 && p==2) {too++; s--;}
          else if(p<2) too++;
        }
      }
    }
    printf("Case #%d: %d\n",t1,too);
  }
  return 0;
}
