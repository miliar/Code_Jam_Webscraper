/*
This program is develpoed by Ratan Dhorawat.
*/

#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#define f(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
using namespace std;


int main()
{
 
 int t,cas=0;
 cin>>t;
 while(t--){cas++;
  int n,l,h;
  cin>>n>>l>>h;
  int a[n];
  f(i,0,n)cin>>a[i];
  
  bool flag=false;
  int ans,k;
  for(int i=l;i<=h;i++)
  {      // cout<<i<<endl;
          for(k=0;k<n;k++)
          {
                  if(!(a[k]%i))continue;
                  else if(!(i%a[k]))continue;
                  else
                  break;
          }
          if(k==n)
          {
                  flag = true;
                  ans=i;
                  break;
          }
          
  }
  cout<<"Case #"<<cas<<": ";
  if(flag)
  cout<<ans<<endl;
  else
  cout<<"NO\n";
}
// system("pause");
 return 0;
}
