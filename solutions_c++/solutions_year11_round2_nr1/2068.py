#include <iomanip>
#include <stdio.h>
#include <map>
#include <set>

using namespace std;
int main(){
  FILE *in = fopen("A-large-0.in","r");
  FILE *out = fopen("small.out","w");
  int T;
  fscanf(in,"%d ", &T);
  for (int t = 0; t < T; t++){
    double WP[110]={}, OWP[110]={}, OOWP[110]={};
    int played[110]={};
    int table[110][110];
    int N; char tmpc;
    fscanf(in,"%d ", &N);
    for (int i = 0; i < N; i++){
      for (int j = 0; j< N; j++){
        fscanf(in," %c ",&tmpc);
        if(tmpc == '.') table[i][j]=-1;
        if(tmpc == '0') {table[i][j]=0; played[i]++;}
        if(tmpc == '1') {table[i][j]=1; played[i]++;}
      }
    }

    for (int i = 0; i < N; i++){
      for (int j = 0; j< N; j++){
        if(table[i][j] ==1)   WP[i]++;
      }
        WP[i]/=played[i];
//        printf("WP %d %lf %d\n", i,WP[i], played[i]); 
    }
    for (int i = 0; i < N; i++){
        int count=0;
        for (int j = 0; j< N; j++){
          if(table[i][j]!=-1) {
            count++;
            OWP[i] +=(WP[j]*played[j]-table[j][i])/(played[j]-1);
          }
        }
        OWP[i]/=count;
  //      printf("OWP %d %lf %d\n", i,OWP[i], count); 
    }
    for (int i = 0; i < N; i++){
        int count=0;
        for (int j = 0; j< N; j++){
          if(table[i][j]!=-1) {
            count++;
            OOWP[i] += OWP[j];
          }
        }
        OOWP[i]/=count;
    }
    printf("Case #%d:\n",t+1);
      for (int i = 0; i < N; i++){
      printf("%.20lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
    } 

  }
    
}
