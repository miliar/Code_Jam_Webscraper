#include<cstdio>

int T,N;
int nums[21];
int sums[2000004];
int now_sum;

int main(){
 int t,i;
 int x,j;
 scanf("%d",&T);
 for(t=1;t<=T;t++){
  for(i=0;i<2000003;i++) sums[i]=0;
  printf("Case #%d:\n",t);
  scanf("%d",&N);
  for(i=0;i<N;i++) scanf("%d",nums+i);
  for(i=1;i<1048576;i++){
   x=i;
   j = 0;
   now_sum = 0;
   while(x>0){
    if(x%2==1) now_sum += nums[j];
    x/=2;
    j++;
   }
   if(sums[now_sum]>0){
    x = sums[now_sum];
    j = 0;
    while(x>0){
     if(x>1 && x%2==1) printf("%d ",nums[j]);
     if(x==1) printf("%d\n",nums[j]);
     x/=2;
     j++;
    }
    x = i;
    j = 0;
    while(x>0){
     if(x>1 && x%2==1) printf("%d ",nums[j]);
     if(x==1) printf("%d\n",nums[j]);
     x/=2;
     j++;
    }
    break;
   }
   sums[now_sum] = i;
  }
  if(i==1048576) printf("Impossible\n");
 }

 return 0;
}
