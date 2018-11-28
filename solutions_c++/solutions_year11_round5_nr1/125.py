#include <iostream>
#include <iomanip>
using namespace std;

int rlx[110], rly[110], rhx[110], rhy[110];
double x[210], l[210], h[210];
int W, L, U, G, N;

double getArea(double xv) {
  double res = 0;
  for (int i = 0; i < N-1; i++) {
    if (x[i+1] > xv) {
      double hv = ((x[i+1]-xv)*h[i]+(xv-x[i])*h[i+1])/(x[i+1]-x[i]);
      double lv = ((x[i+1]-xv)*l[i]+(xv-x[i])*l[i+1])/(x[i+1]-x[i]);
      res += (xv-x[i])*(hv+h[i]-lv-l[i])/2;
      break;
    }
    res += (x[i+1]-x[i])*(h[i+1]+h[i]-l[i+1]-l[i])/2;
  }
  return res;
}

double search(double area) {
  double low = 0, hi = W;
  while (hi-low > 1e-8) {
    double mid = (low+hi)/2;
    if (getArea(mid) > area) hi = mid;
    else low = mid;
  }
  return low;
}

int main() {
  cout.setf(ios::fixed);
  cout << setprecision(8);

  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    cin >> W >> L >> U >> G;
    for (int i = 0; i < L; i++) cin >> rlx[i] >> rly[i];
    for (int i = 0; i < U; i++) cin >> rhx[i] >> rhy[i];

    int ci = 0, cj = 0; N = 0;
    x[0] = 0; l[0] = rly[0]; h[0] = rhy[0];
    for (int i = 1; ci < L-1 || cj < U-1; i++) {
      if (rlx[ci+1] == rhx[cj+1]) {
        ci++; cj++;
        x[i] = rlx[ci];
        l[i] = rly[ci];
        h[i] = rhy[cj];
      } else if (rlx[ci+1] < rhx[cj+1]) {
        ci++;
        x[i] = rlx[ci];
        l[i] = rly[ci];
        h[i] = ((rhx[cj+1]-x[i])*rhy[cj]+(x[i]-rhx[cj])*rhy[cj+1])/(rhx[cj+1]-rhx[cj]);
      } else {
        cj++;
        x[i] = rhx[cj];
        l[i] = ((rlx[ci+1]-x[i])*rly[ci]+(x[i]-rlx[ci])*rly[ci+1])/(rlx[ci+1]-rlx[ci]);
        h[i] = rhy[cj];
      }
      N++;
    }
    x[N] = W; l[N] = rly[L-1]; h[N] = rhy[U-1];
    N++;

//    for (int i = 0; i < N; i++)
//      cout << "\t" << x[i] << " " << l[i] << " " << h[i] << endl;

    double total = 0;
    for (int i = 0; i < N-1; i++)
      total += (x[i+1]-x[i])*(h[i+1]+h[i]-l[i+1]-l[i])/2;

    cout << "Case #" << c << ":" << endl;
    for (int i = 0; i < G-1; i++)
      cout << search(total*(i+1)/G) << endl;
  }
  return 0;
}
