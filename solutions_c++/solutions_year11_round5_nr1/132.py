#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;

#define mineps 1e-8
#define psb push_back

inline int cmp(double x) {
  if (fabs(x) < mineps) return 0;
  else if (x < 0) return -1;
  else return 1;
}

class coor {
public:
       double x, y;
       coor() {}
       coor(double dx, double dy) {x=dx, y=dy; }      
};

vector<coor> lower, upper;
int nl, nu, T, G;
double W;
vector<double> ans;
double area, exparea;

double subcalc(vector<coor> &a, double x1, double x2) {

  double ret = 0;
  for(int i = 0; i < a.size()-1; i++) {
    coor &v1 = a[i], &v2 = a[i+1];
    if (fabs(v1.x - v2.x) == 0) continue;
    if (x1 <= v1.x && v2.x <= x2)
      ret += 0.5 * (v1.y + v2.y) * (v2.x - v1.x);
    else if (x1 <= v1.x && v1.x <= x2 && x2 <= v2.x) {
      double yy = v1.y + (x2-v1.x)/(v2.x-v1.x) * (v2.y-v1.y);
      ret += 0.5 * (v1.y + yy) * (x2 - v1.x);
    }
    else if (v1.x <= x1 && x1 <= v2.x && v2.x <= x2) {
      double yy = v1.y + (x1-v1.x)/(v2.x-v1.x) * (v2.y-v1.y);
      ret += 0.5 * (yy + v2.y) * (v2.x - x1);     
    }
    else if (v1.x <= x1 && x2 <= v2.x) {
      double yy1 = v1.y + (x1-v1.x)/(v2.x-v1.x) * (v2.y-v1.y);
      double yy2 = v1.y + (x2-v1.x)/(v2.x-v1.x) * (v2.y-v1.y);
      ret += 0.5 * (yy1 + yy2) * (x2 - x1);     
    }
                 
  }
  
  return ret;
       
}

double calcarea(double x1, double x2) {
       
  double a1 = subcalc(upper, x1, x2);
  double a2 = subcalc(lower, x1, x2);
  return a1 - a2; 
       
}

double find_next_cut(double lasty) {
       
  double lft = lasty, rft = W;
  for(int i = 0; i < 100; i++) {
    double mid = (lft + rft) * 0.5;
    double thisarea = calcarea(lasty, mid);
    if (thisarea < exparea) lft = mid; else rft = mid;        
  }
  return (lft + rft) * 0.5;
  
}

int main() {
    
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);
  
  scanf("%d", &T);
  for(int ctn = 1; ctn <= T; ctn ++) {
          
    scanf("%lf%d%d%d", &W, &nl, &nu, &G);
    lower.clear(); upper.clear(); 
    for(int i = 0; i < nl; i++) {
      int tx, ty; scanf("%d%d", &tx, &ty);
      lower.psb(coor(tx, ty));        
    }     
    for(int i = 0; i < nu; i++) {
      int tx, ty; scanf("%d%d", &tx, &ty);
      upper.psb(coor(tx, ty));        
    }
    
    ans.clear();
    area = calcarea(0, W);
    exparea = area / G;
    ans.psb(0);
    for(int i = 1; i < G; i++) {
      double nextcut = find_next_cut(ans[ans.size()-1]);
      ans.psb(nextcut);        
    }
    
    printf("Case #%d:\n", ctn);
    for(int i = 1; i < ans.size(); i++) 
      printf("%0.7lf\n", ans[i]);
          
  }    
  
  return 0;
    
}
