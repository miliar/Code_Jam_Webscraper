
// NigelTufnel, start 22:12, end 00:34

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

static char *sep = " \r\n\t";

void chomp(char *s) {
  while(strlen(s)>0 && s[strlen(s)-1] < 32)
    s[strlen(s)-1] = 0;
}

int inside(const double x, const double y, const double r) {
  return (x*x + y*y <= r*r);
}

// area of intersection of rectangle (x1,y1)-(x2,y2)
// covered by origin-centered circle of radius r.
double warea(double x1, double y1, double x2, double y2, double r, double minarea) {

  int p[3],s;
  double x3,y3,t,a,da=0.0;

  a = (x2-x1) * (y2-y1);

  p[0] = inside(x1,y1,r);
  p[1] = inside(x2,y1,r);
  p[2] = inside(x1,y2,r);
  p[3] = inside(x2,y2,r);

  if (p[0] && p[1] && p[2] && p[3])     return ( a );
  if (!p[0] && !p[1] && !p[2] && !p[3]) return ( 0.0 );

  if (a < minarea) {
    s = p[0] + p[1] + p[2] + p[3];
    if (s==4) 
      return a;
    else if (s==3) 
      return a/2.0;
    else
      return 0.0;
  }

  if (!p[1]) {
    x2 = sqrt(r*r - y1*y1);
    p[1] = inside(x2,y1,r);
    p[3] = inside(x2,y2,r);
  }

  if (!p[2]) {
    y2 = sqrt(r*r - x1*x1);
    p[2] = inside(x1,y2,r);
    p[3] = inside(x2,y2,r);
  }
  if (p[1] && !p[3]) {
    t = sqrt(r*r - x2*x2);
    da = (x2-x1) * (t-y1);
    y1 = t;
    p[0] = inside(x1,y1,r);
    p[1] = inside(x2,y1,r);
  }
  if (p[2] && !p[3]) {
    t = sqrt(r*r - y2*y2);
    da += (t-x1) * (y2-y1);
    x1 = t;
    // p0/p2
  }

  x3 = (x1 + x2) / 2.0;
  y3 = (y1 + y2) / 2.0;
  return(da+
	 warea(x1,y1,x3,y3,r,minarea) +
	 warea(x1,y3,x3,y2,r,minarea) +
	 warea(x3,y1,x2,y3,r,minarea) +
	 warea(x3,y3,x2,y2,r,minarea));

}

double solve() {
  char line[512],*p;
  double f,R,t,r,g;

  fgets(line,512,stdin);
  chomp(line);

  p = strtok(line,sep); f = atof(p);
  p = strtok(NULL,sep); R = atof(p);
  p = strtok(NULL,sep); t = atof(p);
  p = strtok(NULL,sep); r = atof(p);
  p = strtok(NULL,sep); g = atof(p);

  if (2.0 * f >= g) return 1.0;

  double qtot, pt, qp=0.0, x1,y1,x2,y2,ma;
  int mt,i,j,a=0,b=0;

  qtot = (M_PI * R * R) / 4.0;
  pt = (g-2.0*f) * (g-2.0*f);
  mt = (int) ceil( (R-t) / (g + 2.0*r) );

  ma = qtot / 1.0e13;

  for(j=0;j<mt;j++)
    for(i=0;i<mt;i++) {
      x1 = r + i*(g+2.0*r);
      y1 = r + j*(g+2.0*r);
      x2 = x1 + g;
      y2 = y1 + g;

      if (inside(x1,y1,R-t) &&
	  inside(x1,y2,R-t) &&
	  inside(x2,y1,R-t) &&
	  inside(x2,y2,R-t)) {
	qp += pt;
	a++;
      } else {
	qp += warea(x1+f,y1+f,x2-f,y2-f,R-t-f,ma);
	b++;
      }	
    }

  if (qp > qtot) qp = qtot;
  //  printf("a=%d b=%d\n",a,b);
  return(1.0 - (qp/qtot));
}

int main(int argc, char **argv) {

  char line[512];
  int i,n;
  double x;

  fgets(line,512,stdin); chomp(line); n=atoi(line);

  for(i=0;i<n;i++) {
    x = solve();
    printf("Case #%d: %.6f\n",i+1,x);
  }

  return 0;
}
