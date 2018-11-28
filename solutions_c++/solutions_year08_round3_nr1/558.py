#include <cstdio>
#include <cstdlib>
#include <cstring>

int N,P,K,L;
int q[1010];

int cmp(const void *a,const void *b)
{
    return *((int *)b)-*((int *)a);
}

int count,m=1;
long long result;

int main()
{
    int i,j;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&N);
    while(N--)
    {
        result=0;
        memset(q,0,sizeof(q));
        scanf("%d%d%d",&P,&K,&L);
        for(i=0;i<L;i++)
        {
            scanf("%d",&q[i]);
        }
        qsort(q,L,sizeof(int),cmp);
        count=1;
        i=0;
        while(i<L)
        {
            for(j=0;j<K;j++)
            {
                result+=q[i]*count;
                i++;
                if(i>=L)
                    break;
            }
            count++;
        }
        printf("Case #%d: %I64d\n",m,result);
        m++;
    }
    return 0;
}
