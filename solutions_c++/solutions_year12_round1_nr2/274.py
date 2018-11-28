#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tn;
int n,nh;
int a[1024];
int b[1024];
int st[1024];

int calc(int k)
{
    if (k==0) return 0;
    if (nh>=b[k])
    {
        if (st[k]==0) return 2;
        if (st[k]==1) return 1;
    }
    else if (nh>=a[k])
        if (st[k]==0) return 1;
    return 0;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&tn);
    for (int w=1;w<=tn;w++)
    {
        int ans=0;
        bool flag=false;
        nh=0;
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
            scanf("%d%d",a+i,b+i);
        memset(st,0,sizeof(st));
        int exp=0;
        do
        {
            for (int i=1;i<=n;i++)
            {
                int t=calc(i);
                if (t>calc(exp)) exp=i;
                else if (t==calc(exp) && (st[i]==1 || (b[i]>b[exp] && st[i]>=st[exp]))) exp=i;
            }
            if (calc(exp)>0)
            {
                if (nh>=b[exp])
                {
                    if (st[exp]==1) nh++;
                    else nh+=2;
                    st[exp]=2;
                }
                else
                {
                    nh++;
                    st[exp]=1;
                }
                ans++;
            }
            else break;
        }while(1);
        for (int i=1;i<=n;i++)
        {
            if (st[i]!=2)
            {
                printf("Case #%d: Too Bad\n",w);
                flag=true;
                break;
            }
        }
        if (!flag) printf("Case #%d: %d\n",w,ans);
    }
    return 0;
}
