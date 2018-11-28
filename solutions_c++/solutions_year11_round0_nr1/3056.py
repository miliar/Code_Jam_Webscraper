#define MAX 101

#include<stdio.h>
#include<cstdlib>

int positions[MAX],positionsO[MAX],positionsB[MAX];
char robot[MAX];

int main(){
  int T,N;
  scanf("%d\n",&T);
  for (int i=0; i<T; i++){
    scanf("%d ",&N);
    int posO=1, posB=1, lengthO=0,lengthB=0;
    for (int j=0; j<N; j++){
      scanf("%c ",&robot[j]);
      scanf("%d ",&positions[j]);
      if (robot[j] == 'O'){
        positionsO[lengthO] = positions[j];
        lengthO++;
      }else{
        positionsB[lengthB] = positions[j];
        lengthB++;
      }
    }
    scanf("\n");
    
    int count=0, dif, indexnextO=0, indexnextB=0;
    for (int j=0; j<N; j++){
      if (robot[j]=='O'){
        dif = std::abs(positions[j]-posO)+1;
        count += dif;
        posO = positions[j];
        indexnextO++;       
        if (posB >= positionsB[indexnextB]){          
          if (posB-positionsB[indexnextB] < dif){    
            posB = positionsB[indexnextB];
          }else{
            posB -= dif;
          }
        }else{
          if (-posB+positionsB[indexnextB] < dif){
            posB = positionsB[indexnextB];
          }else{
            posB += dif;
          }
        }
      }else{
        dif = std::abs(positions[j]-posB)+1;
        count += dif;
        posB = positions[j];
        indexnextB++;       
        if (posO >= positionsO[indexnextO]){
          if (posO-positionsO[indexnextO] < dif){
            posO = positionsO[indexnextO];
          }else{
            posO -= dif;
          }
        }else{
          if (-posO+positionsO[indexnextO] < dif){
            posO = positionsO[indexnextO];
          }else{
            posO += dif;
          }
        }
      }
    }
    printf("Case #%d: %d\n",i+1,count);
  }
  return 0;
} 
