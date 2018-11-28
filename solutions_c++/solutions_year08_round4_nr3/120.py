#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int INF = 1<<30;                
const double EPS = 1e-9;
const double PI = acos(-1.0);

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
typedef long double LD;

#define ALL(a) a.begin(),a.end()
#define PB push_back
#define MP make_pair
#define SZ(a) (int)a.size()
#define CLR(a,v) memset((a),(v),sizeof(a))
#define FOR(i,a,n) for(int i=(a);i<(n);++i)
#define FORD(i,a,n) for(int i=(a);i>=(n);--i)
#define REP(i,n) FOR(i,0,n) 



/// CODE HERE
const int N = 1005;
const int IT = 100;

int x[N];
int y[N];
int z[N];
int p[N];
int n;

inline double S(double x) { return x*x; }

double calc3(double X, double Y, double Z) {
  double ret = 0.0;
  REP(i,n) {
    //double add = abs(X-x[i]);
    //add += abs(Y-y[i]);
    //add += abs(Z-z[i]);
    //ret += add/p[i];
    //double add = S(X-x[i])+S(Y-y[i])+S(Z-z[i]);
    double add = abs(x[i]-X)+abs(y[i]-Y)+abs(z[i]-Z);
    ret = max(ret, add/p[i]);
  }
  return ret;
}

double calc2(double X, double Y, double& Z) {
  double l = 0.0, r = 1e7;
  REP(it,IT) {
    double m1 = (2*l+r)/3;
    double m2 = (l+2*r)/3;
    if (calc3(X, Y, m1) < calc3(X, Y, m2)) r = m2;
    else l = m1;
  }
  Z = (l+r)/2;
  return calc3(X, Y, Z);
}

double calc1(double X, double& Y, double& Z) {
  double l = 0.0, r = 1e7;
  REP(it,IT) {
    double m1 = (2*l+r)/3;
    double m2 = (l+2*r)/3;
    if (calc2(X, m1, Z) < calc2(X, m2, Z)) r = m2;
    else l = m1;
  }
  Y = (l+r)/2;
  return calc2(X, Y, Z);
}

double calc(double& X, double& Y, double& Z) {
  double l = 0.0, r = 1e7;
  REP(it,IT) {
    double m1 = (2*l+r)/3;
    double m2 = (l+2*r)/3;
    if (calc1(m1, Y, Z) < calc1(m2, Y, Z)) r = m2;
    else l = m1;
  }
  X = (l+r)/2;
  return calc1(X, Y, Z);
}

int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);

  int T;
  scanf("%d", &T);

  FOR(NT,1,T+1) {
    scanf("%d", &n);
    REP(i,n) scanf("%d %d %d %d", x+i,y+i,z+i,p+i);

    double X, Y, Z;
    calc(X, Y, Z);
    double ans = 0.0;
    REP(i,n) {
      double add = abs(x[i]-X)+abs(y[i]-Y)+abs(z[i]-Z);
      ans = max(ans, add/p[i]);
    }
    printf("Case #%d: %.6f\n", NT, ans);

    
  }


  return 0;
}