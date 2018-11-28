#include<stdio.h>
#include<algorithm>
#define inf 1e-7
using namespace std;
int T,p,n,d;
int per[1000001],tot;
double left,right,mid;
inline bool check(double x)
{
  int i,j,k;
  double c=per[0]-x,c2;
  for(i=1;i<tot;i++){
    c2=c+d;
    if(per[i]==c2) continue;
    if(per[i]>c2){
      if(per[i]-x>c2){
        c=per[i]-x;continue;}
      else {c=c2;continue;}
    }
    else{
      if(per[i]+x<c2) return false;
      else c=c2;
    }
  }
  return true;
}        
int main()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  int i,j,k,v;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%d",&n,&d);
    tot=0;
    for(i=1;i<=n;i++){
      scanf("%d%d",&k,&v);
      for(j=tot;j<=tot+v;j++)
        per[j]=k;
      tot+=v;
    }
    sort(per,per+tot);
    left=0,right=tot*d*2+10000;
    while(left+inf<right){
      mid=(left+right)/2;
      if(check(mid))  right=mid;
      else  left=mid+inf;}
    printf("Case #%d: %.6lf\n",p,left);
  }
  scanf("%d",&n);
  return 0;
}
        
    
