#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;i++)
  {
    int n,s,p;
    scanf("%d%d%d",&n,&s,&p);
    int s1=3*p-2,s2=3*p-4,sc=0,sc1=0;
    s2=max(s2,2);
    while(n--)
    {
      int t1;
      scanf("%d",&t1);
      if(t1>=s1)
      {
        sc++;
      }
      else if(t1>=s2)
      {
        sc1++;
      }
    }
    sc+=min(s,sc1);
    printf("Case #%d: %d\n",i,sc);
  }
  return 0;
}
