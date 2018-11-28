
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,k,v,len,N,ncase;scanf("%d",&ncase);
    for(int cas=1;cas<=ncase;++cas)
    {
        int Min = 1000000 + 10 , Total = 0 , can = 0;

        scanf("%d",&N);
        while(N--)
        {
            scanf("%d",&v);
            can ^= v;
            Total += v;
            Min = min(Min , v);
        }
        printf("Case #%d: ",cas);
        if(can != 0)puts("NO");
        else
        {
            printf("%d\n",Total-Min);
        }
    }
    return 0;
}
