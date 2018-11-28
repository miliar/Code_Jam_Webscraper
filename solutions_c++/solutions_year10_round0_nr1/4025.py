#include <iostream>
#include <cstdio>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("salida2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int i=0;i<T;i++)
    {
        int N,K;
        scanf("%d%d",&N,&K);
        K%=(1<<N);
        if (K==((1<<N)-1))
            printf("Case #%d: ON\n",i+1);
        else
            printf("Case #%d: OFF\n",i+1);
    }
    return 0;
}
