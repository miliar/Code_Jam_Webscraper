# include <list>
# include <algorithm>
# include <numeric>
# include <sstream>
# include <iostream>
# include <iomanip>
# include <cstdio>
# include <cmath>
# include <cstdlib>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <deque>
# include <stack>
# include <vector>
# include <cstring>
# include <fstream>

typedef long long int lli;
typedef unsigned long long ull;

using namespace std;

int main()
{
int n,a[100],t,s,p,qt,rem;
lli sum;
cin>>t;
for(int i=1;i<=t;i++)
{
  sum = 0;
  cin>>n>>s>>p;
  for(int j=0;j<n;j++)
    cin>>a[j];
  for(int j=0;j<n;j++)
  {
    qt = a[j]/3;
    rem = a[j] % 3;
    if(qt>=p)
      {sum++;continue;}
    else if(a[j]>=p)
    {
      if(rem==0)
      {
        if(s>0 && (qt+1)>=p)
          {sum++;s--;}
      }
      else if(rem==1)
      {
        if(qt+1>=p)
          sum+=1;
      }
      else
      {
        if(qt+1>=p)
          sum++;
        else if(s>0 && (qt+2)>=p)
          {sum++;s--;}
      }
    }
  }
  printf("Case #%d: %lld\n",i,sum);
}
return 0;
}


