#include<stdio.h>
#include<stdlib.h>
#include<math.h>

FILE *f,*f2;

int main()
{
    f=fopen("C-large.in","r");
    f2=fopen("C-large.out","w");
    int T,N;
    fscanf(f,"%d",&T);
    for(int i=0;i<T;i++)
    {
            fscanf(f,"%d",&N);
            long int sum=0;
            long int xo=0;
            long int min=10000000;
            for(int j=0;j<N;j++)
            {
                    long int a;
                    fscanf(f,"%ld",&a);
                    //printf("%d ",a);
                    sum=sum+a;
                    xo=xo^a;
                    if(a<min)
                                min=a;
            }            
            if(xo==0l)
                      fprintf(f2,"Case #%d: %ld\n",i+1,sum-min);
            else
                      fprintf(f2,"Case #%d: NO\n",i+1);
    }
}
                    
    
