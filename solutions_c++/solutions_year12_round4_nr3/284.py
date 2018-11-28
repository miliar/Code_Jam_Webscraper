#include <iostream>
#include <stdio.h>
using namespace std;

int t, n, a[2100], l[2100];
bool fl[2100];
const int st = 1000000, c = 100000;

bool check()
{
    for (int i = 1;i < n;++i)
        for (int j = i+1;j < a[i];++j)
            if (a[j] > a[i]) return false;
    return true;
}

int cal(int x, int y, int z)
{
    double k = 1.0*(l[z]-l[y])*(y-x)/(z-y);
    return l[y]-k-10;
}

void chuli(int x, int y)
{
    for (int j = y;j >= x;--j)
        if (a[j] == y+1) l[j] = l[x-1]-c/10;
        else l[j] = cal(j,a[j],a[a[j]]);
}

void doit()
{
    int k  = 0, now, p;

    for (int i = 1;i <= n;++i) fl[i]= false;
    now = 1; l[1] = st; fl[1] = true;
    now = a[1]; l[now] = st+c; fl[now]; p = 1;
    chuli(2,a[1]-1);
    while (now < n)
    {
        ++k;
       l[a[now]] = (2*l[now]+1.0*(l[now]-l[p])/(now-p)*(a[now]-now))/2;
       fl[a[now]] = true;
       chuli(now+1,a[now]-1);
       p = now; now = a[now];
    }
    for (int i = 1;i < n;++i) printf("%d ",l[i]);
    printf("%d\n",l[n]);
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    cin >> t;
    for (int w = 1;w <= t;++w)
    {
        scanf("%d",&n);
        for (int i = 1;i < n;++i)
            scanf("%d",&a[i]);
        printf("Case #%d: ",w);
        if (check()) doit();
        else printf("Impossible\n");
    }
    return 0;
}
