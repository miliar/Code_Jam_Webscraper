#include<stdio.h>
#include<cstring>
#include<iostream.h>

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cases,ii,r,k,n,re,g[1002],i,res,t,ud[1002],uds,tt[1002];
    long long int an[1002],all,sum;
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d%d",&r,&k,&n);
        for(i=1;i<=n;i++)scanf("%d",&g[i]);
        memset(ud,0,sizeof(ud));
        uds=0;
        t=1;
        while(!ud[t])
        {
            //fprintf(stderr,"t=%d\n",t);
            ud[t]=++uds;
            //tt[t]=uds;
            sum=g[t];
            for(i=t%n+1;i!=t;i=i%n+1)
            {
                //fprintf(stderr,"g[%d]=%d\n",i,g[i]);
                if(sum+g[i]>k)break;
                sum+=g[i];
            }
            i=(i+n-1)%n;
            //fprintf(stderr,"sss i=%d t=%d sum=%I64d\n",i,t,sum);
            an[uds]=sum;
            t=i%n+1;
            //fprintf(stderr,"et=%d\n",t);
            //system("PAUSE");
        }
        re=ud[t]-1;
        res=uds-re;
        sum=0;
        //fprintf(stderr,"re=%d res=%d\n",re,res);
        //for(i=1;i<=uds;i++)fprintf(stderr,"an[%d]=%I64d  ud\n",i,an[i]);
        for(i=re+1;i<=uds;i++)sum+=an[i];
        all=0;
        for(i=1;i<=r && i<=re;i++)all+=an[i];
        if(r>re)
        {
            all+=((r-re)/res)*sum;
            for(i=1;i<=(r-re)%res;i++)all+=an[re+i];
        }
        fprintf(stderr,"Case #%d: %I64d\n",ii,all);
        printf("Case #%d: %I64d\n",ii,all);
    }
    fprintf(stderr,"END\n");
    while(1);
        
    return 0;
}
