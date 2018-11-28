#include <iostream>
#include <algorithm>
using namespace std;
bool cmp1(const int &a,const int &b)
{
  return a>b;
}
bool cmp2(const int &a,const int &b)
{
  return a<b;
}
int n,x[1000],y[1000];
int main()
{
  int t,n,i,cs=0,sum=0;
  scanf("%d",&t);
  while(t--)
    {
      cs++;
      scanf("%d",&n);
      for(i=0;i<n;i++)
	scanf("%d",&x[i]);
      for(i=0;i<n;i++)
	scanf("%d",&y[i]);
      sort(x,x+n,cmp1);
      sort(y,y+n,cmp2);
      sum=0;
      for(i=0;i<n;i++)
	sum+=(x[i]*y[i]);
      printf("Case #%d: %d\n",cs,sum);
    }
  return 0;
}
