#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
#define sz(a)  int((a).size())
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)

//#include "cout.h"

main(){
  int _T; cin>>_T;//20
  rep(_t,_T){
    int A,B; cin>>A>>B; //1<=A<=99999,A<B<=100000

    vector<double> er(A);
    rep(i,A) cin>>er[i];

    vector<long double> ks(A+2);
    ks[0] = B-A+1;
    rep(i,A) ks[i+1] = ks[i]+2;
    ks[A+1] = 1+B+1;
    //cout <<ks<<endl;

    int pen=B+1;
    double r=1.0, psum=0.0;
    vector<long double> ps(A+1);
    long double ans = min(ks[A], ks[A+1]);
    for(int i=A-1;i>=0;--i){
      int j=A-1-i;
      double x=r*(1.0-er[j]); r*=er[j];
      psum += x; ps[j]=psum;
      ks[i] += psum*pen;
      ans = min(ans,ks[i]);
    }
    //cout<<ps<<endl;
    //cout<<ks<<endl;
    printf("Case #%d: %.6f\n", 1+_t, (double)ans);
  }
}
