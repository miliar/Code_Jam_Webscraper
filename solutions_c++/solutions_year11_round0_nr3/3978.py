#include<iostream>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,M,N,A[20],i,j,k,l;
    scanf("%d",&T);
    for (i=0; i<T; i++)
    {
        scanf("%d",&N);
        for (j=0;j<N;j++)
            scanf("%d",&A[j]);
        k=1<<N;
        M=0;
        for (j=1;j<k-1;j++)
        {
            int sum=0, sum1=0, sum2=0;
            for (l=0;l<N;l++)
            {
                if ((j & (1<<l)) == (1<<l))
                {
                   sum+=A[l];
                   sum1^=A[l];
                }
                else
                    sum2^=A[l];
            }
            if (sum1==sum2 && sum>M)
               M=sum;
        }
        printf("Case #%d: ",i+1);
        if(M)
             printf("%d\n",M);
        else
            printf("NO\n");
    }
}
