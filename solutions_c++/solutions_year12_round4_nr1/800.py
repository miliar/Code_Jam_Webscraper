 #include <iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<math.h>
#define PI acos(-1)
using namespace std;
#define Maxn 10010
struct hh
{
    int d,ll,b;
}qq[Maxn];

int main()
{
    freopen("in22.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int t=1;t<=cas;++t)
    {
         printf("Case #%d: ",t);
        int n,d;
        scanf("%d",&n);
        for(int i=1;i<=n;++i)
        {
            scanf("%d%d",&qq[i].d,&qq[i].ll);
            qq[i].b=0;
        }
        scanf("%d",&d);
        qq[1].b=qq[1].d;
        int flag=0;
        for(int i=1;i<=n;++i)
        {
            if(d<=qq[i].d+qq[i].b){flag=1;break;}
            for(int j=i+1;j<=n;++j)
            {
                if((qq[j].d-qq[i].d)>qq[i].b)break;
                qq[j].b=max(qq[j].b,min(qq[j].d-qq[i].d,qq[j].ll));
            }
        }

        if(flag)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}



