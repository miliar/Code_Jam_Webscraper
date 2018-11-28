#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

struct V
{
    int d,l,hehe;
}vine[10050];
int n,d;
void Output(bool jud)
{
    if(jud)
        printf("YES\n");
    else
        printf("NO\n");
}
void DoIt()
{
    int t;
    scanf("%d",&t);
    int i,j;
    for(int cases = 1;cases<=t;++cases)
    {
        scanf("%d",&n);
        i = 1;
        while (i<=n)
        {
            scanf("%d%d",&vine[i].d,&vine[i].l);
            vine[i].hehe=0;
            i++;
        }
        scanf("%d",&d);
        vine[1].hehe = vine[1].d;
        bool jud = 0;
        for(i=1;i<=n;++i)
        {
            if(vine[i].d+vine[i].hehe>=d)
            {
                jud=1;
                break;
            }
            for(j=i+1;j<=n && (vine[j].d-vine[i].d)<=vine[i].hehe;++j)
                if (vine[j].hehe<min(vine[j].d-vine[i].d,vine[j].l))
                    vine[j].hehe = min(vine[j].d-vine[i].d,vine[j].l);
        }
        printf("Case #%d: ",cases);
        Output(jud);
    }
}
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    DoIt();
    return 0;
}
