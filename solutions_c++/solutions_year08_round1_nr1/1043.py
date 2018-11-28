#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


int main()
{
  int T,n,i;
  long long int tmp;
  long long int INF = 90000000;
  long long int sum,minsum;
  vector<int> a,b;
  cin>>T;
  for(int iter=1;iter<=T;iter++)
  {
    cin>>n;
    a.clear();b.clear();
    for(i=0;i<n;i++) {cin>>tmp;a.push_back(tmp);}
    for(i=0;i<n;i++) {cin>>tmp;b.push_back(tmp);}
    minsum=INF;
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    minsum=0;
    for(int i=0;i<a.size();i++)
    {
      minsum+=a[i]*b[n-i-1];
    }  
    cout<<"Case #"<<iter<<": "<<minsum<<endl;
  }
  return 0;
}  