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
const int N=20;
int a[N];

int main()
{
//freopen("C-large.in","r",stdin);
//freopen("C-large.out","w",stdout);
int t,i,res,n,ca=1,sum;
scanf("%d",&t);
while(t--)
{
 scanf("%d",&n);
 res=0;
 sum=0;
 for(i=0;i<n;i++)
 {
  scanf("%d",&a[i]);
  res^=a[i];
  sum+=a[i];
 }
 printf("Case #%d: ",ca++);
 if(res!=0)printf("NO\n");
 else printf("%d\n",sum-*min_element(a,a+n));
}
return 0;
}
