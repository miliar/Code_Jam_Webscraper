#include <stdio.h>
#include <stdlib.h>
#include<string>
#define maxn 101
using namespace std;
struct Cedge{
  int t;
  Cedge *next;
}edgfirst[2048],*first[maxn];
int n,m,tot,ans,b2,p;
bool v[maxn],vv[maxn];
void addedge(int s, int t)
{
  edgfirst[++tot].t=t;edgfirst[tot].next=first[s];first[s]=&edgfirst[tot];	
  edgfirst[++tot].t=s;edgfirst[tot].next=first[t];first[t]=&edgfirst[tot];
}
void init()
{
  tot=0;memset(first,0,sizeof(first));
  scanf("%d%d",&n,&m);
  int i,x,y;
  for(i=1;i<=m;i++){
    scanf("%d,%d",&x,&y);addedge(x,y);
  }
}
int calc()
{
  memset(vv,0,sizeof(vv));
  int s=0,i;
  v[1]=false;
  for(Cedge *j =first[0];j;j=j->next)
    vv[j->t]=true;
  for(i=2;i<=n;i++)
    if(v[i]){
      for(Cedge *j = first[i];j;j=j->next)
        vv[j->t]=true;
	}
  for(i=1;i<=n;i++)
	if(vv[i] && !v[i]) s++;
  return s;
}
void dfs(int i, int s)
{
  if(s>ans) return;
  if(i==1){
    if(s<ans) ans=s, b2=calc();
    else if(s==ans) b2=max(calc(),b2);
    return;
  }
  for(Cedge *j =first[i];j;j=j->next){
    int k=j->t;
    if(!v[k]){
      v[k]=true;  
      dfs(k,s+1);v[k]=false;
    }
  }
}
void work()
{
  ans=maxn;b2=0;
  dfs(0,0);
  printf("Case #%d: %d %d\n",p,ans-1,b2);
}
int main()
{
  int T;
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    init();
    work();
  }
  scanf("%d",&T);
  return 0;
}
