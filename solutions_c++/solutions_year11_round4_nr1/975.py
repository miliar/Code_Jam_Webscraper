#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <iostream>
#include <cstring>
#include <cctype>
#include <climits>

using namespace std;
const int maxv = 987654321;

struct Ent {
  double dif;
  double len;
  double v;
  bool operator < (const Ent& e) const {
    return dif < e.dif;
  }
  Ent (double d, double l, double v) : dif(d), len(l), v(v) {}
  Ent(){}
};

Ent dt[1000010];
int main() {
  int ca;
  scanf(" %d", &ca);
  
  for (int ii = 0; ii < ca; ii++) {
    int X, S, R, t, N;
    scanf( "%d%d%d%d%d", &X, &S, &R, &t, &N);
    

    for (int i = 0; i < N; i++) {
      int b, e, w;
      scanf(" %d%d%d", &b, &e, &w);
      X -= e - b;
      double len = e - b;
      dt[i] = Ent((double)(w + R) / (w + S), e - b, w);
    }
    
    dt[N] = Ent((double)R / S, X, 0);

    double tm = 0;
    double left = t;
    bool use = true;

    sort(dt, dt + N + 1);

    for (int i = N; i >= 0; i--) {
      //printf("tm:%f\n", tm);
      double len = dt[i].len;
      double w = dt[i].v;

	double v = len / (w + R);
	if (!use) {
	  
	  tm += len / (w + S);

	}else if (v < left) {
	  tm += v;
	  left -= v;

	} else {
	  len -= (w + R) * left;
	  tm += left;
	  tm += len / (w + S);
	  use = false;

	}

    }

    
    printf("Case #%d: ", ii + 1);
    printf("%.9f\n", tm);
      
  }
}
