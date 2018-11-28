#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstring>
using namespace std;
#define N 2222
int n,m,a,b,ans,t,cas;
int main()
{
    freopen("cycle.in","r",stdin);
    freopen("cycle.out","w",stdout);
    cin>>cas;
    while(cas--)
    {
    int ans=0;
    cin>>a>>b;
    for(m=1;m<=b;m*=10);
    for(int i=a;i<=b;i++)
        for(int j=i+1;j<=b;j++)
        {
            int t=0;
            for(int k=1;k<=b;k*=10)
                if(((i/k)+(i%k)*(m/k))==j){t=1;break;}
            ans+=t;
        }
    printf("Case #%d: %d\n",++t,ans);
    }
}
