#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T,N;
    int *A;
    int min;
    int sum;
    int xorResult;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d",&N);
        A=(int*)malloc(sizeof(int)*N);

        for(int j=0;j<N;j++)
            scanf("%d",A+j);

        xorResult=A[0];
        sum=A[0];
        min=A[0];
        for(int j=1;j<N;j++)
        {
            if(A[j]<min)
               min=A[j];
            sum+=A[j];
            xorResult=xorResult xor A[j];
        }

        if(xorResult==0)
          printf("Case #%d: %d\n",i+1,sum-min);
        else
          printf("Case #%d: NO\n",i+1);

        free(A);

    }
    return 0;
}
