#include <stdio.h> 
#include <stdlib.h>
#include <math.h>

int main(void)
{
   int T; // numero de linhas
   int N; // numero de snappers
   int K; // numero de estalos
   int dec, i=0, j;
   int quoc, resto;
   
   FILE *fin = fopen("asmall.in","r");
   FILE *fout = fopen("asmall.out","w"); 
                
   fscanf(fin, "%d", &T);
   
   for(j=1;j<=T;j++)
   {
      fscanf(fin, "%d", &N);
      fscanf(fin, "%d", &K);
      
      dec = K;
      dec = dec % (int)pow(2,N);
      while (dec != 1)
      {     
         quoc= dec / 2;  
         resto = dec % 2;
         if(resto == 0)break;
       
         dec=quoc;      
         i++;
      }
      if((i==N-1) && (dec==1))fprintf(fout,"Case #%d: ON\n", j);
      else fprintf(fout,"Case #%d: OFF\n", j);
      i=0;
   }
   return(0);
}
