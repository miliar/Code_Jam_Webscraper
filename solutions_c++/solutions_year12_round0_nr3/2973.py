#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
    FILE* input=fopen("input.in","r");
    FILE* output=fopen("output.out","w");
    
    int T,A,B;
    
    fscanf(input,"%d",&T);
    
    for(int k=0; k<T; k++)
    {
           fscanf(input,"%d",&A);
           fscanf(input,"%d",&B);
           int count=0;
           for(int i=A; i<=B; i++)
           {
               int digits=1;
               int temp=i;
               while((temp/=10)>0) digits++;
               temp=i;
               
               for(int p=0; p<digits; p++)
               {
                      int powerof=1;
                      for(int m=0;m<digits-1;m++) powerof*=10;
                      temp=powerof*(temp%10)+temp/10; 
                      if(temp>i && temp>=A && temp<=B){ printf("%d %d %d\n",i,temp, count); count++;}
                       
               } 
           
                   
           }
           
           fprintf(output,"Case #%d: %d\n", k+1,count); 
            
    }
    
    fclose(output);
    system("PAUSE");
    return 0;   
}
