#include<stdio.h>
#include<Math.h>
FILE *f1=fopen("A-large.in","r");
FILE *f2=fopen("snpr2.out","w");
int main()
{
 int t,i,n,k;
 fscanf(f1,"%d",&t);
 printf("T=%d\n",t);
  for(i=0;i<t;i++)
  {
    fscanf(f1,"%d%d",&n,&k);
   fprintf(f2,"Case #%d: ",i+1); 
   if((k+1) % (int)pow(2,n) == 0)
   {
   fprintf(f2,"ON\n");
   }
   else
    fprintf(f2,"OFF\n");
  }
}
