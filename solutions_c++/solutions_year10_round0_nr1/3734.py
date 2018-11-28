#include <cstdio>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int Test;
    scanf("%d",&Test);
    for (int T = 1; T <= Test; ++T)
    {
        int n,k;
        scanf("%d%d",&n,&k);
        int t = (1<<n);
        k ++;
        if (k % t == 0)
            printf("Case #%d: ON\n",T);
        else printf("Case #%d: OFF\n",T);
    }
}
