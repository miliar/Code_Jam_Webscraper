#include<cstdio>
#include<algorithm>

using namespace std;

struct R {
  int r, i;
  double x, y;
};
bool operator < (const R& a, const R& b)
{
  return a.r > b.r;
}
bool cmp(const R& a, const R& b)
{
  return a.i < b.i;
}

bool check(double dx, double dy, double rr)
{
  return dx*dx + dy*dy >= rr*rr + 1e-6;
}

int main()
{
  int T;
  scanf("%d", &T);
  
  for(int CN=1; CN<=T; ++CN) {
    int N, W, L;
    scanf("%d%d%d", &N, &W, &L);
    
    R r[1024];
    for(int i=0; i<N; ++i)
      scanf("%d", &r[i].r), r[i].i=i;
    
    sort(r, r+N);
    double px = 0;
    int dir = 1;
    for(int i=0; i<N; ++i) {
      double lo = 0, hi = L + 1e-6;
      for(int loop=0; loop<50; ++loop) {
        double mid = (hi+lo) / 2;
        bool ok = true;
        for(int j=0; ok && j<i; ++j)
          if(!check(px-r[j].x, mid-r[j].y, r[i].r+r[j].r))
            ok = false;
        if(ok) hi = mid;
        else lo = mid;
      }
      if(hi >= L) { fprintf(stderr, "YABAI!!!!\n"); }
      r[i].x = px;
      r[i].y = hi + 1e-6;
      if(i == N-1) break;
      if(dir == 1) {
        px += r[i].r + r[i+1].r + 1e-6;
        if(px > W) { px=W; dir=-1; }
      } else {
        px -= r[i].r + r[i+1].r + 1e-6;
        if(px < 0) { px=0; dir=+1; }
      }
    }
    
    sort(r, r+N, cmp);
    
    fprintf(stderr, "!!! Case #%d !!!\n", CN);
    printf("Case #%d:", CN);
    for(int i=0; i<N; ++i)
      printf(" %f %f", r[i].x, r[i].y);
    puts("");
    
    // check
    for(int i=0; i<N; ++i)
      if(r[i].x<0 || r[i].x>W || r[i].y<0 || r[i].y>L)
        fprintf(stderr, "\\(^o^)/\n");
    for(int i=0; i<N; ++i)
      for(int j=i+1; j<N; ++j)
        if(!check(r[i].x-r[j].x, r[i].y-r[j].y, r[i].r+r[j].r))
          fprintf(stderr, "OWACON\n");
  }
}
