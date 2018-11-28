#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>

using namespace std;

#define fo(i, n) for(int i=0; i<(n); i++)
#define ff(i, n) for(int i=1; i<=(n); i++)
#define pb push_back
#define mp make_pair
#define sz(v) int((v).size())
#define S(v) sort(v.begin(), v.end())

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

inline ll sqr(ll x) { return x*x; }
inline ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
inline ll lcm(ll x, ll y) { return x/gcd(x, y)*y; }

const double eps = 1e-11;
const ll linf = 123456789066391630LL;
const int inf = 966391630;
const int md = 100000007;
const int dx[]={-1, 0, 1, 0, -1, -1, 1, 1};
const int dy[]={0, 1, 0, -1, -1, 1, -1, 1};

int i, j, k, l, n, ntst, tall;
double x[1001], y[1001], z[1001], p[1001], xo, yo, zo, mv, nx, ny, nz, bx, by, bz, power, np, nw;

double calc(double x1, double y1, double z1)
{
    double ret=0.0, res;
   fo(i, n) {
       res=(abs(x[i]-x1)+abs(y[i]-y1)+abs(z[i]-z1))/p[i];
      if (res>ret) ret=res;
   }
      return ret;
}

int main()
{
  freopen("C-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  int dx, dy, dz;
   scanf("%d\n", &tall);
  ff(ntst, tall) {
       scanf("%d", &n);
    fo(i, n) scanf("%lf%lf%lf%lf", &x[i], &y[i], &z[i], &p[i]);
     mv=10000;
        xo=0.0; yo=0.0; zo=0.0;
       power=calc(xo, yo, zo);
   while (mv>eps) {
    while (1) {
        nw=power;
           bx=xo;
           by=yo;
           bz=zo;
      for(dx=-1; dx<2; dx++)
        for(dy=-1; dy<2; dy++)
          for(dz=-1; dz<2; dz++) {
                  nx=xo+dx*mv;
                  ny=yo+dy*mv;
                  nz=zo+dz*mv;
                np=calc(nx, ny, nz);
              if (np+eps<nw) {
                  nw=np;
                   bx=nx;
                   by=ny;
                   bz=nz;
              }
          }
       if (power-eps>nw) {
          power=nw;
            xo=bx;
            yo=by;
            zo=bz;
       } else break;
    }
         mv/=2.0;
   }
     printf("Case #%d: %.6lf\n", ntst, power);
  }
      return 0;
} 
