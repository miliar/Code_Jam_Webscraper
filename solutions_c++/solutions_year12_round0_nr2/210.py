#include <stdio.h>
#include <stdlib.h>
#include <conio.h>


int main()
{

FILE * f, * g;
f=fopen("B-large.in","r");
g=fopen("output.out","w");


int T,N,S,p,i,j,sum,total=0,total_s=0,total1=1,min,max;

fscanf (f,"%d",&T);

for (i=1;i<=T;i++)
    {
    total=0;
    total_s=0;
    total1=0;
    
    fscanf(f,"%d",&N);     
    
    fscanf(f,"%d",&S);     
    
    fscanf(f,"%d",&p);     
    
    if(p>=2)
    {
            
    min=3*p-5;
    
    max=3*p-2;
    
    for (j=1;j<=N;j++)
        {
        fscanf(f,"%d",&sum);            
        
        if (sum>=max) total++;
        
        if (sum>min && sum<max) total_s++;               
        }

    if (total_s>=S) total=total+S;
    
    if (total_s<S) total=total=total+total_s;
    
    fprintf(g,"Case #%d: %d",i,total);
    
    if (i<T) fprintf(g,"\n");
    }
    
    if (p<2)
    {   
    for (j=1;j<=N;j++)
        {
        fscanf(f,"%d",&sum);              
        
        if (sum>0) total1++;
                      
        }
    
    if (p==1) fprintf(g,"Case #%d: %d",i,total1);
    
    if (p==0) fprintf(g,"Case #%d: %d",i,N);
    
    if (i<T) fprintf(g,"\n");
    }
    
  
    }

return 0;
}



