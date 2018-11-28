#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int P,K,L;
int A[101][2]={0};
int B[101]={0};
int C[101]={0};

int set()
{
    int i;
    for(i=1;i<101;i++)
    {
        A[i][0]=0;
        A[i][1]=0;
        B[i]=0;
        C[i]=0;
    }
    P=0;
    K=0;
    L=0;
    return 0;
}
    

int findlargest(int i)
{
    int j;
    for(j=i;j<=L;j++)
    {
        if(C[i]<C[j])
            i=j;
    }
return i;    
}

int  arrange()
{
    int i,j,k;
    for(i=1  ;i<=L   ;i++)
    {
        C[i]=A[i][0];
    }
    for(i=1; i<=L;i++)
    {
        j=findlargest(i);
        k=C[i];
        C[i]=C[j];
        C[j]=k;
    }
return 0;
}

int find(int j)
{
    int i;
    for(i=1;i<=L;i++)
    {
        if(A[i][0]==j)
        {
            if(A[i][1]==0)
            {
                A[i][1]=1;
                return i;
            }
        }
    }
return L;
}

int layout()
{
    int i,j,k,t=1,q=1;
    for(i=1;i<=L;i++)
    {
        j=C[i];
        k=find(j);
        B[k]=t;
        q++;
        if(q>K)
        {    
            t++;
            q=1;
        }        
    }
return 0;
}

int calculate()
{
    int i,r=0;
    printf("r=%d",r);
    for(i=1;i<=L;i++)
    {
        printf("r=%d\n",r);
        r=(A[i][0]*B[i])+r;
    }
    return r;
}

int main()
{
    int N,i,j,result;

    FILE *fp;
        if((fp = fopen("KVS1", "w"))==NULL)
        {
            exit(1);
        }

    scanf("%d",&N);
    
    for(i=1;i<=N;i++)
    {
        set();
        scanf("%d %d %d",&P, &K, &L);
        for(j=1  ;j<=L   ;j++)
        {
            scanf("%d",&A[j][0]);
        }
            arrange();
            layout();
            result=calculate();
            fprintf(fp,"Case #%d: %d\n",i,result);
            printf("Case #%d: %d\n",i,result);
    }
    fclose(fp);
return 0;
}
