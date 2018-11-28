#include<cstdio>

using namespace std;
typedef long long ll;
int pd,pg;
ll n;
int main()
{
    freopen("A.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        scanf("%lld%d%d",&n,&pd,&pg);
        printf("Case #%d: ",t);
        if(pg==100 && pd<100) printf("Broken\n");
        else if(pg==0 && pd>0) printf("Broken\n");
        else{
            bool flag=false;
            if(n<100)     {
                for(int i=1;i<=n;i++)
                    if(i*pd%100==0) {
                        flag=true;
                    }
            }else flag=true;
            if(flag) printf("Possible\n");
            else printf("Broken\n");
        }
    }
    return 0;
}
