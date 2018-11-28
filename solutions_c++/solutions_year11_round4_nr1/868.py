#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
#define eps 1e-8
struct node {
  int l, v;
};
struct tri {
  int a,b,c;
  bool operator< (const tri& e) const {
    if(a == e.a) return b < e.b;
    return b < e.b;
  }
};
int x, s, r, t, n;
double w;
bool operator< (const node&a, const node& b) {
  return 1.0/a.v-1.0/(a.v+w) > 1.0/b.v-1.0/(b.v+w) + eps;
}

vector<tri> overlap;
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    overlap.clear();
    scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
    for(int i=0;i<n;++i) {
      int a,b,c;
      scanf("%d%d%d",&a,&b,&c);
      overlap.push_back((tri){a,b,c});
    }
    sort(overlap.begin(), overlap.end());
    vector<node> v;

    for(int i=0; i<overlap.size(); ++i) {
      if(i) {
        if(overlap[i].a != overlap[i-1].b)
          v.push_back((node){overlap[i].a-overlap[i-1].b,s});
      }
      else if(overlap[0].a!=0) v.push_back((node){overlap[i].a,s});
      v.push_back((node){overlap[i].b-overlap[i].a, overlap[i].c+s});
    }
    if(overlap.back().b != x) v.push_back((node){x-overlap.back().b, s});
    
    w=r-s;
    sort(v.begin(), v.end());
    double rest=t;
    double res=0;
    for(int i=0; i<v.size(); ++i) {
      if(w < eps) res += v[i].l/v[i].v;
      else {
        double ti = min (rest, v[i].l/(v[i].v+w));
        rest -= ti;
        res += ti + (v[i].l/(v[i].v+w)-ti)*(v[i].v+w)/v[i].v;
      }
    }
    printf("Case #%d: %.10f\n", cas, res);
  }
  return 0;
}

