#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int cas,tt;
int main()
{
  freopen("dance.in","r",stdin);
  freopen("dance.out","w",stdout);
  cin>>cas;
  while (cas--)
  {
    int n,s,p,c,ans,t;
    ans=t=0;
    cin>>n>>s>>p;
    for(int i=0;i<n;i++)
    {
      cin>>c;
      if(c%3==1&&c/3+1>=p)ans++;
      if(c%3==0)
        if(c/3>=p)ans++;else if(c/3+1>=p&&c>=3)t++;
      if(c%3==2)
        if(c/3+1>=p)ans++;else if(c/3+2>=p)t++;
    }
    printf("Case #%d: %d\n",++tt,ans+min(t,s));
  }
  return 0;
}
