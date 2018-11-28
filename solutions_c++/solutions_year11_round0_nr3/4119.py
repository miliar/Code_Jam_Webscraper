#include<stdio.h>
#include<iostream>

int main()
{
    //freopen("asd.txt","r",stdin);
    //freopen("asd2.txt","w",stdout);
    long long a, b , c,sum,min,total;
    scanf("%lld",&a);
    for(int i=0;i<a;i++)
    {
        sum=0;
        min=99999999;
        total=0;
        scanf("%lld",&b);
        for(int j=0;j<b;j++)
        {
            scanf("%lld",&c);
            if (c<min)min=c;
            total+=c;
            sum^=c;
        }
        if(sum==0)printf("Case #%d: %lld\n",i+1,total-min);
        else printf("Case #%d: NO\n",i+1);
    }
    return 0;
    }
