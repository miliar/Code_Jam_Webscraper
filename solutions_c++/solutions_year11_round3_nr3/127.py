#include<iostream>
using namespace std;

const int maxn=10010;
int a[maxn],l,h,n,ans;
bool cc;

void solve()
{
  scanf("%d%d%d",&n,&l,&h);
  for (int i=1;i<=n;i++) scanf("%d",&a[i]);
  ans=-1;
  for (int i=l;i<=h;i++)
    {
      cc=true;
      for (int j=1;j<=n;j++)
        if ((i%a[j]) && (a[j]%i)) { cc=false; break; }
      if (cc) { ans=i; break; }
    }
  if (ans==-1) printf("NO\n");
  else printf("%d\n",ans);
}

int main()
{
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
  int t; scanf("%d",&t);
  for (int tt=1;tt<=t;tt++)
    {
      printf("Case #%d: ",tt);
      solve();
    }
  return 0;
}
