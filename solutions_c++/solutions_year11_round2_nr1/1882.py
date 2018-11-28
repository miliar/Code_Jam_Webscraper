#include <stdio.h>
#include <stdlib.h>
#include <string.h>


using namespace std;

double wp[105][2], owp[105], oowp[105];
int t, ncase, i, n;
char sche[105][105];
void _wp(int k){
    int i;
    double total, win;
    total = 0; win = 0;
    for(i=0; i < n; i++){
      if(sche[k][i] == '.') continue;
      total++;
      if(sche[k][i] == '1') win++;
    }
    wp[k][0] = win;
    wp[k][1] = total;
}

void _owp(int k){
     int i, count;
     double total;
     total = 0;
     count = 0;
     for(i=0; i < n; i++){
       if(sche[k][i] == '.') continue;
       if(sche[i][k] == '1'){
         total += (wp[i][0]-1)/(wp[i][1]-1);
       }
       if(sche[i][k] == '0'){
         total += wp[i][0]/(wp[i][1]-1);
       }
       count++;
     }
     owp[k] = total/count;
}

void _oowp(int k){
     int i, count;
     double total;
     total = 0; count=0;
     for(i=0; i < n; i++){
       if(sche[k][i] == '.') continue;
       total += owp[i];
       count++;
     }
     oowp[k] = total/count;
}


int main(){
    
    freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
    
    scanf("%d", &t);
    for(ncase=1; ncase <= t; ncase++){
      scanf("%d", &n);
      for(i=0; i < n; i++){
        scanf("%s", &sche[i]);
        //printf("%s\n", sche[i]);        
      }
      
      //printf("wp:\n");
      for(i=0; i < n; i++){
        _wp(i);
        //printf("%f/%f\n", wp[i][0], wp[i][1]);
      }
      
      //printf("owp:\n");
      for(i=0; i < n; i++){
        _owp(i);
        //printf("%f\n", owp[i]);
      }
      
      //printf("owp:\n");
      for(i=0; i < n; i++){
        _oowp(i);
        //printf("%f\n", oowp[i]);
      }
      
      printf("Case #%d:\n", ncase);
      for(i=0; i < n; i++)
        printf("%f\n", 0.25*(wp[i][0]/wp[i][1]) + 0.50*owp[i] + 0.25*oowp[i]);
    }
    return 0;
}
