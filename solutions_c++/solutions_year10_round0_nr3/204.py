#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int T,R,K,N,arr[1001];
long long res;
struct Link
{
    int v;
    int next;
};
Link line[1001];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d %d %d",&R,&K,&N);
        res=0;
        for(j=0;j<N;j++)
        {
            scanf("%d",arr+j);
            line[j].v = 0;
            line[j].next = -1;
            res += arr[j];
        }
        printf("Case #%d: ",i);
        if( res<=K )
        {
            res = res*R;
            printf("%lld\n",res);
        }
        else
        {
            res = 0;
            for(j=0;j<N;j++)
            {
                k = j;
                int tmp=0,pre;
                while(tmp<=K)
                {
                    pre = tmp;
                    tmp += arr[k];
                    if(tmp>K) break;
                    k = (k+1)%N;
                }
                line[j].v = pre;
                line[j].next = k;
            }
            k = 0;
            while(R--)
            {
                res += line[k].v;
                k = line[k].next;

            }
            printf("%lld\n",res);
        }
    }
    return 0;
}
