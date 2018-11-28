#include<iostream>
#include<vector>
#include<map>
#include<cmath>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<stack>
#include<queue>

using namespace std;

int main()
{
     int t,i,j,k,n,x,y,c;
     vector<pair<int,int> > v;
     cin>>t;
     for(i=1;i<=t;i++)
     {
          v.clear();
          cin>>n;
          c=0;
          for(j=0;j<n;j++)
          {
               cin>>x>>y;
               v.push_back(make_pair(x,y));
          }
          sort(v.begin(),v.end());
          for(j=0;j<n-1;j++)
          {
               for(k=j+1;k<n;k++)
               {
                    if(v[j].second>v[k].second) c++;
               }
          }
          cout<<"Case #"<<i<<": ";
          cout<<c;
          cout<<"\n";
     }
     //system("pause");
     return 0;
}
