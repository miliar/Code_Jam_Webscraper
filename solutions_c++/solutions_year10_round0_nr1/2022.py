#include <cstdio>

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int N,I,x,y,k,n,i;
    scanf("%d",&N);
    for(I=1;I<=N;++I)
    {
        scanf("%d%d",&k,&n); x=1;
        for(i=1;i<k;++i)
            x=x*2+1;
        y=x;
        while (x<n)
            x+=y+1;
        if (x==n) printf("Case #%d: ON\n",I);
        else printf("Case #%d: OFF\n",I);
    }
    return 0;
}
