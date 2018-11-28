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
#include<algorithm>
using namespace std;
int main()
{
 int t,count=0;
 cin>>t;
 while(t--)
 {
  int n,p=0;
  count++;
  cin>>n;
  vector<int>x(n),y(n);
  for(int i=0;i<n;i++)
  cin>>x[i];
  for(int i=0;i<n;i++)
  cin>>y[i];
  sort(x.begin(),x.end());
  sort(y.begin(),y.end());
  for(int i=0;i<n;i++)
  p=p+x[n-i-1]*y[i];
  cout<<"Case #"<<count<<": ";
  cout<<p<<endl; 
  }
 return 0;
 }
