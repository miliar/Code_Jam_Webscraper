#include "stdio.h"

int t,n;
int c[1000];
int i,j,k;
int bit[20];
bool bener;
int min;
int total;

int main(){
    FILE *file;    
    file = fopen("output3.txt","w");
    scanf("%d", &t);
    for(i = 0; i < t; i++){
          min = 1000001;
          total = 0;
          bener = true;
          for(k = 0; k < 20; k++){
                bit[k] = 0;      
          }
          scanf("%d", &n);
          for(j = 0; j < n; j++){
                scanf("%d", &c[j]);
                if (min > c[j]) min = c[j];
                total += c[j];
                for(k = 0; k < 20; k++){
                      if(((c[j]>>k) & 1) == 1) bit[k]++;      
                }
          }          
          for(k = 0; k < 20; k++){
                if(bit[k] % 2 != 0) bener = false;     
          }
          if(bener){
                fprintf(file,"Case #%d: %d\n",i+1, total - min);          
          } else {
                fprintf(file,"Case #%d: NO\n",i+1); 
          }
    }
    fclose(file);
    return 0;    
}
