#include <cstdio>

int a[40];

int main()
{
    freopen("a1.in","r",stdin);
    freopen("a1.out","w",stdout);
    for (int i=1;i<=30;i++)
        a[i]=1<<i;
    int Cas;
    scanf("%d",&Cas);
    for (int r=1;r<=Cas;r++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        printf("Case #%d: ",r);
        if (m%a[n]==a[n]-1) printf("ON\n");
        else printf("OFF\n");
    }
    fclose(stdout);
    return 0;
}
        
