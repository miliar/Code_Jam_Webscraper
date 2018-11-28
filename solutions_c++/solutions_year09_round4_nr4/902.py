#include <cstdio>
#include <cmath>

int main () {
  int c;
  scanf ("%d", &c);
  for (int i = 0; i < c; i ++) {
    int n;
    scanf ("%d", &n);
    double minr = 0, minr1 = 0;
      
    int x[4], y[4], r[4];
      
    for (int j = 0; j < n; j ++) 
      scanf ("%d%d%d", &x[j + 1], &y[j + 1], &r[j + 1]);
    switch (n) {
    case 3:
      minr = r[1];
      if ((sqrt ((x[2] - x[3]) * (x[2] - x[3]) + (y[2] - y[3]) * (y[2] - y[3])) + r[2] + r[3]) / 2 > minr)  minr = (sqrt ((x[2] - x[3]) * (x[2] - x[3]) + (y[2] - y[3]) * (y[2] - y[3])) + r[2] + r[3]) / 2;
      minr1 = r[2];
      if ((sqrt ((x[1] - x[3]) * (x[1] - x[3]) + (y[1] - y[3]) * (y[1] - y[3])) + r[1] + r[3]) / 2 > minr1)  minr1 = (sqrt ((x[1] - x[3]) * (x[1] - x[3]) + (y[1] - y[3]) * (y[1] - y[3])) + r[1] + r[3])/2;
      if (minr1 < minr) minr = minr1;
      minr1 = r[3];
      if ((sqrt ((x[1] - x[2]) * (x[1] - x[2]) + (y[1] - y[2]) * (y[1] - y[2])) + r[1] + r[2])/2 > minr1)  minr1 = (sqrt ((x[1] - x[2]) * (x[1] - x[2]) + (y[1] - y[2]) * (y[1] - y[2])) + r[1] + r[2])/2;
      if (minr1 < minr) minr = minr1;
     break;
    case 2:
      minr = r[1];
      if (r[2] > minr ) minr = r[2];
      break;
    case 1:
      minr = r[1];
      break;
    }
    printf ("Case #%d: %.6f\n", i + 1, minr);
  }
  return 0;
}
      
     
      
	
      
      