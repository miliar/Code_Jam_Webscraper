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
 long long t,count=0;
 freopen("A-large(2).in","r",stdin);
 freopen("output.out","w",stdout);
 cin>>t;
 while(t--)
 {
  long long p,i,j;
  int k,l;
  cin>>p>>k>>l;
  count++;
  int flag = 0;
  for(j=1;j<=p;j++)
  {
    long long j2 = j*k/100;
    double j1 = (j*1.0*k)/100;
    if(j1 == j2)
    {i=j2;flag = 1;break;}
  }
  
  if(flag == 0)
  {cout<<"Case #"<<count<<": Broken\n";continue;}
  if(k != 100 && l == 100)
  {cout<<"Case #"<<count<<": Broken\n";continue;}
  if(k == l)
  {cout<<"Case #"<<count<<": Possible\n";continue;}
  
  // cout<<i<<" "<<j<<endl;
  map <long long,int> m;
  long long a1 = i;
  flag = 0;
       for(int a = 1;a<=1000000;a++)
       {
             /*int rem = i%l;
             if(m[rem] == 1)
             {flag = 1;break;}
             m[rem] = 1;
             while(i<l)
             i *= 10;*/
       
             int tot = j+a;
             double c = (tot*1.0*l)/100;
             int d = (int)c;
             if(c == d)
             {
                  if(d >= i)
                  {flag = 1;
                  // cout<<d<<" "<<tot<<endl;
                  break;}
             }
       }
       if(flag == 1)
       {cout<<"Case #"<<count<<": Possible\n";continue;}
  cout<<"Case #"<<count<<": Broken\n";continue;
  // cout<<"Case #"<<count<<": Possible\n";continue;
  
  }
 return 0;
 }

