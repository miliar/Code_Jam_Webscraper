#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int T;
int N;
vector<double> x;
vector<double> y;
vector<double> z;
vector<double> vx;
vector<double> vy;
vector<double> vz;

void print(double t) {
  double sx = 0.;
  double sy = 0.;
  double sz = 0.;
  
  for (int i = 0; i < N; i++) {
    sx += (x[i] + vx[i] * t);
    sy += (y[i] + vy[i] * t);
    sz += (z[i] + vz[i] * t);
  }

  sx /= N;
  sy /= N;
  sz /= N;

  double d = sqrt(sx * sx + sy * sy + sz * sz);
  cout << d << ' ' << t;
}

void work() {
  cin >> N;
  x = vector<double>(N);
  y = vector<double>(N);
  z = vector<double>(N);
  vx = vector<double>(N);
  vy = vector<double>(N);
  vz = vector<double>(N);

  double sx = 0;
  double sy = 0;
  double sz = 0;
  double svx = 0;
  double svy = 0;
  double svz = 0;

  for (int i = 0; i < N; i++) {
    cin >> x[i] >> y[i] >> z[i];
    cin >> vx[i] >> vy[i] >> vz[i];
    
    sx += x[i];
    sy += y[i];
    sz += z[i];
    svx += vx[i];
    svy += vy[i];
    svz += vz[i];
  }

  double up = sx * svx + sy * svy + sz * svz;
  double down = svx * svx + svy * svy + svz * svz;
  if (down < 1E-6) {
    print(0.);
  } else {
    double t = - up / down;
    if (t < 0) {
      print(0.);
    } else {
      print(t);
    }
  }
}

int main() {
  cout << setiosflags(ios::fixed) << setprecision(6);
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    work();
    cout << endl;
  }
  return 0;
}
