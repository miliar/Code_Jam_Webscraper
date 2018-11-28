#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<cmath>
#include<utility>
using namespace std;
int main()
{
    vector<pair<int,int> > v;
    pair<int,int> p;
    int t,n,count=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
            cin>>n;
            v.clear();
            for(int j=0;j<n;j++)
            {
                    cin>>p.first>>p.second;
                    v.push_back(p);      
            }
            count=0;
            for(int j=0;j<v.size();j++)
            {
                    for(int k=j+1;k<v.size();k++)
                    {
                            if((v[j].first>v[k].first)&&(v[j].second<v[k].second))
                                  { count++;}
                            else if((v[j].first<v[k].first)&&(v[j].second>v[k].second))
                                { count++;}
                    }
            }
            
            cout<<"Case #"<<i+1<<": "<<count<<endl;
            
    }
    return 0;
}
