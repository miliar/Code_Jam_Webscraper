#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t-- > 0)
    {
        int n,i;
        long long int k=0ll,temp=1ll;
        scanf("%d%lld",&n,&k);
        
        for(i=1;i<=n;i++)
        {
            temp*=2;
        }
              
        if(k%temp==temp-1)
        printf("Case #%d: ON\n",cases++);
        else
        printf("Case #%d: OFF\n",cases++);
    }
    return 0;
}
