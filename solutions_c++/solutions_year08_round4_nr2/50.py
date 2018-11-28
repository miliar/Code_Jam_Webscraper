#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
using namespace std;
#define FR(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

typedef complex<double> cpx;

const double eps = 1e-8;
const int inf = 123456789;
int cas = 0;
int N,M,A;
void doit() {
  scanf("%d%d%d",&N,&M,&A);

  printf("Case #%d: ",++cas);

  FOR(x2,N+1) FOR(y2,M+1) FR(x3,x2,N+1) FOR(y3,M+1) {
    cpx p(x2,y2), q(x3,y3);

    double a = fabs((conj(p)*q).imag());
    if (fabs(a-A) < eps) {
      printf("0 0 %d %d %d %d\n",x2,y2,x3,y3);
      goto xx;
    }
  }

  printf("IMPOSSIBLE\n");
  xx:;
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}
