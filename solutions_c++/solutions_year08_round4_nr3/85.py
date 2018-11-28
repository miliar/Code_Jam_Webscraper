#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

double x[9999], y[9999], z[9999], p[9999];
double best;
int nr, n;

bool improve(double xp, double yp, double zp){
       double Max = 0;
       for (int i=0; i<n; i++){
           double dist = abs(x[i] - xp) + abs(y[i] - yp) + abs(z[i] - zp);
           dist /= p[i];
           Max = max(Max, dist);
       }
       if (Max < best){
          best = Max;
          return true;
       }
       return false;
}

void solve(){
     scanf("%d", &n);
     double xp=0, yp=0, zp=0;
     for (int i=0; i<n; i++){
         scanf("%lf %lf %lf %lf", x+i, y+i, z+i, p+i);
         xp += x[i]/n;
         yp += y[i]/n;
         zp += z[i]/n;
     }
     double genBest = 1e9;
     for (int i=0; i<=n; i++){
         fprintf(stderr, "%d %d\n", nr, i);
          best = 1e8;
          for (double pas = 1e6; pas > 1e-9; pas*=0.8){
              if (improve(xp+pas, yp, zp)) xp += pas;
              if (improve(xp-pas, yp, zp)) xp -= pas;
              if (improve(xp, yp+pas, zp)) yp += pas;
              if (improve(xp, yp-pas, zp)) yp -= pas;
              if (improve(xp, yp, zp+pas)) zp += pas;
              if (improve(xp, yp, zp-pas)) zp -= pas;                                             
          }
//          printf("%d\n")
          if (best < genBest) genBest = best;
          xp = x[i];
          yp = y[i];
          zp = z[i];
     }
     nr++;
     printf("Case #%d: %f\n", nr, genBest);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
