#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("C:\\Users\\¼Ó·ÆÃ¨\\Downloads\\C-large.in", "r", stdin);
    freopen("D:OUTPUT.txt", "w", stdout);
    int pp,test;
    scanf("%d",&test);
    for (pp=1;pp<=test;pp++)
    {
        int n,i,ans,tot,small,temp;
        scanf("%d",&n);
        scanf("%d",&small);
        tot=small;
        ans=small;
        for (i=2;i<=n;i++)
        {
            scanf("%d",&temp);
            small=min(temp,small);
            tot+=temp;
            ans=ans xor temp;
        }
        if (ans!=0) printf("Case #%d: NO\n",pp);
        else printf("Case #%d: %d\n",pp,tot-small);
    }
}
