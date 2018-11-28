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
//freopen("A-large.in","r",stdin);
//freopen("A-large.out","w",stdout);
int t,pd,pg,pp,i,ca=1;
long long n;
scanf("%d",&t);
while(t--)
{
 scanf("%lld%d%d",&n,&pd,&pg);
 printf("Case #%d: ",ca++);
 if((pd<100&&pg==100)||(pd>0&&pg==0)){printf("Broken\n");continue;}
 pp=100;
 for(i=2;i<=5;i++)
 {
  while(pd%i==0&&pp%i==0)
  {
   pd/=i;pp/=i;
  }
 }
 if(pp>n)printf("Broken\n");
 else printf("Possible\n");
}
return 0;
}
