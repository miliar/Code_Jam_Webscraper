#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
   int n,k,cases=1;
   FILE *output;
   FILE *input;
   output = fopen("out.txt","w");
   input = fopen("in.txt","r");
   fscanf(input,"%d",&cases);
   for(int i=1;i<=cases;i++)
   {
      fscanf(input,"%d%d",&n,&k);
      if((k+1)%(int)pow(2,n)==0)
         fprintf(output,"Case #%d: ON\n",i);
      else
         fprintf(output,"Case #%d: OFF\n",i);
                          
   }
   fclose(output);
   fclose(input);
   system("pause");
   return 0;
}
