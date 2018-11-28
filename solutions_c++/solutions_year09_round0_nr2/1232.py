#include <stdio.h>
#include <iostream>
#define u 200
#define maxlong 2000000000
using namespace std;


char ans[u][u],ch;
long dx[4],dy[4],i,t,x,y,l,k,j,nx,ny,cx,cy,bx,by,m[u][u],mini;
bool boo;

main()
{
 dx[0]=-1; dx[3]=1; dy[1]=-1; dy[2]=1;
 freopen("B.in","r",stdin);
 freopen("B.out","w",stdout);
 scanf("%d",&t);
 
 for (i=1; i<=t; i++)
 {
  scanf("%d%d",&x,&y);
  for (l=0; l<x; l++)
   for (k=0; k<y; k++) scanf("%d",&m[l][k]);
   
  memset(ans,0,sizeof(ans));
  
  ch='a';
  for (l=0; l<x; l++)
   for (k=0; k<y; k++)
   {
     boo=true;
     for (j=0; j<4; j++)
     {
      nx=l+dx[j]; ny=k+dy[j];
      if (nx<0 || ny<0 || nx>=x || ny>=y) continue;
       if (m[l][k]<=m[nx][ny]) continue; else { boo=false; break; }
     }
    if (boo) 
     ans[l][k]=1;
   }
  
  for (l=0; l<x; l++)
   for (k=0; k<y; k++)
   {
    nx=l; ny=k;
    while ( ans[nx][ny]==0 )
    { 
     mini=maxlong;
     for (j=0; j<4; j++)
     {
      cx=nx+dx[j]; cy=ny+dy[j];
     if (cx<0 || cy<0 || cx>=x || cy>=y) continue;
      if ( m[cx][cy]<mini ) { mini=m[cx][cy]; bx=cx; by=cy; }
     }
     nx=bx; ny=by;
    }
    if (ans[nx][ny]==1) ans[l][k]=ans[nx][ny]=ch++; else ans[l][k]=ans[nx][ny];
   }  
   
  printf("Case #%d:\n",i);
  for (l=0; l<x; l++)
  {
   printf("%c",ans[l][0]);
   for (k=1; k<y; k++)
    printf(" %c",ans[l][k]);
   printf("\n");
  }  
  
 }
 
}
