#include <stdio.h>

int main()
{
    int _kase,kase=0,n,k;
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    scanf("%d",&_kase);
    while(_kase--)
    {
        scanf(" %d %d",&n,&k);
        n = 1<<n;
        printf("Case #%d: ",++kase);
        if( (k+1)%n==0 ) printf("ON");
        else printf("OFF");
        printf("\n");
    }
    return 0;
}
