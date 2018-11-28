#include<cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,N,K;
    scanf("%d",&T);
    for(int i=0; i<T; ++i)
    {
        scanf("%d%d",&N,&K);
        K %= (1<<N);
        if(K!=(1<<N)-1)
        printf("Case #%d: OFF\n",i+1);
        else
        printf("Case #%d: ON\n",i+1);
    }
    return 0;
}
