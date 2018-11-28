#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("a.out","w",stdout);
    long long n,p,pd,pg;
    bool r = true;
    bool t;
    cin>>n;
    for(int i=0;i<n;i++)
    {
     cin>>p>>pd>>pg;
     r = true;
     t = false;
     cout<<"Case #"<<i+1<<": ";
     for(int  j = 1; j<=p; j++)
     {
      if(j>100)break;
      if(j*pd%100 == 0)
      {
       t = true;
       break;            
      }               
     }
     if(t != true)
     {
      r = false;     
     }
     if(pg == 100 && pd != 100)
     {
      r = false;
     }
     if(pg == 0 && pd != 0)
     {
      r = false;
     }
     if(r == true)
      cout<<"Possible"<<endl;
     else
      cout<<"Broken"<<endl;
    }
    return 0;
}
