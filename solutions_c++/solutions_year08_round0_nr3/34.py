
#include <algorithm>
#include <cmath>
#include <fstream>
#include <iostream>

using namespace std;

const double PI = 3.141592653589793238;

// get slice (1D)
inline double calcint(double r, double x) {
  if (x > r) x = r;
  if (x < 0) x = 0;
  return 0.5 * ( atan(x / sqrt(r*r - x*x))*r*r + x*sqrt(r*r - x*x) );
}

// get sector (2D)
inline double calc2(double r, double x, double y) {
  if (x*x+y*y > r*r) return 0;
  return PI*r*r/4 - calcint(r, x) - calcint(r, y) + x*y;
}

// get square (check all cases with overlap, etc)
inline double calc3(double r, double x1, double y1, double x2, double y2) {
  return calc2(r, x1, y1) + calc2(r, x2, y2) - calc2(r, x1, y2) - calc2(r, x2, y1);  
}

double calcAll(double f, double R, double t, double r, double g) {
  double radius = R-t-f;
  if (radius <= r+f || g <= 2*f) return 1.0;

  double total = 0;
  for (double x = r+f; x < radius; x += g+2*r)
    for (double y = r+f; y < radius; y += g+2*r)
      total += calc3(radius, x, y, x-2*f+g, y-2*f+g);
  
  return 1.0 - total*4/PI/R/R;
}

int main()  {
  ifstream fin("C-large.in");
  FILE *fout = fopen("C-large.out", "w");
  
  int N; fin >> N; cout << N << endl;
  
  for (int p = 1; p <= N; p++) {
    double f, R, t, r, g; fin >> f >> R >> t >> r >> g;
    fprintf(fout, "Case #%d: %.6lf\n", p, calcAll(f, R, t, r, g));
  }
  
  fin.close();
  
  system("pause");
  
  return 0;
}
