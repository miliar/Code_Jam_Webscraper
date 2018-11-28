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
string a,b,ret;
int A(char c)
{
     if(a.size()==0)return 0;
     int i=ret.size()-1;
     if((ret[i]==a[1]&&c==a[0])||(ret[i]==a[0]&&c==a[1])) {ret.erase(i,1);ret+=a[2];return 1;}
     return 2;
}
int B(char c)
{
     if(b.size()==0)return 0;
     int s=2;
     if(c==b[0])s=1;
     else if(c==b[1])s=0;
     for(int i=0;i<ret.size();++i)
     {
             if(s<2&&ret[i]==b[s]) {ret="";return 1;}
     }
     return 2;
}
int main()
{
    
   freopen("B-small-attempt0.in","r",stdin);
   freopen("out.txt","w",stdout);
    int t,f,N=1,n;
    char c;
    cin>>t;
    while(t--)
    {
              a="";
              b="";
            cin>>n;
            if(n) cin>>a;
            
            cin>>n;
            if(n) cin>>b;
            
            cin>>n;
            ret="";
            for(int i=0;i<n;++i)
            {
                    cin>>c;
                    if(ret.size()==0)ret+=c;
                    else if(A(c)!=1)
                    {
                               if(B(c)!=1)
                               ret+=c;
                    }   
            }
             cout<<"Case #"<<N++<<": [";
               for(int i=0;i<ret.size();++i)
               {
                       cout<<ret[i];
                       if(i<ret.size()-1)cout<<", ";
               }
               cout<<"]"<<endl;
    }
}  
                     
                     
                     
