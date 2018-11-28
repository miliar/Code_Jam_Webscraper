#include<iostream>
using namespace std;

int i,j,k,l,m,n,t,r;
int ans[1100];
int g[1100];
int f[1100];
long long answ;


int main()
{
    freopen("tmp.in","r",stdin);
    freopen("tmp.out","w",stdout);
    scanf("%d",&t);
    for (int jj=1;jj<=t;++jj)
    {
        memset(g,0,sizeof(g));
        memset(f,0,sizeof(f));
        memset(ans,0,sizeof(ans));
        answ=0;
        scanf("%d%d%d",&r,&k,&n);
        for (i=1;i<=n;i++)
          scanf("%d",&g[i]);
        j=1;l=0;
        while (!f[j])
        {
          f[j]=++l;
          g[0]=0;
          f[0]= j>1 ? 1 : 0;
          while (g[0]+g[j]<=k && j<=n)
          {
             g[0]+=g[j];
             j++;
             if (f[0] && j>n) j=1;
          }
          ans[0]++;
          ans[ans[0]]=g[0];
		  if (j>n) j=1;
        }

        r=r-f[j]+1;
//        ans[0]=ans[0]-f[j]+1;
        k=r%(ans[0]-f[j]+1);
        l=r/(ans[0]-f[j]+1);
        for (i=f[j];i<=ans[0];++i)
        {
            answ+=ans[i];
        }
        answ*=l;
		for (i=1;i<f[j];++i)
          answ+=ans[i];
        for (i=f[j];i<f[j]+k;++i)
          answ+=ans[i];
        printf("Case #%d: ",jj);
        cout<<answ<<endl;
    }
}
