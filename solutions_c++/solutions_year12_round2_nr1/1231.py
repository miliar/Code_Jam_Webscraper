#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
using namespace std;

vector<pair<double,int> >v;
vector<pair<int,double> >w;

int main()
{
    freopen("A111.in","r",stdin);
    freopen("A111o.txt","w",stdout);
    int t,x=0,i,j,k;
    double sum=0,a[250],sums;
    cin>>t;
    while(t--)
    {
          v.clear();
          w.clear();    
          int n;
          cin>>n; 
          sum=0;   
          for(i=0;i<n;i++)
          {
                cin>>a[i];
                v.push_back(make_pair(a[i],i));
                sum+=a[i];
          }
          cout<<"Case #"<<++x<<":";
          sums=sum*2;
          sort(v.begin(),v.end());
          
          for(i=v.size()-1;i>=0;i--)
          {
                 if(v[i].first>=sums/n)
                 {
                      w.push_back(make_pair(v[i].second,0)); 
                      sums-=(v[i].first);
                      n--;
                 }
                 else
                 {
                     w.push_back(make_pair(v[i].second,100*(sums/n-v[i].first)/sum));
                 }
          }
          
          sort(w.begin(),w.end());
          
          for(i=0;i<w.size();i++)
          printf(" %.6f",w[i].second);
          cout<<endl;
    }    
}  
