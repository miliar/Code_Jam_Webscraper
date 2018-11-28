#define MAX 105
#include<stdio.h>

char games[MAX][MAX];
long double rpi[MAX], wp[MAX], owpx[MAX][MAX], oowp[MAX], owp[MAX];

int main(){
  int N,T,wins,losses;
  scanf("%d\n",&T);
  for (int t=0; t<T; t++){
    scanf("%d\n",&N);
    for (int i=0; i<N; i++){
      wins = 0; losses = 0;
      for (int j=0; j<N; j++){
        char cc;
        scanf("%c",&games[i][j]); // 1 = i beats j
        if (games[i][j] == '1'){wins++;} else if  (games[i][j] == '0') losses++;
      }  
      scanf("\n");
      wp[i] = (long double)wins / (wins + losses);
    }
    
    for (int i=0; i<N; i++){   
      for (int j=0; j<N; j++){
        if (j != i){
          if (games[i][j] != '.'){
            wins = 0; losses = 0;
        
          // j = opponent, berechne average wp of games without i
          
            for (int k=0; k<N; k++){    
              if (k != i){                  
                if (games[j][k] == '1') wins++; else if  (games[j][k] == '0') losses++;
              }    
            }
            owpx[j][i] = (long double)wins / (wins + losses);
          }         
        }        
      }
    }
    for (int i=0; i<N; i++){ 
      owp[i]=0;
      int ct = 0;
      for (int j=0; j<N; j++) if ((j != i) && (games[i][j] != '.')){
        owp[i] += owpx[j][i];
        ct++;
      }  
      owp[i] /= ct;
    }
    for (int i=0; i<N; i++){  
      oowp[i] = 0;
      int ct=0;
      for (int j=0; j<N; j++){
        if ((j != i) && (games[i][j] != '.')){  
          oowp[i] += owp[j];
          ct++;
        }
      }  
      oowp[i] /= ct;
  //    printf("%llf %llf %llf\n",wp[i],owp[i],oowp[i]); 
      rpi[i] = wp[i]/4 + owp[i]/2 + oowp[i]/4; 
    }
    
    printf("Case #%d:\n",t+1);
    for (int i=0; i<N; i++) printf("%llf\n",rpi[i]); 
  }
  return 0;
} 

