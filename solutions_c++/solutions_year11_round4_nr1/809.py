#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;

struct ww {
  long long B;
  long long E;
  long long w;
  long long L;

  bool operator<(const ww &rhs) const {
    return w < rhs.w;
  }
};

int main(int argc, char *argv[]) {
  if(argc < 3)
    return 0;

  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  int T;
  ifs >> T;
  for(int t=1;t<=T;t++){
    ofs << "Case #" << t << ": ";

    long long X, S, R, t, N;
    ifs >> X;
    ifs >> S;
    ifs >> R;
    ifs >> t;
    ifs >> N;

    ww *wa = new ww[N];
    double *tt = new double[N];

    long long L0 = X;
    double t_remain = (double)t;
    for(int n=0;n<N;n++) {
      ifs >> wa[n].B;
      ifs >> wa[n].E;
      ifs >> wa[n].w;
      wa[n].L = wa[n].E - wa[n].B;

      L0 -= wa[n].L;
    }

    sort(wa, wa + N);

    double t0;
    double dt = ((double)L0) / R;
    if(dt > t) {
      t_remain = 0;
      t0 = t + (((double)L0) - R * t) / S;
    }
    else {
      t0 = dt;
      t_remain = ((double)t) - dt;
    }

    for(int n=0;n<N;n++) {
      double dt = ((double)wa[n].L) / (R + wa[n].w);
      if(dt > t_remain) {
	tt[n] = t_remain + (((double)wa[n].L) - (R + wa[n].w) * t_remain) / (S + wa[n].w);
	t_remain = 0;
      }
      else {
	tt[n] = dt;
	t_remain -= dt;
      }
      t0 += tt[n];
    }

    ofs << fixed << setprecision(7) <<  t0;

    delete []tt;
    delete []wa;

    ofs << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}
