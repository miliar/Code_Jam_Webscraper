#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
}

long long dot(const vector<long long>& a,const vector<long long>& b){
  long long ret=0;
  for(int i=0;i<a.size();i++)
    ret+=a[i]*b[i];
  return ret;
}

long long solve(){
  int n;
  cin>>n;
  vector<long long> a(n),b(n);
  for(int i=0;i<a.size();i++)
    cin>>a[i];
  for(int i=0;i<b.size();i++)
    cin>>b[i];
  sort(a.begin(),a.end());
  sort(b.begin(),b.end());
  reverse(a.begin(),a.end());
  return dot(a,b);
}
