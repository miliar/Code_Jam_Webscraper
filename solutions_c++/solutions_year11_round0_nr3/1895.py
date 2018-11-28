#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MAXN=1005;
int value[MAXN];
int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int cas,cnt,n,i,sum,t;
    scanf("%d",&cas);
    for(cnt=1;cnt<=cas;cnt++)
    {
        scanf("%d",&n);
        sum=t=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&value[i]);
            sum+=value[i];
            t^=value[i];
        }
        if(t!=0) printf("Case #%d: NO\n",cnt);
        else
        {
            sort(value,value+n);
            printf("Case #%d: %d\n",cnt,sum-value[0]);
        }
     }
}
