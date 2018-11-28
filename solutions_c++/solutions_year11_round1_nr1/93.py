#include <stdio.h>
#include <math.h>
#include <algorithm>
#define ll long long
using namespace std;
ll gcd(ll a,ll b)
{
  while(b!=0)
    {
      ll t=b;
      b=a%b;
      a=t;
    }
  return a;
}
ll absval(ll x)
{
  if(x<0)
    return -x;
  else
    return x;
}
ll lcm(ll x,ll y)
{
  return (x/gcd(x,y))*y;
}
ll PD,PG,N;
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      scanf("%lld%lld%lld",&N,&PD,&PG);
      ll p1=PD/gcd(PD,100);
      ll q1=100/gcd(PD,100);
      ll p2=PG/gcd(PG,100);
      ll q2=100/gcd(PG,100);
      ll a=q2*p1-q1*p2;
      ll b=p2*q1;
      ll c=q1*q2;
      //printf("%lld %lld %lld\n",a,b-c,b);
      ll gval=gcd(absval(b-c),gcd(a,b));
      ll x=a/gval;
      ll y=(b-c)/gval;
      ll z=b/gval;
      //y* v1 + z* v2 must be x* v3 where vi>=0
      //printf("%lld %lld %lld\n",x,y,z);
 

      
      if(lcm(q1,gcd(absval(y),absval(z)))>N ||(y>=0 && z>=0 && x<0)  || (y<=0 && z<=0 && x>0) || (x==0 && y*z>0))
	printf("Case #%d: Broken\n",t);
      else
	printf("Case #%d: Possible\n",t);
    }
}
