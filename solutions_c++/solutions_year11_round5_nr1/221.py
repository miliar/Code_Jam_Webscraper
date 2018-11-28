
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long LL;
typedef complex<double> P;


void init(void) {
  // init_primes();
}

const double EPS = 1e-10;

double area(const P& a, const P& b) {
  return (a.imag() + b.imag()) * (b.real() - a.real());
}

P lower[1234];
P upper[1234];
void solve(void) {
//   cerr << "HOGE"<< endl;
  double width;
  int nLower, nUpper;
  double div;
  cin >> width >> nLower >> nUpper >> div;
//   cout <<  width  << nLower << nUpper << div;

  double allarea = 0;
  
  REP(i, nLower){
    cin >> lower[i].real() >> lower[i].imag();
    if(i > 0){
      allarea -= area(lower[i-1], lower[i]);
    }
  }
  REP(i, nUpper){
    cin >> upper[i].real() >> upper[i].imag();
    if(i > 0){
      allarea += area(upper[i-1], upper[i]);
    }
  }
  
  double divarea = allarea / div;
  
  int li = 0;
  int ui = 0;
  double curarea = 0;
  double curX = 0;
  P top = upper[0], bottom = lower[0];
  cout << endl;
//   cerr << "FUGA" << endl;
  for(int d = 0; d < div-1; ){
    double nextX;
    P nextTop, nextBottom;
    if(lower[li+1].real() < upper[ui+1].real()){
      nextX = lower[li+1].real();
      nextTop = top + (upper[ui+1] - top) * (nextX - curX) / (upper[ui+1].real() - curX);
      nextBottom = lower[li+1];
    }else if(upper[ui+1].real() < lower[li+1].real()){
      nextX = upper[ui+1].real();
      nextTop = upper[ui+1];
      nextBottom = bottom + (lower[li+1] - bottom) * (nextX - curX) / (lower[li+1].real() - curX);
    }else{
      nextX = upper[ui+1].real();
      nextTop = upper[ui+1];
      nextBottom = lower[li+1];
    }

//     cerr << "PIYO!" << endl;
    double a = area(top, nextTop) - area(bottom, nextBottom);
//     cerr << curX << ", " << nextX << " : " << curarea << " " << a << endl;
    if(curarea + a >= divarea){
      double ux = nextX;
      double lx = curX;
      while(lx + EPS < ux){
//       cerr << "(" << lx << ", " << ux << ")" << endl;
	double mx = (ux + lx)/2;
	P ttt = top + (nextTop - top) * (mx - curX) / (nextX - curX);
	P bbb = bottom + (nextBottom - bottom) * (mx - curX) / (nextX - curX);
	double ar = area(top, ttt) - area(bottom, bbb);
// 	cerr << divarea << " " << curarea << " " << ar << endl;
	if(ar < divarea - curarea){
	  lx = mx;
	}else{
	  ux = mx;
	}
      }
      

      printf("%.10f\n", lx);
//       cerr << lx << endl;
      d++;
      curarea = 0;

      top =  top + (nextTop - top) * (lx - curX) / (nextX - curX);
      bottom = bottom + (nextBottom - bottom) * (lx - curX) / (nextX - curX);
      curX = lx;
      continue;
    }
    
    curarea += a;
    curX = nextX;
    top = nextTop;
    bottom = nextBottom;
    
    if(lower[li+1].real() < upper[ui+1].real()){
      li++;
    }else if(lower[li+1].real() > upper[ui+1].real()){
      ui++;
    }else{
      li++;
      ui++;
    }

  }
//    cerr << endl << endl;;
}

/////////////////////////////////////////////////////////

int main(int argc, char* argv[]) {

  init();
  int nCases;
  cin >> nCases;
  REP(iCase, nCases) {
    cout << "Case #" << (iCase+1) << ": ";
    solve();
  }
  
  return 0;
}
