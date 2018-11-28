#include <stdio.h>
#include <math.h>
#include <io.h>
#include <stdlib.h>

void check(long n,long k,long i);
     FILE * pFile;
     FILE * rFile;
int main() {
           pFile = fopen("test.txt","w");
          if((rFile=fopen("A-large.in","r")) == NULL) {
           printf("Cannot open file.\n");
             //exit(1);
              }
              
         //rFile = fopen("t.txt","w+");
        // rewind (pFile);
    long ncase;
    long n,k;
    fscanf(rFile,"%d",&ncase);
    for(long i =1;i<=ncase;i++){
            fscanf(rFile,"%d %d",&n,&k);
         //   printf("%d %d",n,k);
         check(n,k,i);
    }
    fclose(pFile);
    fclose(rFile);
        //    getchar();getchar();
    
return 0;
}
void check(long n,long k,long i) {
     long pow1 = (long)pow(2,n);
     long cal = (k+1)%pow1;
     if(cal != 0) fprintf(pFile,"Case #%d: OFF\n",i);
     else fprintf(pFile,"Case #%d: ON\n",i);
     }
