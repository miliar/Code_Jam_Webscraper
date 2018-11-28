#include<iostream>
using namespace std;

int main() {
  cout.setf(ios::fixed);
  cout.precision(6);
  int t;
  cin>>t;
  for (int ncase=1;ncase<=t;++ncase) {
    int n,m;
    double l=0;
    cin>>n;
    for (int i=1;i<=n;++i) {
      cin>>m;
      if (m!=i) ++l;
    }
    cout<<"Case #"<<ncase<<": "<<l<<endl;
  }
}
