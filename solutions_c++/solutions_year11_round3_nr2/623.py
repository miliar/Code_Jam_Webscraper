#include <cstdio>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)

#define MAX 1005

int parsecs[MAX];

int main(){
  long long T,L,t,N,C,i,j,sum;
  int a;
  scanf("%Ld\n",&T);
  REP(a,T){
    scanf("%Ld %Ld %Ld %Ld ",&L,&t,&N,&C);
 //   printf("%Ld\n",t);
    REP(i,C){
      scanf("%d ",&parsecs[i]);
    }
    scanf("\n");
    if (L == 0){
      sum = 0;
      REP(i,N){
        sum += parsecs[i%C];
      }
      printf("Case #%d: %Ld\n",a+1,2*sum);
    }else if (L == 1){
      long long best = 1000000000;
      for (int i=0; i<N; i++){
        // put it on i
  //      int time = 0;
        sum = 0;
        REP(j,N){
          if ((j == i) && (sum >= t)) sum += parsecs[i%C]; else{
            if ((j == i) && (sum < t) && (sum + 2*parsecs[i%C] > t)){
              sum += parsecs[i%C] + (t - sum)/2;
            }else{
              sum += 2*parsecs[j%C];
             // printf("h %d\n",2*parsecs[i%C]);
            }
          }
  //        printf("%d\n",sum);
        }
        if (sum < best) best = sum;
      }
      printf("Case #%d: %Ld\n",a+1,best);
    }else{
      long long best = 1000000000;
      for (int i=0; i<N; i++){
        long long best1 = 1000000000;
        for (int k=i+1; k<=N; k++){  
          sum = 0;
          REP(j,N){
            if ((j == i) && (sum >= t)) sum += parsecs[j%C]; else{
              if ((j == k) && (sum >= t)) sum += parsecs[j%C]; else{
                if ((j == i) && (sum < t) && (sum + 2*parsecs[i%C] > t)){
                  sum += parsecs[i%C] + (t - sum)/2;
                }else{
                  if ((j == k) && (sum < t) && (sum + 2*parsecs[k%C] > t)){
                    sum += parsecs[k%C] + (t - sum)/2;
                  }else{
                    sum += 2*parsecs[j%C];
                  }
                }
              }
            }
          }
    //      printf("s %d\n",sum);
          if (sum < best1) best1 = sum;
        }
        if (best1 < best) best = best1;
      }
      printf("Case #%d: %Ld\n",a+1,best);
    }   
  }
  return 0;
}
 
