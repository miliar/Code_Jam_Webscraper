#include<iostream>
#include<vector>
using namespace std;
int g[20][20],a[20],b[20],n,m,ans,p,ck;
vector<int> c[20],d;
int check()
{
    int i,j,x;
    for (i=0;i<p;i++)
    {
        x=0;
        for (j=0;j<c[i].size();j++)
        x|=(1<<a[c[i][j]]);
        if (x+1!=(1<<ans)) return 0;
    }
    return 1;
}
void dfs(int x)
{
     if (x==n)
     {
        if (check()) ck=1;
        return;
     }
     int i;
     for (i=0;i<ans;i++)
     {
         a[x]=i;
         dfs(x+1);
         if (ck) return;
     }
}

void print()
{
     int i,j;
        for (i=0;i<p;i++)
        {
            for (j=0;j<c[i].size();j++) printf("%d ",c[i][j]);
            puts("");
        }
        puts("");
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,j,cases,tt,k,l,o;
    for (scanf("%d",&cases),tt=0;tt<cases;tt++)
    {
        scanf("%d%d",&n,&m);
        for (i=0;i<m;i++) scanf("%d",&a[i]);
        for (i=0;i<m;i++) scanf("%d",&b[i]);
        p=1;
        c[0].clear();
        for (i=0;i<n;i++) c[0].push_back(i); 
        for (i=0;i<m;i++)
        {
            a[i]--;
            b[i]--;
            for (j=0;j<p;j++)
                for (k=0;k<c[j].size();k++)
                if (c[j][k]==a[i])
                   for (l=k+1;l<c[j].size();l++)
                   if (c[j][l]==b[i])
                   {
                      d.clear();
                      for (o=k;o<=l;o++) d.push_back(c[j][o]);
                      c[p]=d;
                      p++;
                      d.clear();
                      for (o=0;o<=k;o++) d.push_back(c[j][o]);
                      for (o=l;o<c[j].size();o++) d.push_back(c[j][o]);
                      c[j]=d;
                      goto  aaa;
                   }
            aaa:;//print();
        }
        for (ans=n/2+1;;ans--)
        {
            ck=0;
            dfs(0);
            if (!ck) continue;
           printf("Case #%d: %d\n",tt+1,ans);
           for (i=0;i<n;i++)
           {
               printf("%d",a[i]+1);
               putchar(i==n-1?'\n':' ');
           }
           break;
        }
    }
    return 0;
}
