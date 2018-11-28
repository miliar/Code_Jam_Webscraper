#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int A[1005];
int compare(const void *A,const void *B)
{   int p=*(int*)A;
    int q=*(int*)B;
    return q-p;
}
int main ()
{   int i,j,P,K,L,N,ct,flag;
    double tot;
    scanf("%d",&N);
    for(i=1;i<=N;i++)
    {   scanf("%d %d %d",&P,&K,&L);
        for(j=0;j<L;j++)
        {  scanf("%d",&A[j]);
        }
        qsort(A,L,sizeof(int),compare);
        tot=0.0;flag=0;
        ct=1;
        for(j=0;j<L;j++)
        {  tot+=(double)(ct)*(double)(A[j]);
           flag++;
           if(flag==K)
           {  ct++;flag=0;
           }
        }
        printf("Case #%d: %.0lf\n",i,tot);
    }
    
    return 0;
}
