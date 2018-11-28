#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

/*struct runtype {
  double speed;
  int no;
  runtype() {}
  runtype(double x, int y) {speed = x, no = y; }
  friend bool operator< (runtype a, runtype b) {
    return a.speed > b.speed;       
  }
};*/

struct runtype {
  double t1, t2, len, w;
  runtype() {}
  runtype(double x, double y, double z, double t) {t1 = x, t2 = y, len = z, w = t; }
  friend bool operator< (runtype a, runtype b) {
    return (a.t1-a.t2)/a.t2 > (b.t1-b.t2)/b.t2;       
  }       
};

#define maxn 1010
#define psb push_back

int T, n;
double X, S, R, t;
vector<runtype> leng;
double ans;

int main() {
    
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    scanf("%lf%lf%lf%lf%d", &X, &S, &R, &t, &n);
    leng.clear();
    double tmp = 0;
    for(int i = 0; i < n; i++) {
      double t1, t2, w; scanf("%lf%lf%lf", &t1, &t2, &w);
     // printf("t1 = %lf, t2 = %lf, w = %lf\n", t1, t2, w);
      double tleng = t2 - t1;
      tmp += tleng;
      
      leng.psb(runtype(tleng / (S + w), tleng / (R + w), tleng, w));
    }
    if (tmp < X) {
      double tleng = X - tmp;
      leng.psb(runtype(tleng / S, tleng / R, tleng, 0));        
    }
    
    
  /*  for(int i = 0; i < leng.size(); i++)
      printf("%lf, %lf, %lf, %lf\n", leng[i].t1, leng[i].t2, leng[i].len, leng[i].w);    */
    
    sort(leng.begin(), leng.end());

    
    ans = 0;
    double runt = 0;
    for(int i = 0; i < leng.size(); i++) {
      if (runt + leng[i].t2 < t) {
        runt += leng[i].t2;
        ans += leng[i].t2;         
      }        
      else if (runt < t) {
        double tt = t - runt;
        ans += tt + (leng[i].len - tt * (R + leng[i].w)) / (S + leng[i].w);
        runt = t;    
      }
      else ans += leng[i].t1;
    }
    
    printf("Case #%d: %0.8lf\n", ctn, ans);
            
  }
  
  return 0;
    
}
