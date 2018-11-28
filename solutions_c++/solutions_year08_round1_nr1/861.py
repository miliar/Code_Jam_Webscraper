#include<iostream>
using namespace std;
#include<stdlib.h>

int compare_function1(const void *a,const void *b) 
{
    int *x = (int *) a;
    int *y = (int *) b;
    return *x - *y;
}

int compare_function2(const void *a,const void *b) 
{
    int *x = (int *) a;
    int *y = (int *) b;
    return *y - *x;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,N,A[10],B[10],i,j;
    long long mult=0;
    scanf("%d",&T);
    for (i=0;i<T;i++)
    {
        mult=0;
        scanf("%d",&N);
        for (j=0;j<N;j++)
            scanf("%d",&A[j]);
        for (j=0;j<N;j++)
            scanf("%d",&B[j]);
        qsort(A,N,4,compare_function1);
        qsort(B,N,4,compare_function2);
        for (j=0;j<N;j++)
            mult+=A[j]*B[j];
        printf("Case #%d: %lld\n",i+1,mult);
    }
    
}
