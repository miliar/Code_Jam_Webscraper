#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <ext/hash_set>
#include <ext/hash_map>
using namespace std;


long long cant(string s)
{
  long long res=1;
  for(int i=1;i<s.size();i++)
    if(s[i]!=s[i-1])
      res++;
  return res;
}

int main()
{
  int n;
  cin>>n;
  
  for(int i=0;i<n;i++)
  {
          
     vector<int> vec(0);
          
      cout<<"Case #"<<i+1<<": ";
     int a;

       
       
     cin>>a;
          for(int j=0;j<a;j++)
       vec.push_back(j);
     string s;
     cin>>s;

     string tmp=s;
     
     int res=1000000;
     do
     {
     int ppar=0;
     
       for(int j=0;j<s.size()/a;j++)
       {
          for(int k=0;k<a;k++)
          {
            tmp[ppar+k]=s[ppar+vec[k]];    
          }
     ppar+=a;
       }    
     
     
     res=min((long long)res,cant(tmp));
     } 
     while(next_permutation(vec.begin(),vec.end()));
       
     cout<<res<<endl;
     }
}
