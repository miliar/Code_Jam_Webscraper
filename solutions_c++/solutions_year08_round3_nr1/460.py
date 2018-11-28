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
 long long t,kase=0;
 ifstream is("input.in");
 ofstream os("output.out");
 is>>t;
 while(t--)
 {
  long long p,k,l,total=0;
  is>>p>>k>>l;
  kase++;
  vector<long long>v(l);
  vector<long long>m(k,0);
  for(long long i=0;i<l;i++)
  is>>v[i];
  sort(v.begin(),v.end());
  long long n=l-1;
  while(n>=0)
  {
  bool found=false;
  for(long long j=0;j<k;j++)
  {
   if(m[j]<p)
   {
     m[j]++;
     total+=m[j]*v[n];
     n--;
     found=true;
     }
    if(n<0)
    break;
    }
    if(!found)
    break;
   }
  os<<"Case #"<<kase<<": "<<total<<endl;
  }
 return 0;
 }

