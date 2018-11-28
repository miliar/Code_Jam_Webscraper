#include <iostream>
#include <fstream>
using namespace std;

long T;
long R;
long K;
long N;
long* G;
long money;
long front,sum;

int main()
{
    int i,j,k,l;
    G=new long[10000000];
    freopen("small.in","r",stdin);freopen("small.out","w",stdout);
    
    scanf("%d\n",&T);
    for(i=1;i<=T;i++)
    {
        money=0;
        scanf("%d",&R);
        scanf("%d",&K);
        scanf("%d",&N);
        for(j=0;j<N;j++)
            scanf("%d",&G[j]);
        front=0;
        for(j=0;j<R;j++)
        {
            sum=0;
            for(k=0;k<N && sum+G[front]<=K;k++)
            {
                sum+=G[front];
                money+=G[front];
                if(front == N-1)
                    front=0;
                else
                    front++;
            }
        }
        
        printf("Case #%d: %ld\n",i,money);
    }
    
    fflush(stdout);
    return 0;
}
