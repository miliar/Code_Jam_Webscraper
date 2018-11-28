#define mset(a) memset(a,0,sizeof(a))

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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int t,p,m[3000],money[3000];
int mypow(int p)

 {int ans=1;
     for(int i=1;i<=p;i++)
        ans*=2;
 return ans;
 }

int main()
{
cin >>t;
for(int tt=1;tt<=t;tt++)
 {mset(m);
  cin >>p;
  int ans=0;
  int p2=mypow(p);
  int temp;
  for(int i=1;i<=p2;i++)
    scanf("%d",&m[p2+i-1]);
  for(int i=p-1;i>=0;i--)
    for(int j=1;j<=mypow(i);j++)
      scanf("%d",&temp);
  for(int i=p2-1;i>=1;i--)
    if(m[2*i]>0&m[2*i+1]>0)
      m[i]=min(m[2*i],m[2*i+1])-1;
    else {m[i]=0;ans++;}

  printf("Case #%d: %d\n",tt,ans);
 }
return 0;
}
