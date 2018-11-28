#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;

int N;
double J[200];
double Y[200];

int run() {
  double JJ=0.0;
  for (int i=0;i<N;++i)
    JJ += J[i];
  for (int i=0;i<N;++i)
    Y[i] = 1.0;
  int M;
  for(;;) {
    double JJJ=0.0;
    M=0;
    for (int i=0;i<N;++i) {
      if (Y[i]!=0.0) {
	M++;
	JJJ += J[i];
      }
    }
    double c = (JJ + JJJ) / M; 
    cerr <<"M="<<M<<" JJJ="<<JJJ<<" c="<<c<<endl;
    int changed = 0;
    for (int i=0;i<N;++i) {
      if (Y[i]>0) {
	Y[i] = (c - J[i])/JJ;
	if (Y[i]<0.0) {
	  Y[i]=0.0;
	  changed = 1;
	}
      } 
    }
    if (!changed)
      break;
  }
  for (int i=0;i<N;++i) {
    cout<<setprecision(10)<<" "<<Y[i]*100.0;
  }
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin>>N;
    for (int i=0;i<N;++i)
      cin >> J[i];
    cout<<"Case #"<<Ti<<":";
    run();
    cout<<endl;
  }
}
