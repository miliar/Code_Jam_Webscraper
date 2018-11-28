#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

void process()
{
  int k;cin>>k;
  int n;cin>>n;
  vector<int> ds(n);
  for (int i=0;i<n;i++) cin>>ds[i];
  vector<int> ns(k,0);

  int p=-1;
  for (int i=1;i<=k;i++){
    int r=i%(k+1-i);
    if (r==0) r=(k+1-i);
    while(r--){
      p=(p+1)%k;
      while(ns[p]!=0) p=(p+1)%k;
    }
    ns[p]=i;
  }

  for (int i=0;i<n;i++){
    if (i!=0) cout<<" ";
    cout<<ns[ds[i]-1];
  }
  cout<<endl;
}

int main()
{
  string line;
  getline(cin,line);
  int cases=atoi(line.c_str());
  for (int c=1;c<=cases;c++){
    cout<<"Case #"<<c<<": ";
    process();
  }
}
