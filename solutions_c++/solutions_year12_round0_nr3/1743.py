#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int used[2100000];

int main()
{
  int i,j,l,t,a,b,mo,ans,cnt,x;
  scanf("%d",&t);
  for (l=0;l<t;l++)
  {
    memset(used,0,sizeof(used));
    scanf("%d%d",&a,&b);
    mo=1;
    while (mo<=b) mo*=10;
    ans=0;
    for (i=a;i<=b;i++)
      if (used[i]==0)
      {
        cnt=0;
        x=i;
        while (1)
        {
          if ((x>=a)&&(x<=b))
          {
            used[x]=1;
            cnt++;
          }
          x=x*10;
          x+=x/mo;
          x%=mo;
          if (x==i) break;
        }
        ans+=cnt*(cnt-1)/2;
      }
    printf("Case #%d: %d\n",l+1,ans);
  }
}
