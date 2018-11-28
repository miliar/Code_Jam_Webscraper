#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,pocz,koniec) for (int var=(pocz); var<=(koniec); ++var)
#define FORD(var,pocz,koniec) for (int var=(pocz); var>=(koniec); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

typedef long double LD;

LD sqr(LD x){
  return (LD)x*(LD)x;
}

int main(){
  int testy;
  scanf("%d",&testy);
  REP(numer,testy){
    printf("Case #%d: ", numer+1);
    int n;
    scanf("%d",&n);
    LL x = 0, y= 0, z=0, dx=0, dy=0, dz=0;
    REP(foo,n){
      int t[6];
      REP(i,6) scanf("%d",t+i);
      x+=t[0]; y+=t[1]; z+=t[2];
      dx+=t[3]; dy+=t[4]; dz+=t[5];
    }
    LL a = dx*dx + dy*dy + dz*dz;
    LL b = 2.0*(dx*x + dy*y + dz*z);
    if (a == 0){
      printf("%.6Lf %.6Lf\n",sqrtl(sqr(x/(LD)n)+sqr(y/(LD)n)+sqr(z/(LD)n)),(LD)0.0);
    } else {
      if (b > 0){
        printf("%.6Lf %.6Lf\n",sqrtl(sqr(x/(LD)n)+sqr(y/(LD)n)+sqr(z/(LD)n)),(LD)0.0);
      } else {
        LD t = (LD)-b/(LD)2.0/(LD)a;
        LD xx = x/(LD)n + (LD)dx / (LD)n * t;
        LD yy = y/(LD)n + (LD)dy / (LD)n * t;
        LD zz = z/(LD)n + (LD)dz / (LD)n * t;
        printf("%.6Lf %.6Lf\n",sqrtl(sqr(xx)+sqr(yy)+sqr(zz)),t);
      }
    }
  }
  return 0;
}
