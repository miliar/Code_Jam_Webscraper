#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long P,K,L,i,j,k,Lj,sum,m;
vector<long long> v;

int main()
{
    //freopen("i.txt","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("o.txt","w",stdout);
    int n;
    cin>>n;
    
    for(i=0;i<n;i++)
    {
           cin>>P;
           cin>>K;
           cin>>L;
           sum=0;
           m=1;
           if(P*K < L)
           {
                  cout<<"Case #"<<i+1<<": "<<"Impossible"<<endl;
                  continue;
           }
           
           for(j=0;j<L;j++)
           {
                           cin>>Lj;
                           v.push_back(Lj);
           }
           sort(v.begin(),v.end());
           reverse(v.begin(),v.end());
           
           
           for(k=0;k<L;k++)
           {
                           sum+=v[k]*m;
                           if((k+1)%K==0)
                                         m++;               
           }
           cout<<"Case #"<<i+1<<": "<<sum<<endl;
           sum=0;
           m=1;
           v.erase(v.begin(),v.end());
    }
    
    return 0;
}
