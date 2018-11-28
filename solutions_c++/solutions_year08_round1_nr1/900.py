#include<iostream>
#include<vector>
using namespace std;
long long pro(vector<int>x, vector<int>y)
{ long long p=0;
  sort(x.begin(),x.end());
  sort(y.begin(),y.end());
  reverse(y.begin(),y.end());
  for(int i=0;i<x.size();i++)
  { p+=x[i]*y[i];
  }
  return p;
}
int main()
{ freopen("A-small.in","r",stdin);
  freopen("output.txt","w",stdout);
  int n,t,tem;
  
  cin>>n;
  for(int i=0;i<n;i++)
  { vector<int> a,b;
    cin>>t;
    for(int j=0;j<t;j++)
    { cin>>tem;
      a.push_back(tem);
    }
    for(int j=0;j<t;j++)
    { cin>>tem;
      b.push_back(tem);
    }
    cout<<"Case #"<<i+1<<": "<<pro(a,b)<<endl;
  }
}
