#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
const int Maxn=10010;
struct P
{
    int d,l,b;
}p[Maxn];
int n,d;
long long a[24]={0,3 ,6 ,10 ,21 ,39 ,92 ,198 ,498 ,1219 ,
3210 ,8418 ,22913 ,62415 ,173088 ,481598 ,
1351983 ,3808083 ,10781954 ,30615354 ,87230157 ,
249144711 ,713387076 ,2046856566 };
int main()
{
   // freopen("A-large.in","r",stdin);
   // freopen("out.txt","w",stdout);

    int cas;
    scanf("%d",&cas);
    for(int tcas=1;tcas<=cas;++tcas)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
        {
            scanf("%d%d",&p[i].d,&p[i].l);
            p[i].b=0;
        }
        scanf("%d",&d);
        p[1].b=p[1].d;
        bool ok=0;
        for(int i=1;i<=n;++i)
        {
            if(p[i].d+p[i].b>=d){ok=1;break;}
            for(int j=i+1;j<=n&&(p[j].d-p[i].d)<=p[i].b;++j)
            {
                p[j].b=max(p[j].b,min(p[j].d-p[i].d,p[j].l));
            }
        }
        printf("Case #%d: ",tcas);
        if(ok)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
