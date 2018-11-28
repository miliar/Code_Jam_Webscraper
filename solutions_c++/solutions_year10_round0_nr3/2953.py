#include<stdio.h>


int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.in","w",stdout);

    long r,k,n,t,sum,g[1005],i,total,now,count,cas=0;

    scanf("%ld",&t);

    while(t--)
    {
    scanf("%ld%ld%ld",&r,&k,&n);
    sum=0;
    for(i=1;i<=n;i++)
     {scanf("%ld",&g[i]);
      if(sum<=k)
       sum+=g[i];
     }
    if(sum<=k)
     {total=sum*r;
      goto out;
     }

    total=0;

    now=1;
    for(i=1;i<=r;i++)
    {
        count=0;
        while(1)
        {
        if((count+g[now])>k)
        break;

        count=count+g[now];

        now=now+1;
        if(now==(n+1))
         now=1;
        }

    total+=count;


    }

    out:

    printf("Case #%ld: %ld\n",++cas,total);
}
return 0;
}



