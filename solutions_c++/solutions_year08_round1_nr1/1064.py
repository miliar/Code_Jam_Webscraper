#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N;
int A[10];
int B[10];

int findminA(int i)
{
    int r;
    r=i;
    for(;i<=N;i++)
    {
        if(A[r]>A[i])
        {   
            r=i;
        }
    }
    return r;
}

int findminB(int i)
{
    int r;
    r=i;
    for(;i<=N;i++)
    {
        if(B[r]>B[i])
        {   r=i;
        }
    }
    return r;
}

int arrange()
{
    int i,j,k;
    for(i=1;i<=N;i++)
    {
        j=findminA(i);
        k=A[i];
        A[i]=A[j];
        A[j]=k;
        j=findminB(i);
        k=B[i];
        B[i]=B[j];
        B[j]=k;
    }   
}

int findproduct()
{
    int r=0,i,j;
    j=N/2;
    for(i=1;i<=N;i++)
    {
        r=(A[i]*B[N-i+1])+r;
    }

    return r;
}
        
int main()
{
    int T,i,j,k,r;
    FILE *fp;
        if((fp = fopen("KVS1", "w"))==NULL)
        {
            exit(1);
        }

    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        N=0;
        scanf("%d",&N);
        for(j=1;j<=N;j++)
        {
            scanf("%d",&A[j]);
        }
        
        for(j=1;j<=N;j++)
        {
            scanf("%d",&B[j]);
        }
    
        arrange();
        r=findproduct();      
        fprintf(fp,"Case #%d: %d\n",i,r);
    }
    fclose(fp);
    
return 0;
}
