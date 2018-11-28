#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;
int main()
{
     freopen("C://Users//abir//Desktop//Topcoder//b.in","r",stdin);
     freopen("C://Users//abir//Desktop//Topcoder//b.out","w",stdout);
     
     long long int t1,i,j,k,n,b,t,c=1,p,q,x[1000],v[1000];
     cin>>t1;
     while(t1--)
     {
           cin>>n>>k>>b>>t;
           for(i=0;i<n;i++)cin>>x[i];      
           for(i=0;i<n;i++)cin>>v[i];
           p=0;
           q=0;
           bool vis[1000]={0};
           for(i=n-1;i>=0;i--)
           {
                //cout<<<<" "<<endl
                if(p==k)break;
                if((x[i]+v[i]*t)>=b)
                {
                    for(j=i+1;j<n;j++)
                    {
                        if(vis[j]==1)q++;    
                    }
                    p++;
                }
                else vis[i]=1;                     
           }            
          // cout<<p<<endl;
           if(p==k)cout<<"Case #"<<c++<<": "<<q<<endl;
           else cout<<"Case #"<<c++<<": IMPOSSIBLE"<<endl;
     }    
    return 0;
}
