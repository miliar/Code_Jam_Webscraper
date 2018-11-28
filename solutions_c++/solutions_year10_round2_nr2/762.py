#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<stdio.h>
using namespace std;

long long an=0;

bool sf(pair<int,int> a,pair<int,int> b)
{
    return a.first-b.first;
}

int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    an=0;
    double n,k,b,t;
    cin>>n>>k>>b>>t;
    vector<pair<int,int> > xv;
    xv.clear();
    for(int j=0;j<n;j++)
    {
        int q;
        cin>>q;
        xv.push_back(make_pair(q,0));
    }
    for(int j=0;j<n;j++)
    {
        cin>>xv[j].second;
    }
   // sort(xv.begin(),xv.end(),sf);
   vector<pair<int,int> > zx;
   for(int j=n-1;j>=0;j--)
        zx.push_back(xv[j]);
    for(int j=0;j<n;j++)
        xv[j]=zx[j];
    int mk=0,dd=0;
    for(int j=0;j<n && mk<k;j++)
    {// 
    //   cout<<xv[j].first<<" "<<xv[j].second<<endl;
        if((b-xv[j].first)/xv[j].second<=t)
        {
            mk++;
            an+=dd;
        }
        else
        {
            dd++;
        }
    }
    if(mk<k)
    {
        cout<<"Case #"<<i<<": IMPOSSIBLE\n";
    }
    else
    {
        cout<<"Case #"<<i<<": "<<an<<endl;
    }
}
 // system("pause");
  return 0;
}
