#include <stdio.h>
#include <stdlib.H>

int main(){
int r=0, k=0, n=0;
int i,j, t=0,tt,tot, volta, g[10], temp;
scanf ("%i",&t);
for (temp = 1; temp<=t;temp++){
    i=tt=tot=volta=j=0;
    scanf ("%i",&r);
    scanf ("%i",&k);
    scanf ("%i",&n);
    for (i=0;i<n;i++){
       scanf("%i",&g[i]);    
    }
        i=0;
        do{
           if (tt+g[i]<=k){
              tt=tt+g[i];
              tot=tot+g[i];
              i++;
              j++;
              if (i==n){
                 i=0;         
              }
              if(j==n){
                 j=0;
                 volta++;
                 tt=0;
                 if (volta == r){
                  break;          
                 }          
              }               
           }else{
              volta++;
              tt=0;
              j=0;
              if (volta == r){
                  break;          
              }      
           }    
        }while (1);   
        printf ("Case #%i: %i\n",temp, tot);   
    }
return 0;    
}
