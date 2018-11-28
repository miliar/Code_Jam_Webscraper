#include<stdio.h>
#include<string.h>

int num = 0;

int work()
{
    int n,k,t,ans = 0,k1,k2,tmp,i;
    scanf("%d%d%d",&n,&k,&t);
    k1 = t * 3 - 2;
    k2 = t * 3 - 4;
    if (t == 0) k1 = k2 = 0;
    if (t == 1) k1 = k2 = 1;
    for(i = 1;i <= n;i++) {
        scanf("%d",&tmp);
        if (tmp >= k1) ans ++;
          else if (tmp >= k2 && k) { k--; ans++;}
        }
    printf("Case #%d: %d\n",++num,ans);
    return 0;
}

int main()
{
  freopen("GCJ.in","r",stdin);
  freopen("GCJ.out","w",stdout);
  int tt;
  scanf("%d",&tt);
  while (tt--) work();
  return 0;
}
