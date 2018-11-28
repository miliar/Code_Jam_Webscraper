#include <iostream>
using namespace std;
int maxn = 1005;

int n,m;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int k,t,T;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        scanf("%d%d",&n,&k);
        k%=(1<<n);
        if(k+1==(1<<n)) printf("Case #%d: ON\n",t);
        else printf("Case #%d: OFF\n",t);
    }
    return 0;
}
