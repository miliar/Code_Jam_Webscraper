#include <iostream>
#include <cstdio>
#include <cmath>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define sqr(_a) ((_a) * (_a))
#define syso system("pause")

using namespace std;

double dist(double x1, double y1, double x2, double y2){
  return sqrt(sqr(x1 - x2) + sqr(y1 - y2));
}

int main(){
  freopen("Ds.out","wt", stdout);
  freopen("Ds.in","r", stdin);
  int tests, b;
  scanf("%d\n", &tests);
  FOR (test, tests){
    double ret = -1.0;
    int n;
    scanf("%d", &n);
    int x[n], y[n], r[n];
    FOR (i, n)
      scanf("%d %d %d", &x[i], &y[i], &r[i]);
    
    if (n == 1)
      ret = r[0];
    else if (n == 2)
      ret = max(r[0], r[1]);
    else
      FOR (i, 3)
        FOR (j, 3)
          FOR (k, 3)
            if (i != j && i != k && j != k){
              double val = r[k];
              double dd = dist(x[i], y[i], x[j], y[j]);
              
              if (dd <= r[i]){
                if (dd + r[j] <= r[i])
                  val >?= r[i];
                else
                  val >?= (r[i] + dd + r[j]) / 2.0;
              } 
              else if (dd <= r[j]){
                if (dd + r[i] <= r[j])
                  val >?= r[j];
                else
                  val >?= (r[i] + dd + r[j]) / 2.0;
              }
              else
                val >?= (dd + r[i] + r[j]) / 2.0;
                
              if (ret < 0.0 || val < ret)
                ret = val;
            }
    
    printf("Case #%d: %.6lf\n", test + 1, ret);
  }
  
  return 0;
}
