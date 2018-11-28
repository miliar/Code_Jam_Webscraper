#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;

int N, D;

int d[20000];
int l[20000];
int good[20000];

int compute(int k,int h) {
  if (d[k]+h >= D) {
    return 1;
  }
  for (int j=k+1;j<N;++j) {
    if (d[k]+h>=d[j]) {
      int hh = d[j]-d[k];
      if (l[j]<hh) hh = l[j];
      int r = compute(j,hh);
      if (r) return 1;
    }
  }
  return 0;
}

main() {
  int T;
  cin>>T;
  for (int Ti=1; Ti <= T; ++Ti) {
    cerr<<"Computing test: "<<Ti<<endl;
    cin >> N;
    for (int i=0;i<N;++i) {
      cin >> d[i] >> l[i];
    }
    cin >> D;
    cout<<"Case #"<<Ti<<": ";
    if (d[0] <= l[0] && compute(0,d[0]))
      cout << "YES";
    else
      cout << "NO";
    cout<<endl;
  }
}
