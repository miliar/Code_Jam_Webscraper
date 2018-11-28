#include <stdio.h>
int main()
{
    long long i,j,k,l,n,t=1,test;
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);

    scanf("%lld",&test);
    while(test--)
    {
        scanf("%lld %lld",&n,&k);
        j=(1<<n)-1;
        l=k%(1<<n);
        if(j==l)
           printf("Case #%lld: ON\n",t++);
        else
           printf("Case #%lld: OFF\n",t++);
    }
return 0;
}
