#include <stdio.h>
#include <string.h>

int a[1010];
bool flag[1010];
int p;

void pre()
{
    p=0;

    memset(flag,0,sizeof(flag));
    for(int i=2;i<=1000;i++)
    {
        if (flag[i]==0) a[p++]=i;
        for(int j=0;j<p&&i*a[j]<=1000;j++)
        {
            flag[i*a[j]]=1;
            if(i%a[j]==0) break;
        }
    }
}

int main()
{
    pre();
    int cas;
    int n;

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&cas);
    for(int ll=1;ll<=cas;ll++)
    {
        scanf("%d",&n);
        int mins=0;
        int maxs=0;
        for(int i=0;i<p;i++)
        {
            if (a[i]<=n) mins++;
            int now=a[i];
            int num=0;
            while(now<=n)
            {
                num++;
                now*=a[i];
            }
            maxs+=num;
        }
        if (n!=1) maxs++;
        printf("Case #%d: %d\n",ll,maxs-mins);
    }
    return 0;
}

