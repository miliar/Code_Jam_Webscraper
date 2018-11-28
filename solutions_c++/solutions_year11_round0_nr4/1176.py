#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
#include<stack>
#include<map>
using namespace std;
int n;
struct point
{
    int v;
    int num;
}a[1009];
void init()
{
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i].v);
        a[i].num=i;
    }
}
bool cmp(point a,point b)
{
    return a.v<b.v;
}
void solve()
{
    sort(a,a+n,cmp);
    double ans=0;
    for(int i=0;i<n;i++)
    if(a[i].num!=i)
    ans=ans+1;
    printf("%.6lf\n",ans);
}

void rw()
{
	freopen("E:\\D-large.in","r",stdin);
	freopen("E:\\ans_D_small.out","w",stdout);
}

int main()
{
    int Case;
    rw();
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
        solve();
    }
return 0;
}
