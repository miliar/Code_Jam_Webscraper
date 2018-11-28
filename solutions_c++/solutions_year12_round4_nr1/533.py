#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct node{
    int pos,maxs;
} qu[20000];

int len[20000],d[20000];

int main()
{
    int cas;
    int n;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ii=1;ii<=cas;ii++)
    {
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d %d",&d[i],&len[i]);
        int s=0,t=0;
        qu[s].maxs=2*d[0];
        qu[s].pos=d[0];
        for(int i=1;i<n;i++)
        {
            while(s<=t&&qu[s].maxs<d[i]) s++;
            if (s<=t)
            {
                t++;
                qu[t].pos=d[i];
                qu[t].maxs=min(len[i],d[i]-qu[s].pos)+d[i];
            }
        }
        int need;
        scanf("%d",&need);
        bool ansflag=0;
        for(int i=0;i<=t;i++)
         if (qu[i].maxs>=need) ansflag=1;
         printf("Case #%d: ",ii);
        if (ansflag) puts("YES");
        else puts("NO");
    }
    return 0;
}




