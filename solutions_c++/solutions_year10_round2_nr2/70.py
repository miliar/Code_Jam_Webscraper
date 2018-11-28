#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n,k,b,t;
vector<int> start,vel;
int calc()
{
  vector<int> end(n);
  vector<int> cpos;
  int i,rv=0;
  reverse(start.begin(),start.end());
  reverse(vel.begin(),vel.end());
  for(i=0;i<n;++i) end[i]=(b-start[i]+vel[i]-1)/vel[i];
  for(i=0;i<n;++i) if(end[i]<=t) cpos.push_back(i);
  if(cpos.size()<k) return -1;
  for(i=0;i<k;++i) rv+=cpos[i]-i;
  return rv;
}

int main()
{
  int ci,cn,i;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  {
    cin>>n>>k>>b>>t;
    start.resize(n); vel.resize(n);
    for(i=0;i<n;++i) cin>>start[i];
    for(i=0;i<n;++i) cin>>vel[i];
    int res=calc();
    cout<<"Case #"<<ci<<": ";
    if(res<0) cout<<"IMPOSSIBLE"<<endl;
    else cout<<res<<endl;
  }
}
