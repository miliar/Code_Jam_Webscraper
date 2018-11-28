#include<stdio.h>
#include<stdlib.h>
#include<math.h>

FILE *f,*f2;

int main()
{
    f=fopen("D-large.in","r");
    f2=fopen("D-large.out","w");
    int T,N;
    fscanf(f,"%d",&T);
    //scanf("%d",&T);  
    for(int i=0;i<T;i++)
    {
            fscanf(f,"%d",&N);
            //scanf("%d",&N);
            long int s=0;
            for(int j=1;j<=N;j++)
            {
                    long int a;
                    //scanf("%d",&a);
                    fscanf(f,"%d",&a);
                    if(j!=a)
                            s++;
            }
            fprintf(f2,"Case #%d: %ld.000000\n",i+1,s);
            //printf("Case #%d: %ld.000000\n",i+1,s);
    }
}
                            
