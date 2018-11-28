#include<iostream>
using namespace std;
#include<stdlib.h>

int compare_function(const void *a,const void *b) 
{
    int *x = (int *) a;
    int *y = (int *) b;
    return *y - *x;
}

int main()
{
    freopen("A-large.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int T,P,L,K,num[1001],i,j,k,f;
    long long min=0;
    scanf("%d",&T);
    for (i=0;i<T;i++)
    {
        scanf("%d%d%d",&P,&K,&L);
        for (j=0;j<L;j++)
            scanf("%d",&num[j]);
        qsort(num,L,4,compare_function);
        min=0;
        for (j=0,f=1;j<L;f++)
            for (k=0;k<K && j<L;k++,j++)
                min+=f*num[j];
        printf("Case #%d: %lld\n",i+1,min);
    }
}
