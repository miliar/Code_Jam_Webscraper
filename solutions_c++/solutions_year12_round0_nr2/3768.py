#include<cstdio>

int t,n,s,p,score;

int main(){
  scanf("%d",&t);
  for(int ccase = 1;ccase<=t;ccase++){
    scanf("%d",&n);
    scanf("%d",&s);
    scanf("%d",&p);
    int surpriseBound = 3*p-4;
    int regularBound = 3*p-2;
    int count = 0;
    for(int i = 0;i<n;i++){
      scanf("%d",&score);
      if(score>=regularBound){
        count++;
        continue;
      }
      if(p>1 && score >= surpriseBound && s>0){
        count++;
        s--;
      }
    }
    printf("Case #%d: %d\n",ccase,count);
  }
  return 0;
}
