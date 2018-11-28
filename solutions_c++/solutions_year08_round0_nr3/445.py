#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <queue>
#include <set>
#include <math.h>
using namespace std;

const int dx = 10000000;

int main() {
  int N;
  scanf("%d", &N);
  for (int iii = 0; iii < N; iii++) {
    double f, R, t, r, g;
    scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
    //printf("%f\n", r);
    if (g <= f*2) {
      printf("Case #%d: %f\n", iii+1, 1.0);
      continue;
    }
    //sekibun
    double my_r = R - t - f;
    double ans = 0;
    
    for (int i = 0; i < dx; i++) {
      //dx ha my_r/dx
      double x = i*my_r/dx;
      
      int bar = (int)(x / (r+g+r));
      double tmp = x - (r+g+r)*bar;
      if (r+f < tmp && tmp < g+r-f) {
        double y = sqrt(my_r*my_r - x*x);
        
        int foo = (int)(y / (r+g+r));
        ans += (g-f*2) * foo;
        
        double tmp2 = (y - foo*(r+g+r)) - r - f;
        if (tmp2 > g-f*2) {
          tmp2 = g-f*2;
        }
        if (tmp2 < 0) {
          tmp2 = 0;
        }
        ans += tmp2;
      }
    }
    ans = 4 * ans * my_r / dx;
    double area = 3.1415926535 * R * R;
    //printf("Case #%d: %f %f %f\n", iii+1, ans, area, 1.0 - (ans / area));
    printf("Case #%d: %f\n", iii + 1, 1.0 - (ans / area));
  }
}
