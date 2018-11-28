#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>

using namespace std;

//===================================================
class Solver {
  bool debug;

  int N, W, L;
  vector<int> arms;
  vector<double> x, y;
  vector<double> xF, yF;

public:

  Solver():debug(false) {
    cin >> N >> W >> L;

    arms.resize(N);
    for (int i = 0; i < N; ++i)
      cin >> arms[i];

    x.resize(N); y.resize(N);
    xF.resize(N); yF.resize(N);
  }

  void go() {
    int i, j;
    for (i = 0; i < N; ++i) {
      x[i] = (rand()/(double)RAND_MAX)*W;
      y[i] = (rand()/(double)RAND_MAX)*L;
    }

    bool good;
    do {
      good = true;

      if (debug) {
	for (int i = 0; i < N; ++i)
	  cerr << " " << x[i] << " " << y[i];
	cerr << "\n";
      }

      for (i = 0; i < N; ++i) xF[i] = yF[i] = 0.0;
      
      for (i = 0; i < N; ++i)
	for (j = i; ++j < N; ) {
	  double dx = x[j] - x[i], dy = y[j] - y[i];
	  if (dx==0.0) dx = 0.01;
	  if (dy==0.0) dy = 0.01;
	  double dist = hypot(dx, dy), minDist = arms[i]+arms[j];
	  if (dist < minDist - 0.0001) {
	    good = false;
	    // dx *= minDist - dist;
	    // dy *= minDist - dist;
	    xF[i] += -dx; yF[i] += -dy;
	    xF[j] += dx; yF[j] += dy;
	  }
	}
      
      if (!good) {
	double a = 0.01;
	for (i = 0; i < N; ++i) {
	  x[i] += a*xF[i];
	  if (x[i] < 0.0) x[i] = 0.0;
	  if (x[i] > W) x[i] = W;
	  y[i] += a*yF[i];
	  if (y[i] < 0.0) y[i] = 0.0;
	  if (y[i] > L) y[i] = L;
	}
      }

    } while (!good);

    for (int i = 0; i < N; ++i)
      cout << " " << fixed << x[i] << " " << fixed << y[i];
  }

};
//===================================================

int main(void) {
  int iTest, nTests; cin >> nTests;

  for (iTest = 1; iTest <= nTests; ++iTest) {
    cerr << iTest << "/" << nTests << "\n";

    Solver solver;

    cout << "Case #" << iTest << ":";

    solver.go();

    cout << "\n";
  }

  return 0;
}
