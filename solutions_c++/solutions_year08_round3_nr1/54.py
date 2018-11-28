#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int cases,ii,p,k,l,y,n[1002],i,yy;
    long long int an;
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d%d",&p,&k,&l);
        if(p*k<l)
        {
            printf("Case #%d: Impossible\n",ii);
            continue;
        }
        for(i=1;i<=l;i++)scanf("%d",&n[i]);
        sort(n+1,n+1+l);
        an=yy=0;
        y=1;
        for(i=l;i>=1;i--)
        {
            an+=n[i]*y;
            //fprintf(stderr,"n[%d]=%d y=%d yy=%d  p=%d k=%d l=%d\nan=%d\n",i,n[i],y,yy,p,k,l,an);
            yy++;
            if(yy==k)yy=0,y++;
            //if(an<0){fprintf(stderr,"cc %d\n",ii);while(1);}
        }
        printf("Case #%d: %I64d\n",ii,an);
    }
    //while(1);
    return 0;
}
