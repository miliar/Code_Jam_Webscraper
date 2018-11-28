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

int main()
{
  int i,l,t,n,s,p,x,ans;
  scanf("%d",&t);
  for (l=0;l<t;l++)
  {
    scanf("%d%d%d",&n,&s,&p);
    ans=0;
    for (i=0;i<n;i++)
    {
      scanf("%d",&x);
      if (x>=p+p-1+p-1)
        ans++;
      else
      {
        if ((s>0)&&(p>1)&&(x>=p+p-2+p-2))
        {
          ans++;
          s--;
        }
      }
    }
    printf("Case #%d: %d\n",l+1,ans);
  }
}
