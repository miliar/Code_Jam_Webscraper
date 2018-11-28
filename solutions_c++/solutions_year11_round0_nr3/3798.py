#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
using namespace std;
vector<int>v;
bool flag=0;
int ret;
void ex(int n,int l)
{
     
     while(1)
     {
             int sum1=0;
             int sum2=0;
             int tot=0,x=0,y=0;
             if(n==0)return;
           for(int i=0;i<l;++i)
           {
                   if(n&(1<<i))
                   {
                               tot+=v[i];
                               sum1=sum1^v[i];
                               x++;
                   }
                   else
                   {
                       sum2=sum2^v[i];
                       y++;
                   }
           }
           if(x&&y&&tot>ret&&sum1==sum2)
           {flag=1;ret=tot;}
           n--;
     }
}
             
int main()
{
    
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,f,N=1,n;
    cin>>t;
    while(t--)
    {
              v.clear();
              flag=0;
              ret=-(int)1e8;
       cin>>f;
       int par=(1<<f)-1,F=f;
       while(f--)
       {
           cin>>n;
           v.push_back(n);
       }
       //cout<<par<<endl;
       ex(par,F);
       if(!flag)
       cout<<"Case #"<<N++<<": NO"<<endl;
       else
       cout<<"Case #"<<N++<<": "<<ret<<endl;
    }
}  
                     
                     
                     
