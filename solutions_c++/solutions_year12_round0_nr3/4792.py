#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int swap(int i, int numSwap){
 char a[50];
 itoa(i,a,10);
 char temp[50];
 itoa(i,temp,10);
 int l,k, pos;
 
      for(k=0;k<strlen(a);k++){
         pos = (k + numSwap)%strlen(a);
         temp[pos] = a[k];
      }
    
     int j = atoi(temp);
     
     return j;
}

int recycle(int lower, int upper, int numDigit, int count){
    int i, j, k;
    if(numDigit == 0) return count;
    
    for(i=lower; i<=upper; i++){
       k = swap(i,numDigit);
       if(k<=upper && k > i){ 
          count++;
          //printf("%d, %d\n",k,i);
          }                         
    }   
    
    return recycle(lower,upper,numDigit-1,count);
}




int main(){
 FILE * in = fopen("C-small-attempt0.in","r");
 FILE * out = fopen("output.txt", "w");
 
 int T, i, j;
 int pair[50][50];
 fscanf(in,"%d", &T); 
    
    for(i = 0; i < T; i++){
      for(j=0;j<2;j++){
         fscanf(in,"%d", &pair[i][j]);          
      }        
    }
    
   
   for(i=1;i<=T;i++){ 
    char a[50];
    itoa(pair[i-1][0],a,10);
    int count = 0;
    count = recycle(pair[i-1][0], pair[i-1][1], strlen(a)-1,count);
    printf("Case #%d: %d\n",i,count);
    fprintf(out,"Case #%d: %d\n",i,count);
   }
    system("pause");
    
}


