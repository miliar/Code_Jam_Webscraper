#include <cstdio>
#include <cstring>

typedef long long LL;
int a[1001],g[1001];
LL f[1001];
int r,lim,n;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int Cas;
    scanf("%d",&Cas);
    for (int run=1;run<=Cas;run++)
    {
        scanf("%d%d%d",&r,&lim,&n);
        int tot=0;
        for (int i=1;i<=n;i++)
        {
            scanf("%d",a+i);
            tot+=a[i];
        }
        printf("Case #%d: ",run);
        if (tot<=lim) printf("%I64d\n",(LL)tot*r);
        else
        {
            memset(g,0,sizeof(g));
            int t=1;
            LL s=0;
            bool ok=0;
            for (int i=1;i<=r;i++)
            {
                  if (g[t])
                  {
                      ok=1;
                      int p=i-g[t];
                      r-=g[t]-1;
                      printf("%I64d\n",f[g[t]-1]+(LL)(s-f[g[t]-1])*(r/p)+f[g[t]+r%p-1]-f[g[t]-1]);
                      break;
                  }
                  g[t]=i;
                  int j=t,now=0;
                  while (1)
                  {
                      if (now+a[j]>lim) break;
                      now+=a[j];
                      j++;
                      if (j>n) j=1;
                  }
                  s+=now;
                  f[i]=s;
                  t=j;
            }
            if (!ok) printf("%I64d\n",s);
        }
    }
    return 0;
}
