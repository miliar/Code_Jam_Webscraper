#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

vector<double> vals;

int n;

double d;

bool possible(double move){
  double lastPos = vals[0] - move, npos;
  ffor (i, 1, n){
    if (lastPos + d < vals[i])
      npos = max(lastPos + d, vals[i] - move);
    else
      npos = min(lastPos + d, vals[i] + move);
    
    if (npos < lastPos + d - 1e-9)
      return false;
    lastPos = npos;
//    cout << "lastPos = " << lastPos << " i = " << i << endl;
  }
  
  return true;
}

int main(){
  freopen("Bs.out","wt", stdout);
  freopen("Bs.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  string str;
  int c, d, a, b;
  FOR (test, tests){
    cin >> c >> d;
    ::d = d;
    
    vals.clear();
    FOR (i, c){
      cin >> a >> b;
      FOR (j, b)
        vals.pb(a);
    }
    sort(all(vals));
    n = vals.sz;
    double s = 0.0, e = 10000000000000.0, mid;
    while (fabs(e - s) > 1e-10){
      mid = (s + e) / 2.0;
      if (possible(mid))
        e = mid;
      else
        s = mid;
    }

    cout << "Case #" << (test + 1) << ": ";
    printf("%.11lf", s);
    cout << "\n";
  }
  return 0;
}
