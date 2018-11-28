#include<stdio.h>
#include<algorithm>
using namespace std;
struct node{
  int be,ee,w,l;
};
node edge[1101];
int T,x,s,r,n,p;
double t,ans,cal,opt;
inline bool cmp(node a,node b)
{
  return a.w<b.w;
}
int main()
{
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);
  int i,j,k,l,all;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%d%d%lf%d",&x,&s,&r,&t,&n);
    for(i=1;i<=n;i++)
      scanf("%d%d%d",&edge[i].be,&edge[i].ee,&edge[i].w),edge[i].l=edge[i].ee-edge[i].be;
    ans=x*1.0/(s*1.0),all=x;
    for(i=1;i<=n;i++){
      ans+=edge[i].l*1.0/( (s+edge[i].w)*1.0 )-edge[i].l*1.0/(s*1.0);
      all-=edge[i].l;}
    edge[++n].l=all,edge[n].w=0;
    sort(edge+1,edge+n+1,cmp);
    for(k=1;k<=n;k++){
      cal=edge[k].l*1.0/( (r+edge[k].w)*1.0);
      if(t>=cal){
        t-=cal;
        ans=ans+cal-edge[k].l*1.0/( (s+edge[k].w)*1.0);
        continue;}
      else{
        opt=edge[k].l*1.0-(r+edge[k].w)*1.0*t;
        cal=t+opt/( (s+edge[k].w)*1.0);
        ans=ans+cal-edge[k].l*1.0/( (s+edge[k].w)*1.0);
        t=0;
      }
      if(t==0) break;
    }
    printf("Case #%d: %.10lf\n",p,ans);
  }
  scanf("%d",&n);
  return 0;
}
