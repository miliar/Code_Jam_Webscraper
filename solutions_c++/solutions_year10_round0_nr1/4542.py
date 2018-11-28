//Google Code Jam 2010
//Qualification Round 2010
//Snapper Chain
//David Grilli
//djgrill@gmail.com

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <math.h>

int main()
{
 int t=0,k=0,n=0,i=0,j=0;
 char *line=new char;
 char *split;
 char *salida;
 
 FILE *in,*out;
 in=fopen("A-small-attempt0.in","rt");
 out=fopen("A-small-attempt0.out","w");
 t=atoi(fgets(line,10,in));
 
 if((t>=1)&&(t<=10000))
 {
  for(i=1;i<=t;i++)
  {
   fgets(line,10,in);
   split=strtok(line," \n");
   n=atoi(split);
   split=strtok(NULL," \n");
   k=atoi(split);
   
   if((n<1)||(n>10)||(k<0)||(k>100))
    fprintf(out,"Case #%i: error with the number of snappers or finger snappes",i);
   else if(k==0)
    fprintf(out,"Case #%i: OFF\n",i);
   else if((k+1)%(int)pow(2,n)==0)
    fprintf(out,"Case #%i: ON\n",i);
   else
    fprintf(out,"Case #%i: OFF\n",i);
  }
 }
 else
  fprintf(out,"error, too many tests");
  
 fclose(in);
 fclose(out);
}
