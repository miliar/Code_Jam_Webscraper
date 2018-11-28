#include<stdio.h>
using namespace std;
int T,p,r,c,d,ans;
int g[501][501];
char re;
bool flag;
bool cal(double cx,double cy,int x,int y)
{
  int i,j,k,l;
  double tx=0.0,ty=0.0;
  for(i=x;i<x+ans;i++)
    for(j=y;j<y+ans;j++){
      if( (i==x&&j==y) || (i==x&&(j==y+ans-1)) || ((i==x+ans-1)&&j==y) || ((i==x+ans-1)&&(j==y+ans-1)) )
        continue;
      tx+=(cx-i*1.0)*(g[i][j]+d)*1.0;
      ty+=(cy-j*1.0)*(g[i][j]+d)*1.0;
    }
  if(tx==0.0 && ty==0.0) return true;
  return false;
}
bool check(int x,int y)
{
  if( cal((x+(ans-1)*1.0/2.0),(y+(ans-1)*1.0/2.0),x,y) )
    return true;
  return false;
}
int main()
{
  freopen("B.IN","r",stdin);
  freopen("B.out","w",stdout);
  int i,j,k,l;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%d%d",&r,&c,&d);
    for(i=1;i<=r;i++){
      scanf("\n");
      for(j=1;j<=c;j++){
        scanf("%c",&re);
        g[i][j]=re-'0';}
    }
    ans=r<c?r:c;flag=false;
    while(ans>=3){
      for(i=1;i+ans-1<=r;i++)
        for(j=1;j+ans-1<=c;j++)
          if(check(i,j)){
            flag=true;break;}
      if(flag) break;
      ans--;} 
    if(ans>=3) printf("Case #%d: %d\n",p,ans);
    else printf("Case #%d: IMPOSSIBLE\n",p);
  }
  scanf("%d",&T);
  return 0;
}
