#include<stdio.h>
#include<string.h>
#include<limits.h>
#include<stdlib.h>
#include<iostream>
#include<deque>
#include<vector>
#include<list>
#include<stack>
#include<algorithm>
#include<math.h>
#include<map>

#define MOD 1000000007
using namespace std;
int main()
{
  int t,c,n,s,p,sup,tot,i,rem,same;
  int a[111];
  scanf("%d",&t);
  for(c=1;c<=t;c++)
  {
    tot=0;
    sup=0;
    scanf("%d%d%d",&n,&s,&p);
    for(i=0;i<n;i++)
      scanf("%d",&a[i]);
    for(i=0;i<n;i++)
    {
      same=a[i]/3;
      rem=a[i]%3;
      if(rem==0)
      {
        if(same>=p) tot++;
        else if(same+1>=p && same-1>=0) sup++;
      }
      else if(rem==1)
      {
        if(same+1>=p) tot++;
      }
      else
      {
        if(same+1>=p) tot++;
        else if(same+2>=p) sup++;
      }
    }
    if(s>=sup) tot+=sup;
    else tot+=s;
    printf("Case #%d: %d\n",c,tot);
  } 
  return 0;
}
