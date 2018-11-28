#include <cstdio>
#include <algorithm>

using namespace std;

int a,b,que[15],len;

int solve(int key)
{
    int t,tmp,s,i;
    t=1;tmp=key;
    while (tmp>0) { tmp/=10;t*=10; }
    t/=10;
    len=0;tmp=key;
    for (i = 1;i<=10;i++)
    {
        tmp=(tmp / t)+tmp % t * 10;
        que[++len]=tmp;
    }
    sort(que+1,que+1+len);
    s=0;
    for (i = 1;i<=len;i++) if (que[i]!=que[i-1] && que[i]>key && que[i]<=b) s++;
    return s;
}

int main()
{
    //freopen("Recycled.in","r",stdin);
    //freopen("Recycled.out","w",stdout);
    int tt,t,i,ans;
    scanf("%d",&tt);
    for (t = 1;t<=tt;t++)
    {
        scanf("%d%d",&a,&b);
        ans=0;
        for (i = a;i<b;i++) ans+=solve(i);
        printf("Case #%d: %d\n",t,ans);
    }
}
