#include <cstdio>
#include <cmath>
#include <queue>
using namespace std;
int n;
int o[105],b[105];
struct T
{
    char c;
    int p;
} t[105];
int po,pb;
int co,cb;
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    for(int pp=1; pp<=ca; pp++)
    {
        scanf("%d",&n);
        po=pb=1;
        co=cb=0;
        for(int i=0; i<n; i++)
        {
            scanf(" %c %d",&t[i].c,&t[i].p);
            if(t[i].c=='O') o[co++]=t[i].p;
            else b[cb++]=t[i].p;
        }
        int j=0,k=0;
        int ans=0;
        for(int i=0; i<n; i++)
        {
            ans++;
            bool fg_o=1;
            bool fg_b=1;
            if(j<co)
            {
                if(po<o[j]) po++,fg_o=0;
                else if(po>o[j]) po--,fg_o=0;
            }
            if(k<cb)
            {
                if(pb<b[k]) pb++,fg_b=0;
                else if(pb>b[k]) pb--,fg_b=0;
            }
            if(t[i].c=='O'&&fg_o&&po==t[i].p)
            {
                j++;
            }
            else if(t[i].c=='B'&&fg_b&&pb==t[i].p)
            {
                k++;
            }
            else i--;

        }
        printf("Case #%d: %d\n",pp,ans);
    }
    return 0;
}
