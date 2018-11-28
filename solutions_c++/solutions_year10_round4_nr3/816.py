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
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int c,r,x11,x22,y11,y22;
bool a[505][505],cc[505][505];
int main()
{mset(a);
cin >>c;
for(int p=1;p<=c;p++)
 {
  cin >>r;
  for(int i=1;i<=r;i++)
    {
     cin>>x11>>y11>>x22>>y22;
     for(int x=x11;x<=x22;x++)
       for(int y=y11;y<=y22;y++)
         a[x][y]=true;

    }


  bool b=true;
  int ans=0;
  while(b)
   {b=false;
    ans++;
    //cout <<ans<<endl;
    for(int i=1;i<=250;i++)
      for(int j=1;j<=250;j++)
        {cc[i][j]=a[i][j];
         if((a[i-1][j]==false)&&(a[i][j-1]==false))
           cc[i][j]=false;
        if((a[i-1][j]==true)&&(a[i][j-1]==true))
          cc[i][j]=true;
        if(cc[i][j])
          b=true;
        }

    for(int i=1;i<=250;i++)
      for(int j=1;j<=250;j++)
        a[i][j]=cc[i][j];
  }
  printf("Case #%d: %d\n",p,ans);
 }
return 0;
}
