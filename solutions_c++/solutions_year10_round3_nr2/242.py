#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <math.h>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef deque<string> DS;
typedef unsigned long long ull;

DS split( string s, string c )
{
  DS ret;
  for (int i=0, n; i <= s.length(); i=n+1 ) {
    n = s.find_first_of( c, i );
    if( n == string::npos ) n = s.length();
    string tmp = s.substr( i, n-i );
    ret.push_back(tmp);
  }
  return ret;
}

double logn(int base, double antilog) {
    return log(antilog) / log((double)base);
}

int logint(ull base, ull p, ull l) {
  int count = 0;
  while(l<p) {
    l*=base;
    //cout << l << "<=>" << p << endl;
    count++;
  }
  return count;
}

int main () {
  int test, T;

  cin >> T;
  ull L,P,C;
  REP (test, T) {
    //TODO
    cin >> L >> P >> C;
    int r = 0;
    //double dif = logn(C, P) - logn(C, L);
    //cout << "logdifduble:" << dif << endl;
    //int difn = (int)ceil(dif);
    int difn = logint(C,P,L);
    //cout << "logdif:" << difn << endl;
    double rd = logn(2, difn);
    r = (int)ceil(rd);
    gp(r);
  }
  return 0;
}

