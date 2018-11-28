#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int gcd(int a,int b)
{
    if (!b) return a;
    else return gcd(b,a%b);
}
int lcm(int a,int b)
{
    return a*b/gcd(a,b);
}
int a[10005];
int main()
{
    freopen("C-small.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        printf("Case #%d: ",cas);
        int n,l,h;
        scanf("%d%d%d",&n,&l,&h);
        for (int i=1;i<=n;i++)
            scanf("%d",&a[i]);
        int res=-1;
        for (int i=l;i<=h;i++)
        {
            bool flag=true;
            for (int j=1;j<=n;j++)
            {
                if (a[j]%i==0 || i%a[j]==0) continue;
                else
                {
                    flag=false;break;
                }
            }
            if (flag)
            {
                res=i;break;
            }
        }
        if (res==-1) printf("NO\n");
        else printf("%d\n",res);
    }
}
