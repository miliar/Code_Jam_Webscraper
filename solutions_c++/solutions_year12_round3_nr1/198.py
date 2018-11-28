#include<stdio.h>
#include<string.h>

#define clear(a,b) memset(a,b,sizeof(a))

int vis[1100],st[1100],edge[100000],ans,num = 1;

void dfs(int k,int p)
{
  int i;
  if (ans) return ;
  vis[k] = p;
  for(i = st[k];i < st[k+1];i++)
     if (vis[edge[i]] == p) {ans = 1;return;}
       else dfs(edge[i],p);
  return ;
}

void work()
{
  int i,n,l = 0,t,j;

  ans = 0;
  clear(st,0);
  clear(edge,0);
  clear(vis,0);

  scanf("%d",&n);
  for(i = 1;i <= n;i++) {
     scanf("%d",&t);
     st[i] = l;
     for(j = 1;j <= t;j++) scanf("%d",&edge[l++]);
      }
   st[n+1] = l;
   for (i = 1;i <= n;i++) dfs(i,i);

   printf("Case #%d: ",num++);
   if (ans) printf("Yes\n");
     else printf("No\n");
    return ;
}

int main()
{
  int t;
  freopen("xx.in","r",stdin);
  freopen("GCJ_OUT.txt","w",stdout);
  scanf("%d",&t);
  while (t--) work();
  return 0;
}
