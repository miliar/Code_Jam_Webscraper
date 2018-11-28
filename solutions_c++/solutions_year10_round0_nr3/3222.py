#include<stdio.h>
#include<stdlib.h>
int main()
{
   int times,allseats,cases=1,i,j,groups,list[10],sum,tmpsum,k,check;
   FILE *output;
   FILE *input;
   output = fopen("out.txt","w");
   input = fopen("in.txt","r");
   fscanf(input,"%d",&cases);
   for(i=1;i<=cases;i++)
   {
      sum=0;
      k=0;
      fscanf(input,"%d%d%d",&times,&allseats,&groups);
      for(j=0;j<groups;j++)
         fscanf(input,"%d",&list[j]);
      
      while(times--)
      {
         tmpsum=0;
         check=0;
         while((tmpsum+list[k%groups])<=allseats)
         {
            tmpsum+=list[k%groups];           
            k++;
            check++;
            if(check==groups)
               break;
         }
         sum+=tmpsum;           
      }          
      fprintf(output,"Case #%d: %d\n",i,sum);                         
   }
   fclose(output);
   fclose(input);
   return 0;
}
