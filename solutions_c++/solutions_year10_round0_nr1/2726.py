#include <cstdio>

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int n,a,b;
    scanf("%d",&n);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d %d",&a,&b);
        if ((b % (1 << a)) == ((1 << a)-1))
           printf("Case #%d: ON\n",i);
        else printf("Case #%d: OFF\n",i);
    }
    return 0;
}
