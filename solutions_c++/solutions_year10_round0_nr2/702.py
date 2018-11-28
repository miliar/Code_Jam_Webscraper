//******************************************
// This code uses the Number Theory Library
// http://www.shoup.net/ntl/
//
//*****************************************
#include <NTL/ZZ.h>

#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
using namespace NTL;

ZZ LCM(ZZ &a, ZZ &b) {
  ZZ ret;
  ret  = (a*b)/GCD(a,b);
  return ret;
}
int main() {
  int C;

  cin >> C;
  for (int i=1;i<=C;i++) {
    vector<ZZ> vals;
    int N;
    cin >> N;
    vals.resize(N);
    for (int j=0;j<N;j++) {
      cin >> vals[j];
    }

    vector<ZZ> diffs;
    diffs.clear();
    sort(vals.begin(),vals.end());
    //cout << "***" << endl;
    //for (int l=0;l<vals.size();l++) {
    //  cout << "\t" << vals[l] << endl;
    //}
    for (int l=0;l<vals.size();l++) {
      for (int ln=l+1;ln<vals.size();ln++) {
	if (vals[l]!=vals[ln]) {
	  diffs.push_back(vals[ln]-vals[l]);
	}
      }
    }
    ZZ g = diffs[0];
    for (int l=1;l<diffs.size();l++) {
      g = GCD(g,diffs[l]);
    }
    // g == Maximum T

    // y == 
    ZZ y;
    if (g==1) {
      y=0;
    } else {
      ZZ a = vals[0]%g;
      if (a==0) {
	y=0;
      } else {
	y = g - a;
      }
    }
    /* cout << "*** " << g << endl;
    for (int l=0;l<vals.size();l++) {
      cout << vals[l]%g << endl;
      cout << vals[l] << endl;
      assert((vals[l]+y)%g == 0);
      //cout << g << endl;
      //cout << (vals[l]+y)%g  << endl;
      } 
    */
    cout << "Case #"<<i<<": " << y <<endl;
  }
}

    // 
