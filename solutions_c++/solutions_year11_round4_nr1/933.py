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
const int N=1005;
struct node
{
double bi,ei,wi;
};
node a[N];
int n;
double X,S,R,T;

bool cmp(const node& a,const node& b)
{
return a.wi<b.wi;
}

int main()
{
//freopen("A-large.in","r",stdin);
//freopen("A-large.out","w",stdout);
int t,i,ca=1;
double l,sp,res,v;
scanf("%d",&t);
while(t--)
{
 scanf("%lf%lf%lf%lf%d",&X,&S,&R,&T,&n);
 sp=0;
 for(i=0;i<n;i++)
 {
  scanf("%lf%lf%lf",&a[i].bi,&a[i].ei,&a[i].wi);
  sp+=a[i].ei-a[i].bi;
 }
 l=X-sp;
 sort(a,a+n,cmp);
 if(l/R<T||(fabs(l/R-T))<EPS)
 {
  res=l/R;
  T-=l/R;
  l=0;
 }
 else
 {
  res=T;
  l-=R*T;
  T=0;
 }
 if(fabs(l)>EPS)res+=l/S;
 for(i=0;i<n;i++)
 {
  l=a[i].ei-a[i].bi;
  v=R+a[i].wi;
  if(fabs(T)>EPS)
  {
   if(l/v<T||fabs(l/v-T)<EPS)
   {
    res+=l/v;
    T-=l/v;
    l=0;
   }
   else
   {
    res+=T;
    l-=v*T;
    T=0;
   }
  }
  if(fabs(l)>EPS)res+=l/(a[i].wi+S);
 }
 printf("Case #%d: %.8f\n",ca++,res);
}
return 0;
}
