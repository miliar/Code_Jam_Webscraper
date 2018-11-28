#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
int xx,yy;
struct PO
{
    int r,id;
    int x, y;
}po[100];
int cmp(PO a,PO b)
{
    if(a.r>b.r)
      return 1;
    return 0;
}
int cmp2(PO a,PO b)
{
    if(a.id<b.id)
      return 1;
    return 0;
}
int dir[4][2]={1,0,0,1,-1,0,0,-1};
int dis(int x1,int y1,int x2,int y2)
{
    return (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
}
int ok(int th,int x,int y)
{
    for(int i=0;i<th;++i)
    {
        if(dis(po[i].x,po[i].y,x,y)<(po[i].r+po[th].r)*(po[i].r+po[i].r))
          return false;
    }
    return true;
}
void bfs(int bf,int th,int &d)
{

    for(int i=0;i<4;++i)
    {
        int x=dir[d][0],y=dir[d][1];
        int stax=x+po[bf].x+(po[bf].r+po[th].r)*x;
        int stay=y+po[bf].y+(po[bf].r+po[th].r)*y;
        for(int j=0;;j++){
            if(stax+j*x>=0 && stax+j*x<=xx  && stay+j*y>=0&& stay+j*y<=yy){

              if(ok(th,stax+j*x,stay+j*y)){
                po[th].x=stax+j*x;
                po[th].y=stay+j*y;
                return ;
              }
            }
            else
               break;
        }
        d=(d+1)%4;
    }
}
int main()
{
   int cn,n;
   int cc=0;
   scanf("%d",&cn);
   while(cn--)
   {
       scanf("%d%d%d",&n,&xx,&yy);
       for(int i=0;i<n;++i){
         scanf("%d",&po[i].r);
         po[i].id=i;
       }
     //  scanf("",);
       sort(po,po+n,cmp);
       po[0].x=0;
       po[0].y=0;
       int dir=0;
       for(int i=1;i<n;++i)
       {
           bfs(i-1,i,dir);
       }
       sort(po,po+n,cmp2);
       printf("Case #1:");
       for(int i=0;i<n;++i)
         printf(" %d %d",po[i].x,po[i].y);
        printf("\n");

   }
   return 0;
}
