#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define M 105
int ca,T,n;
int d[M];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&T);
    for (int cases=1;cases<=T;cases++)
    {
        memset(d,0,sizeof(d));
        int sum=0;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            int a;
            scanf("%d",&d[i]);
            sum+=d[i];
        }
        int tmp=0;
        for (int i=0;i<n;i++)
            tmp=tmp^d[i];
        if (tmp>0) printf("Case #%d: NO\n",cases);
        else
        {
            sort(d,d+n);
            printf("Case #%d: %d\n",cases,sum-d[0]);
        }
    }
    return 0;
}
