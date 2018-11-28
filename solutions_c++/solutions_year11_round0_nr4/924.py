#include<iostream>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<deque>
#include<stack>
#include<algorithm>
#include<queue>
#include<map>
#include<cstdio>
using namespace std;
int main()
{int t,cs=0;
int n;
int a[1010];
cin>>t;
while(t--)
{cs++;
          cin>>n;
          for(int i=1;i<=n;i++)
          cin>>a[i];
          double cnt=0;
          for(int i=1;i<=n;i++)
          {
                  if(a[i]!=i) cnt++;
                  }
                  printf("Case #%d: %0.6f\n",cs,cnt);
          
          }



return 0;
}
