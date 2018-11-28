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
const double EPS=1e-3;
const double PAI=4*atan(1.0);
const float FLOAT_MAX=1.0e38,FLOAT_MIN=-1.0e38;
const double DOUBLE_MAX=1.79e308,DOUBLE_MIN=-1.79e308;
int main()
{
//freopen("in.txt","r",stdin);
//freopen("A-large.out","w",stdout);
int t,n,i,p,flag,num,t1,t2,p1,p2,ca=1;
char r;
scanf("%d",&t);
while(t--)
{
 scanf("%d",&n);
 t1=t2=0;
 p1=p2=1;
 flag=-1;
 while(n--)
 {
  scanf(" ");
  scanf("%c%d",&r,&p);
  if(r=='O')
  {
   if(flag==0||flag==-1)
   {
    num=t1+abs(p-p1)+1;
    t1=num;
    p1=p;
   }
   else
   {
    num=max(t1+abs(p-p1)+1,num+1);
    t1=num;
    p1=p;
   }
   flag=0;
  }
  else
  {
   if(flag==1||flag==-1)
   {
    num=t2+abs(p-p2)+1;
    t2=num;
    p2=p;
   }
   else
   {
    num=max(t2+abs(p-p2)+1,num+1);
    t2=num;
    p2=p;
   }
   flag=1;
  }
 }
 printf("Case #%d: %d\n",ca++,num);
}
return 0;
}
