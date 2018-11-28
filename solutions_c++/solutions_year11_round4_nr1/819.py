#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <algorithm>

#define D if(0)
using namespace std;

double x,s,r,t,tall;
int n;
struct Walkway {
  double b, e, w;
  double tw,tr,vw,vr,weight;
  void read() { scanf("%lf%lf%lf", &b,&e,&w);}
  bool operator<(const Walkway& rhs) const {
    return b < rhs.b;
  }
} w[100];

struct Piece {
  double b, e,w, vw, vr, t, tw, tr, weight;
  void calc() {
    vw = s+w;
    vr = r+w;
    t = tw = (e-b)/vw;
    tr = (e-b)/vr;
    weight = (tw-tr)/tr;
  }
  bool operator<(const Piece& rhs) const {
    return weight > rhs.weight;
  }
  void set(const Walkway& r) {
    b=r.b;e=r.e;w=r.w;
  }
  void run(double& run_time) {
    if (run_time >= tr) {
      // run all
      run_time -= tr;
      t = tr;
    } else {
      // run with run_time
      double d=(e-b) - vr*run_time;
      t=d/vw+run_time;
      run_time = 0;
    }
  }
} p[210];
int pc;

int main(int argc, char const* argv[])
{
  int case_count;
  scanf("%d", &case_count);
  for (int case_index = 0; case_index < case_count; case_index++) {
    printf("Case #%d: ", case_index + 1);
    scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
    for (int i = 0; i < n; i++) w[i].read();
    sort(w,w+n);

    pc=0;
    tall=0;
    double pos=0;
    for (int i = 0; i < n; i++) {
      if (pos < w[i].b) {
        p[pc].b = pos;
        p[pc].e = w[i].b;
        p[pc].w = 0;
        pc++;
      }
      p[pc].set(w[i]);
      pc++;
      pos = w[i].e;
    }
    if (pos < x) {
      p[pc].b = pos;
      p[pc].e = x;
      p[pc].w = 0;
      pc++;
    }

    D printf("\n");
    for (int i = 0; i < pc; i++) {
      p[i].calc();
 D     printf("%g - %g, weight: %.2lf\n", p[i].b, p[i].e, p[i].weight);
    }
    sort(p,p+pc);

    int i=0;
    while(t>0 && i<pc) {
      p[i].run(t);
      i++;
    }

    tall=0;
    for (int i = 0; i < pc; i++) {
      tall+=p[i].t;
    }

    printf("%.10lf\n", tall);
  }
  return 0;
}


