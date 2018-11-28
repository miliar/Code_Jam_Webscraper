#include<stdio.h>
int n,a[1020];
int b[1020];
int ans;
int cnt;
void print()
{
    cnt++;
    printf("Case #%d: ",cnt);
    if (ans==-1)printf("NO\n");
    else printf("%d\n",ans);
}
void solve()
{
    int i;
    int sum=0,xorsum=0;
    int min=1e8;
    for (i=1;i<=n;i++)
    {
	sum+=a[i];
	xorsum^=a[i];
    	if (a[i]<min)min=a[i];
    }
    if (xorsum!=0)ans=-1;
    else ans=sum-min;
}
void init()
{
    int i;
    scanf("%d",&n);
    for (i=1;i<=n;i++)scanf("%d",&a[i]);
}
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t;
    scanf("%d",&t);
    while (t--)
    {
    	init();
    	solve();
    	print();
    }
    return 0;
}
