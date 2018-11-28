#include <cstdio>
#include <cmath>

typedef long double DOUBLE;

const DOUBLE EPS=4e-14;

DOUBLE A, R2;

int inside(DOUBLE x, DOUBLE y);
DOUBLE recurse(DOUBLE x, DOUBLE y, DOUBLE r);

int main() {
  int t, T, x, y;
  DOUBLE f, R, w, r, g, q, Q, z1, z2, cx, cy;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    scanf("%Lf %Lf %Lf %Lf %Lf", &f, &R, &w, &r, &g);
    q=0;
    Q=A=M_PI*R*R;
    R-=w+f;
    R2=R*R;
    r*=2;
    r+=2*f;
    g-=2*f;
    z1=(r+g)/2;
    z2=g/2;
    if (R>0 && g>0)
      for (x=(-1003); x<=1003; x+=2)
	for (y=(-1003); y<=1003; y+=2) {
	  cx=z1*x;
	  cy=z1*y;
	  q+=recurse(cx, cy, z2);
	}
    printf("Case #%d: %.9Lf\n", t, 1-q/Q);
    fprintf(stderr, "Case #%d: %.9Lf\n", t, 1-q/Q);
    fflush(stderr);
  }
  return 0;
}

int inside(DOUBLE x, DOUBLE y) {
  return x*x+y*y<=R2;
}

DOUBLE recurse(DOUBLE x, DOUBLE y, DOUBLE r) {
  DOUBLE a=4*r*r;
  if (a/::A<EPS)
    return 0;
  int i=0, I=0;
  DOUBLE A=0;
  DOUBLE xs[4], ys[4];
  for (int dx=(-1); dx<=(+1); dx+=2)
    for (int dy=(-1); dy<=(+1); dy+=2) {
      xs[i]=x+dx*r;
      ys[i]=y+dy*r;
      I+=inside(xs[i], ys[i]);
      i++;
    }
  if (I==0)
    return 0;
  if (I==4)
    return a;
  for (i=0; i<4; i++)
    A+=recurse((x+xs[i])/2, (y+ys[i])/2, r/2);
  return A;
}
