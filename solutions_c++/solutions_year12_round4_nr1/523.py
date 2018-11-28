#include<stdio.h>
#include<string.h>
int n,d[10002],l[10002],f[10002];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,qq;
    scanf("%d",&test);
    for(qq=1;qq<=test;qq++)
    {
                           if(qq==2)
                           printf("");
      scanf("%d",&n);
      int i,j;
      for(i=1;i<=n;i++)scanf("%d%d",&d[i],&l[i]);
      scanf("%d",&d[n+1]);
      memset(f,0,sizeof(f));
      f[1]=d[1];
      for(i=1;i<=n;i++)
      {
        if(f[i]==0)continue;
        if(f[i]>l[i])f[i]=l[i];
        for(j=i+1;j<=n+1;j++)
        {
          if(d[j]-d[i]>f[i])break;
          if(f[j]<d[j]-d[i])f[j]=d[j]-d[i];
        }
        if(j==n+2)break;
      }
      if(j==n+2)printf("Case #%d: YES\n",qq);
      else printf("Case #%d: NO\n",qq);
    }
}
