#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const double error=1e-8;

struct point {
  double x,y;
};

struct circle {
  point o;
  double r;
};

struct rec {
  bool a[50];
};

int n,np,C;
rec re[5000];
point p[5000];
circle cir[50];
int ip[5000];

bool operator < (rec a,rec b) {
  for (int i=1;i<=n;i++) {
    if (a.a[i] && (!b.a[i])) return true;
    if ((!a.a[i]) && b.a[i]) return false;
  }
  return false;
}

bool operator != (rec a,rec b) {
  return (a<b) || (b<a);
}

double sqr(double x) {
  return x*x;
}

double dist(point a,point b) {
  return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}

bool merge(int k1,int k2) {
  for (int i=1;i<=n;i++) {
    if (!(re[k1].a[i] || re[k2].a[i])) return false;
  }
  return true;
}

int ccc(point p1,double r1,point p2,double r2,point &cp1,point &cp2) {
  double mx=p2.x-p1.x,sx=p2.x+p1.x,mx2=mx*mx;
  double my=p2.y-p1.y,sy=p2.y+p1.y,my2=my*my;
  double sq=mx2+my2,d=-(sq-sqr(r1-r2))*(sq-sqr(r1+r2));
  if (d+error<0) return 0;
  if (d<error) d=0; else d=sqrt(d);
  double x=mx*((r1+r2)*(r1-r2)+mx*sx)+sx*my2;
  double y=my*((r1+r2)*(r1-r2)+my*sy)+sy*mx2;
  double dx=mx*d,dy=my*d;sq*=2;
  cp1.x=(x-dy)/sq;cp1.y=(y+dx)/sq;
  cp2.x=(x+dy)/sq;cp2.y=(y-dx)/sq;
  if (d>error) return 2; else return 1;
}

bool check(double r) {
  np=0;
  for (int i=1;i<=n;i++)
    if (r-cir[i].r<0) return false; else p[++np]=cir[i].o;
  point p1,p2;
  for (int i=1;i<=n;i++) 
    for (int j=i+1;j<=n;j++) {
      int tmp=ccc(cir[i].o,r-cir[i].r,cir[j].o,r-cir[j].r,p1,p2);
      if (tmp>=1) p[++np]=p1;
      if (tmp>=2) p[++np]=p2;
    }
  memset(re,0,sizeof(re));
  for (int i=1;i<=np;i++) {
    for (int j=1;j<=n;j++) {
      if (dist(p[i],cir[j].o)<r-cir[j].r+error) {
	re[i].a[j]=true;
      }
    }
  }

  for (int i=1;i<=np;i++) ip[i]=i;
  sort(ip+1,ip+np+1);
  int bp=np;np=1;
  for (int i=2;i<=bp;i++)
    if (re[ip[i]]!=re[ip[np]]) ip[++np]=ip[i];
  for (int i=1;i<=np;i++) {
    for (int j=i;j<=np;j++) {
      if (merge(ip[i],ip[j])) return true;
    }
  }
  return false;
}

int main() {
  scanf("%d",&C);
  for (int c=1;c<=C;c++) {
    scanf("%d",&n);
    for (int i=1;i<=n;i++) scanf("%lf%lf%lf",&cir[i].o.x,&cir[i].o.y,&cir[i].r);
    double l=0,r=10000;
    while (l+error<r) {
      double mid=(l+r)/2;
      if (check(mid)) r=mid; else l=mid;
    }
    printf("Case #%d: %0.6lf\n",c,l);
  }
}
