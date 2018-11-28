#include <cstdio>
#include <cmath>

#define MAX_N 40

int p[MAX_N][2];
int r[MAX_N];
int n;

double d(int x1, int y1, int x2, int y2)
{
  return sqrt((x1-x2)*(x1-x2) +
	      (y1-y2)*(y1-y2));
}

double dd(int i, int j)
{
  return d(p[i][0],p[i][1],
	   p[j][0],p[j][1]);
}

inline double min(double a, double b)
{
  return (a < b) ? a : b;
}

inline double max(double a, double b)
{
  return (a > b) ? a : b;
}

void read_input()
{
  scanf("%d",&n);
  for(int i=0; i<n; i++)
    scanf("%d %d %d",&p[i][0],
	  &p[i][1], &r[i]);
}

main()
{
  int c;
  scanf("%d",&c);
  for(int t=0; t<c; t++) {
    read_input();
    double rr;
    if(n==1) {
      rr = r[0];
    } else if(n==2) {
      double r1 = (dd(0,1)+r[0]+r[1])/2;
      double r2 = max(r[0],r[1]);
      rr = min(r1,r2);
    } else {
      double r1 = max((dd(0,1)+r[0]+r[1])/2,r[2]);
      double r2 = max((dd(0,2)+r[0]+r[2])/2,r[1]);
      double r3 = max((dd(2,1)+r[2]+r[1])/2,r[0]);
      rr = min(r1,min(r2,r3));
    }
    printf("Case #%d: %lf\n",t+1,rr);
  }
}
