#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAX 17
int t,vec[MAX],total,n,pat,sean,xorp,xors,mejor;
void busca(int pos)
{
    if (pos>=1)
    {
        int xp,xs;
        xp=xorp;
        xs=xors;
        pat+=vec[pos];
        xorp^=vec[pos];
        busca(pos-1);
        pat-=vec[pos];
        xorp=xp;
        sean+=vec[pos];
        xors^=vec[pos];
        busca(pos-1);
    }
    else
    {
        if (xors==xorp && pat>mejor && sean!=0 && pat!=0)
            mejor=pat;
    }
}
int main()
{
    scanf("%d",&t);
    for (int g=1; g<=t; g++)
    {
        scanf("%d",&n);
        total=0;
        mejor=0;
        memset(vec,0,sizeof(vec));
        for (int i=1; i<=n; i++)
        {
            scanf("%d",&vec[i]);
            total^=vec[i];
        }
        if (total==0)
        {
            pat=0,sean=0,xorp=0,xors=0;
            //primero ordenar el vector
            sort(vec,vec+n+1);
            busca(n);
            printf("Case #%d: %d\n",g,mejor);
        }
        else
            printf("Case #%d: NO\n",g);
    }
}
