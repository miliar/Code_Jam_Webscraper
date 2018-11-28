#include <stdio.h>
#include <string.h>
#include <conio.h>
#include <stdlib.h>

int main(){
    FILE *out,*in;
    in=fopen("A-large.in","r");
    out=fopen("sal.txt","w");
    int t,n,k,l,i,j,t2;
    char c[30]={NULL};
    fscanf(in,"%d",&t);
    t2=1;
    while (t2<=t){
          fscanf(in,"%d %d",&n,&k);          
          itoa(k,c,2);
          l=strlen(c);
          for (i=l-1,j=0;j<n&&c[i]=='1';i--,j++);
          fprintf(out,"Case #%d: ",t2);
          if (j==n)
             fprintf(out,"ON\n");
             else
                 fprintf(out,"OFF\n");            
          t2++;
          }    
    fclose (in);
    fclose (out);
    return 0;
    }
