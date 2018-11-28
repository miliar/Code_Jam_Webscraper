#include<iostream>
#include<vector>
using namespace std;

typedef vector<char> vc;
typedef vector<int> vi;

int main() {
  int t,n;
  cin>>t;
  for (int i=1;i<=t;++i) {
    cin>>n;
    vc robot(n);
    vi move(n);
    for (int j=0;j<n;++j) cin>>robot[j]>>move[j];
    vi oran(0),blue(0);
    for (int j=0;j<n;++j) {
      if (robot[j]=='O') oran.push_back(move[j]);
      else blue.push_back(move[j]);
    }
    int no=oran.size(),nb=blue.size();
    vi despor(no),despbl(nb);
    if (no) despor[0]=oran[0];
    for (int j=1;j<no;++j) despor[j]=(oran[j]-oran[j-1]<0?oran[j-1]-oran[j]:oran[j]-oran[j-1])+1;
    if (nb) despbl[0]=blue[0];
    for (int j=1;j<nb;++j) despbl[j]=(blue[j]-blue[j-1]<0?blue[j-1]-blue[j]:blue[j]-blue[j-1])+1;
    int io=0,ib=0,o=0,b=0,real=0;
    for (int j=0;j<n;++j) {
      if (robot[j]=='O') {
// cerr<<j<<' '<<o+despor[io]<<' '<<b<<' '<<real<<endl;
        o+=despor[io];
        if (real<o) real=o;
        else {
          ++real;
          o=real;
        }
        ++io;
      } else {
// cerr<<j<<' '<<o<<' '<<b+despbl[ib]<<' '<<real<<endl;
        b+=despbl[ib];
        if (real<b) real=b;
        else {
          ++real;
          b=real;
        }
        ++ib;
      }
// cerr<<j<<' '<<o<<' '<<b<<' '<<real<<endl;
    }
    cout<<"Case #"<<i<<": "<<real<<endl;
  }
}
