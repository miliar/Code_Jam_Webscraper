#include<stdio.h>
#include<math.h>


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    long   t,n,k,m,ans,count;
    scanf("%ld",&t);

    count=0;

    while(t--)
    {
        scanf("%ld%ld",&n,&k);
        m=pow(2,n);

        k=k+1;

        if(k<m)
         {ans=0;
          goto last;
         }

        if((k%m)==0)
         ans=1;
        else
         ans=0;

    last:



    if(ans==1)
     printf("Case #%ld: ON\n",++count);
    else
     printf("Case #%ld: OFF\n",++count);

    }

    return 0;

     }

