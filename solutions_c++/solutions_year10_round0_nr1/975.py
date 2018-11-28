#include<iostream>
using namespace std;
int main()
{
    freopen("1.txt","w",stdout);
    int t,cas,k,n;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d%d",&n,&k);
        int mask=(1<<n)-1;
        if((k&mask)==mask)
            printf("Case #%d: ON\n",cas);
        else
            printf("Case #%d: OFF\n",cas);
    }
}
