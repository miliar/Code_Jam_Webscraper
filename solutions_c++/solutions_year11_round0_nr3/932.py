#include<iostream>
using namespace std;

const int inf=1000001;

int main() {
  int t;
  cin>>t;
  for (int ncase=1;ncase<=t;++ncase) {
    int n,cur,psum=0,sum=0,mini=inf;
    cin>>n;
    for (int i=0;i<n;++i) {
      cin>>cur;
      psum=psum xor cur;
      sum+=cur;
      if (cur<mini) mini=cur;
    }
    if (psum) cout<<"Case #"<<ncase<<": NO"<<endl;
    else cout<<"Case #"<<ncase<<": "<<sum-mini<<endl;
  }
}
