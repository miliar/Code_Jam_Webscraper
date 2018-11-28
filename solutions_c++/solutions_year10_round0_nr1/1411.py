#include<stdio.h>
#include<stdlib.h>

long long power(long p)
{
    long long ans=1,i;

    for(i=0;i<p;i++)
        ans*=2;

    return ans;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);

    long long test,_case=1,n,k,val,i,on;

    scanf("%lld",&test);

    while(test--)
    {
        scanf("%lld %lld",&n,&k);

        for(i=0;i<n;i++)
        {
            val=k/power(i);
            val%=2;
            if(val) continue;
            break;
        }
        if(i==n) on=1;
        else on=0;
        printf("Case #%lld: ",_case++);
        if(on) printf("ON\n");
        else printf("OFF\n");
    }

    return 0;
}
