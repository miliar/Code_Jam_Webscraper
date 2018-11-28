#include<cstdio>
#include<iostream>
#include<cmath>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<sstream>
#include<vector>
#include<utility>
#include<map>
#include<cstdlib>
#include<limits.h>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
 int t,count=0;
 freopen("C-small-attempt0.in","r",stdin);
 freopen("output.out","w",stdout);
 cin>>t;
 vector <int> res;
 while(t--)
 {
  int p,k,l;
  res.clear();
  cin>>p>>k>>l;
  count++;
  int i,j,a;
  for(i=0;i<p;i++)
  {
          cin>>a;
          res.push_back(a);
  }
  
  int f = 0;
  for(i=k;i<=l;i++)
  {
                   int flag = 0;
                   for(j=0;j<res.size();j++)
                   if(res[j] % i == 0 || i % res[j] == 0);
                   else {flag = 1;break;}
                   if(flag == 0)
                   {cout<<"Case #"<<count<<": "<<i<<endl;f=1;break;}
  }
  if(f == 0)
  cout<<"Case #"<<count<<": NO"<<endl;
  
  }
 return 0;
 }

