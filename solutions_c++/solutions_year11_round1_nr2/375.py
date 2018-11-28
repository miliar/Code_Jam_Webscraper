#include<cstdio>
#include<cstring>
const int MAXN=100;
char d[MAXN][11],s[27];
int l[MAXN],cur[MAXN+1];
int main()
{
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;++i)
  {
    int n,m;
    scanf("%d%d ",&n,&m);
    for(int j=0;j<n;++j)
    {
      gets(d[j]);
      l[j]=strlen(d[j]);
    }
    printf("Case #%d:",i);
    while(m--)
    {
      gets(s);
      int maxlose=-1,ans;
      for(int j=0;j<n;++j)
      {
        cur[0]=0;
        for(int k=0;k<n;++k)
          if(l[k]==l[j])
            cur[++cur[0]]=k;
        int lose=0;
        for(int p=0;p<26;++p)
        {
          bool g=1;
          for(int k=1;g&&k<=cur[0];++k)
            for(int q=0;g&&q<l[j];++q)
              if(d[cur[k]][q]==s[p])
                g=0;
          putchar(s[p]);
          putchar('\n');
          if(!g)
          {
            for(int q=0;q<l[j];++q)
              if(d[j][q]==s[p])
                g=1;
            if(!g)
            {
              putchar(s[p]);
              ++lose;}
            else
            {
              int tot=cur[0];
              cur[0]=0;
              for(int k=1;k<=tot;++k)
              {
                g=1;
                for(int q=0;g&&q<l[j];++q)
                  if(d[j][q]==s[p]&&d[cur[k]][q]!=s[p])
                    g=0;
                if(g)
                  cur[++cur[0]]=cur[k];
              }
            }
          }
        }
        printf("lose %s=%d\n",d[j],lose);
        if(lose>maxlose)
        {
          maxlose=lose;
          ans=j;
        }
      }
      printf(" %s",d[ans]);
    }
    putchar('\n');
  }
  while(1);
  return 0;
}
