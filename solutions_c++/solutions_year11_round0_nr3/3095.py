#define MAXN 1001
#define MAXPOWER 20

#include<stdio.h>

int powers[MAXPOWER], count[MAXPOWER];

int main(){
  powers[0] = 1;
  for (int i=1; i<MAXPOWER; i++){ 
    powers[i] = powers[i-1]*2;
  }
  
  int T;  
  scanf("%d\n",&T);
  for (int tt=0; tt<T; tt++){
    for (int i=0; i<MAXPOWER; i++) count[i] = 0;
    int smallest = 99999999, sum = 0;
    int N;
    scanf("%d\n",&N);
    int value;
    for (int i=0; i<N; i++){
      scanf("%d ",&value);
      if (value < smallest) smallest = value;
      sum += value;
      int temp = value;
      for (int j=MAXPOWER-1; j>=0; j--){       
        if (temp >= powers[j]){
          temp -= powers[j];
          count[j]++;
        }
      }
    }  
    scanf("\n");
    
    bool works = true;
    for (int i=0; i<MAXPOWER; i++){
      if (count[i] % 2 == 1){
        works = false;
      }
    }
    
    if (works){
      printf("Case #%d: %d\n",tt+1,sum-smallest);
    }else{
      printf("Case #%d: NO\n",tt+1);
    }
  }
  return 0;
} 
