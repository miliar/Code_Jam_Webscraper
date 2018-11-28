#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tn;
int a,b;
int ans=0,maxn;
int hash[2000001];

int turn (int a,int b,int maxn)
{
    int tmp=a % b;
    a/=b;
    a=a+tmp*(maxn/b);
    return a;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tn);
    for (int w=1;w<=tn;w++)
    {
        memset(hash,0,sizeof(hash));
        scanf("%d%d",&a,&b);
        ans=0;
        for (int i=a;i<=b;i++)
        {
            for (maxn=10;maxn<=i;maxn*=10);
            for (int j=10;j<=i;j*=10)
            {
                int tmp=turn(i,j,maxn);
                if (tmp>i && tmp<=b && hash[tmp]!=i)
                    ans++,hash[tmp]=i;
            }
        }
        printf("Case #%d: %d\n",w,ans);
    }
    return 0;
}
