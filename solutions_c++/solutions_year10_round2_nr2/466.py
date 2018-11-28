#include<iostream>
using namespace std;
__int64 x[100];
__int64 v[100];
int main()
{
    __int64 n,k,b,t,cases;
    scanf("%I64d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        scanf("%I64d%I64d%I64d%I64d",&n,&k,&b,&t);
        for(int i=1;i<=n;i++)
        scanf("%I64d",&x[i]);
        for(int i=1;i<=n;i++)
        scanf("%I64d",&v[i]);
        int res=0;
        int ok=0;
        for(int i=n;i>=1;i--)
        {
             if(x[i]+t*v[i]>=b)
                 ok++;
             else
             {
                 res+=k-ok;
             }
             if(ok==k)
             break;
        }
        printf("Case #%d: ",ca);
        if(ok!=k)
        printf("IMPOSSIBLE\n");
        else
        printf("%d\n",res);
    }
}
