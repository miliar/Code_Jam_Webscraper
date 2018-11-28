#include<stdio.h>

inline int aabs(int n)
{
    return n<0?-1:n;
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int cases,ii,n,m,i,a,j,iii,jjj;//,aa,bb;
    bool yes;
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d%d",&n,&m,&a);
        if(a<=0)
        {
            printf("Case #%d: IMPOSSIBLE\n",ii);
            continue;
        }
        yes=0;
        
        for(i=0;i<=n;i++)for(j=0;j<=m;j++)
        for(iii=0;iii<=n;iii++)for(jjj=0;jjj<=m;jjj++)
        {
            //fprintf(stderr,"i=%d %d %d %d\n",i,j,iii,jjj);
            if(aabs(i*jjj-iii*j)==a)
            {
                printf("Case #%d: 0 0 %d %d %d %d\n",ii,i,j,iii,jjj);
                yes=1;
                iii=j=i=2222222;
                break;
            }
        }
        if(!yes)printf("Case #%d: IMPOSSIBLE\n",ii);
        fprintf(stderr,"ii=%d\n",ii);
    }


    return 0;
}
