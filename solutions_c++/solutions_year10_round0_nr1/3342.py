#include <cstdio>

int main()
{
    int t;
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	scanf("%d",&t);
	for (int i=1; i<=t; i++)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        int nr=1<<n;
        printf("Case #%d: ",i);
        if ((k+1)%nr) printf("OFF\n");
        else printf("ON\n");
    }

    return 0;
}
