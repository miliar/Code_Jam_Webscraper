
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

double proba(double f, double R, double t, double r, double g) {
  double S = 0;
  double R2max = (R - f - t)*(R - f - t);
  if(2*f > g) return 1.;

  for(int x = 0; x * (g + 2*r) < R; x++)
    for(int y = 0; y * (g + 2*r) < R; y++) {
      double Xmin = x*(g+2*r) + r + f;
      double Ymin = y*(g+2*r) + r + f;
      double Xmax = (x+1)*(g+2*r) - r - f;
      double Ymax = (y+1)*(g+2*r) - r - f;

      if(Xmin*Xmin + Ymin*Ymin > R2max) continue;
      if(Xmax*Xmax + Ymax*Ymax < R2max) {
        S += (g - 2*f)*(g -2*f);
        continue;
      }
      double l = (g - 2*f)/5000.;
      Xmin += l/2;
      Ymin += l/2;      
      int nb = 0;
      for(int dx = 0; dx < 5000; dx++)
        for(int dy = 0; dy < 5000; dy++)
          if ((Xmin+dx*l)*(Xmin+dx*l) + (Ymin+dy*l)*(Ymin+dy*l) < R2max)
            nb++;
      S += l*l*nb;

    }

    double ret = 1 - (4 * S / (3.1415926535897932384626433 * R * R));
    if( ret > 1) ret = 1;
    if(ret < 0) ret = 0;
    return ret;

}

int main() {
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    double f, R, t, r, g;
    cin >> f >> R >> t >> r >> g;
    cout << "Case #" << i << ": " << proba(f, R, t, r, g) << endl;
  }
}
