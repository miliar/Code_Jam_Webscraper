#include <iostream>
#include <cmath>
#include <algorithm>
using std::max;
#define MAX 10
struct pir {
  double x,y,r;
};
pir round[MAX];

inline double SQR(double x) {
  return x*x;
}
double dis(const pir&a,const pir&b) {
  return sqrt(SQR(a.x-b.x)+SQR(a.y-b.y));
}
bool coverd(const pir&a,const pir&b) {
  return a.r-dis(a,b)>b.r;
}
pir get_round(const pir&a,const pir&b) {
  pir vec,zero;
  zero.x = 0;zero.y = 0;zero.r = 0;
  vec.x = a.x-b.x;vec.y = a.y-b.y;
  double ll = dis(zero,vec);
  vec.x/=ll;vec.y/=ll;
  pir aa = a,bb = b;
  aa.x += vec.x*aa.r;
  aa.y += vec.y*aa.r;
  bb.x -= vec.x*bb.r;
  bb.y -= vec.y*bb.r;
  pir ret;
  ret.x = (aa.x+bb.x)/2;
  ret.y = (aa.y+bb.y)/2;
  ret.r = dis(aa,bb)/2;
  return ret;
}
pir cal_two(int i,int j){
  pir tmp;
  if (coverd(round[i],round[j])) {
    tmp = round[i];
  } else if (coverd(round[j],round[i])) {
    tmp = round[j];
  } else {
    tmp = get_round(round[i],round[j]);
  }
  return tmp;
}
bool chek[MAX];
double ans;
void search(int step,int N) {
  if (step==N) {
    pir A,B;
    A.r = 0;B.r = 0;
    for (int i = 0;i<N;++i) {
      if (chek[i]) {
        if (A.r<1e-6) A = round[i];
        else A = get_round(A,round[i]);
      } else {
        if (B.r<1e-6) B = round[i];
        else B = get_round(B,round[i]);
      }
    }
    if (max(A.r,B.r)<ans) ans = max(A.r,B.r);
  } else {
    for (int i = 0;i<2;++i) {
      if (i==0) chek[step] = false;
      else chek[step] = true;
      search(step+1,N);
    }
  }
}
int main(void) {
  int T;
  freopen("A.txt","r",stdin);
  freopen("fdout.txt","w",stdout);
  scanf("%d",&T);
  for (int cas = 1;cas<=T;++cas) {
    int N;
    scanf("%d",&N);
    for (int i = 0;i<N;++i)
      scanf("%lf%lf%lf",&round[i].x,&round[i].y,&round[i].r);
    memset(chek,0,sizeof(chek));
    ans = 1000000;
    search(0,N);
    printf("Case #%d: %lf\n",cas,ans);
  }
  return 0;
}