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

#define M 100003;
ull combi (int a, int b) {
  ull l=1;
  int i;
  REP(i,b) {
    //l=(l*(a-i)) % M;
    l=(l*(a-i));
    //cout << "*" << (a-i) << endl;
  }
  REP(i,b+1) {
    if (i<2) continue;
    l=l/i;
    //cout << "/" << i << endl;
  }
  return l;
}

ull solve (int n, int m) {
  //nをm番目に配置した場合の、subset数を返す。
  //cout << "##try### solve:" << n << ":" << m << endl;
  ull c=0;
  if (m == 1) {
    c=1;
  } else {
    int i=0;
    int mini = max(2*m-n, 1);
    for (i=mini; i<=m-1; i++) {
      //mをiに配置する
      ull r = combi(n-m-1, m-i-1);
      //printf("multiple combi(%d,%d)=%llu\n", n-m-1, m-i-1, r);
      c += r*solve(m,i) % M;
    }
  }
  //cout << "#solve:" << n << ":" << m << endl;
  //cout << "#return:" << c << endl;
  return c;
}

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    //TODO
    int n;
    cin >> n;
    int i;
    ull c=0;
    for (i=1;i<=n-1;i++) {
      c+=solve(n,i);
    }
    c = c % M;
    gp(c);
  }
  return 0;
}

