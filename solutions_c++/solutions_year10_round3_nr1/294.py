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

typedef vector<int> vi;

int main () {
  int test, T;

  cin >> T;
  int a,b;
  int n;
  int i,j;
  REP (test, T) {
    vi av;
    vi bv;
    //TODO
    int r = 0;
    cin >> n;
    REP (i,n) {
      cin >> a >> b;
      av.push_back(a);
      bv.push_back(b);
    }
    REP (i,n) {
      int ta = av[i];
      int tb = bv[i];
      REP(j,i) {
        int oa = av[j];
        int ob = bv[j];
        //printf("dif1=%d dif2=%d\n", ta-oa, tb-ob);
        if ((ta-oa)*(tb-ob)<0) {
          //intersect
          r++;
        }
      }
    }
    gp(r);
  }
  return 0;
}

