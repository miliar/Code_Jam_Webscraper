#include <cstdlib>
#include <cstdio>
#include <cassert>
#include <cmath>

FILE* input;
FILE* output;


void solveone(int tc) {
  int n;
  long long x[1000];
  long long y[1000];
  long long z[1000];
  long long vx[1000];
  long long vy[1000];
  long long vz[1000];

  fscanf(input, "%d\n", &n);

//  fprintf(stderr, "\n\n");
  for (int i = 0; i < n; ++i) {
    int a,b,c,d,e,f;
    fscanf(input, "%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
    x[i] = a;
    y[i] = b;
    z[i] = c;
    vx[i] = d;
    vy[i] = e;
    vz[i] = f;
//    fprintf(stderr, "%d %d %d %d %d %d\n", a,b,c,d,e,f);
  }

  double xx0 = 0;
  double yy0 = 0;
  double zz0 = 0;
  double vxx = 0;
  double vyy = 0;
  double vzz = 0;
  
  for (int i = 0; i < n; ++i) {
    xx0 += x[i];
    yy0 += y[i];
    zz0 += z[i];
    vxx += vx[i];
    vyy += vy[i];
    vzz += vz[i];
  }

//  fprintf(stderr, "vxx=%f, vyy=%f, vzz=%f\n", vxx, vyy, vzz);
  
  double tmin = vxx*vxx + vyy*vyy + vzz*vzz != 0 ? -(xx0*vxx + yy0*vyy + zz0*vzz)/((double)(vxx*vxx + vyy*vyy + vzz*vzz)) : 0.0;
  if (tmin < 0.0) {
    tmin = 0.0;
  }
  
  double dmin = sqrt((xx0 + tmin*vxx)*(xx0 + tmin*vxx) + (yy0 + tmin*vyy)*(yy0 + tmin*vyy) + (zz0 + tmin*vzz)*(zz0 + tmin*vzz))/((double)n);
  if (dmin <= 0.0) {
    dmin = 0.0;
  }
  fprintf(output, "Case #%d: %.8f %.8f\n", tc, dmin, tmin);
}

void solve() {
  int n;
  fscanf(input, "%d\n", &n);
  for (int i = 0; i < n; ++i) {
    solveone(i+1);
  }
}

int main(int argc, char** argv) {
  if (argc >= 2 ) {
    input = fopen(argv[1], "r");
    if (input == NULL) {
      fprintf(stderr, "could not open input file\n");
      exit(1);
    }
  }
  else {
    input = stdin;
  }
  
  if (argc >= 3) {
    output = fopen(argv[2], "w");
    if (output == NULL) {
      fprintf(stderr, "could not open output file\n");
      exit(2);
    }
  }
  else {
    output = stdout;
  }

  solve();
}
