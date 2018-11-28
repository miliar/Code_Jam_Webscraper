#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<cstdlib>
#include<iomanip>
#include<map>
#include<set>
#include<vector>
#include<deque>
#include<queue>
#include<list>
#include<stack>
#include<algorithm>
#include<numeric>
#include<ctime>
#include<climits>
using namespace std;
const double EPS=1e-8;
const double PAI=4*atan(1.0);
const float FLOAT_MAX=1.0e38,FLOAT_MIN=-1.0e38;
const double DOUBLE_MAX=1.79e308,DOUBLE_MIN=-1.79e308;
const int N=15;
double a[N][N];
int r,c;
double d;

int main()
{
freopen("B-small-attempt0.in","r",stdin);
freopen("B-small-attempt0.out","w",stdout);
int t,i,j,k,ca=1,flag,x1,y1,op;
double x,y,x0,y0;
char cc;
scanf("%d",&t);
while(t--)
{
 scanf("%d%d%lf",&r,&c,&d);
 for(i=1;i<=r;i++)
 {
  scanf("\n");
  for(j=1;j<=c;j++)
  {
   scanf("%c",&cc);
   op=cc-'0';
   a[i][j]=d+op;
  }
 }
 flag=0;
 for(k=min(r,c);k>=3;k--)
 {
  for(i=1;i+k-1<=r&&!flag;i++)
   for(j=1;j+k-1<=c&&!flag;j++)
   {
      /*if(k%2==0)
      {
         x=0;y=0;
         x0=i+k/2;y0=j+k/2;
         for(y1=j+1;y1<=j+k-2;y1++)
         {

         }
      }
      else */
      {
         x=0;y=0;
         if(k%2==1){x0=i+k/2;y0=j+k/2;}
         else {x0=i+k/2-0.5;y0=j+k/2-0.5;}
         for(y1=j+1;y1<=j+k-2;y1++)
         {
          x+=(y1-y0)*a[i][y1];
          x+=(y1-y0)*a[i+k-1][y1];
         }
         for(x1=i+1;x1<=i+k-2;x1++)
          for(y1=j;y1<=j+k-1;y1++)
           x+=(y1-y0)*a[x1][y1];
         for(x1=i+1;x1<=i+k-2;x1++)
         {
          y+=(x1-x0)*a[x1][j];
          y+=(x1-x0)*a[x1][j+k-1];
         }
         for(y1=j+1;y1<=j+k-2;y1++)
          for(x1=i;x1<=i+k-1;x1++)
           y+=(x1-x0)*a[x1][y1];
         if(fabs(x)<EPS&&fabs(y)<EPS)flag=1;
      }
   }
  if(flag)break;
 }
 if(k>=3)printf("Case #%d: %d\n",ca++,k);
 else printf("Case #%d: IMPOSSIBLE\n",ca++);
}
return 0;
}
