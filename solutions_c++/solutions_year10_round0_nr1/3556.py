#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main (){
  int i,j,j2,n,num,tam,flag;
  char buffer[33]={0};
  FILE *in,*out;
  in=fopen("A-large.in","r");
//  in=fopen("ent.txt","r");
  out=fopen("sal.txt","w");
  
  fscanf (in,"%d",&n);
  for (j=0;j<n;j++){
      fscanf (in,"%d %d",&tam,&num);
      itoa (num,buffer,2);
      flag=1;
      for (i=strlen(buffer)-1,j2=0;j2<tam&&buffer[i]=='1';i--,j2++);
      if (j2<tam)
         fprintf(out,"Case #%d: OFF\n",j+1);
      else
         fprintf(out,"Case #%d: ON\n",j+1);
      }
  fclose(in);
  fclose(out);
  return 0;
}
