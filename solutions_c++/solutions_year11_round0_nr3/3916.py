#include <stdio.h>
#include <string.h>
inline int min(int &a,int &b)
{
    return (a<b)?a:b;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("c_large.out","w",stdout);
    int casee,n;
    scanf("%d",&casee);
    for(int tt=1;tt<=casee;tt++)
    {
        int small=1<<30,sum=0;
        scanf("%d",&n);
        int tmp,judge=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&tmp);
            small=min(small,tmp);
            sum+=tmp;
            judge^=tmp;
        }
        printf("Case #%d: ",tt);
        if(!judge) printf("%d\n",sum-small);
        else printf("NO\n");
    }
    return 0;
}
