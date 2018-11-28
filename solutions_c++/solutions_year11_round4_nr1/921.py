#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
struct walkway{
  int b,e,w;
  int sp;
  double t;
  bool operator<(const walkway b) const{
    return sp<b.sp;
  }
} w[1000];
int main(){
  int t;
  cin >> t;
  for (int kkk=1; kkk<=t;++kkk)
    {
      cout << "Case #" <<kkk<<": ";
      int s,r,t,n;
      double x;
      cin >> x >> s >> r >> t >> n;
      for (int i = 0; i <n; ++i ){
	cin >> w[i].b>>w[i].e>>w[i].w;
	x-=(w[i].e-w[i].b);
	w[i].sp = w[i].w+s;
	w[i].t = (w[i].e-w[i].b)/w[i].sp;
      }
      double tl = t;
      double usedtime=0;
      sort(w,w+n);
      if (tl*r<=x){
	x-=tl*r;
	usedtime = tl;
	tl = 0;
      }else{
	tl-=x/r;
	usedtime=x/r;
	x = 0;
      }
      usedtime += x/s;
      for (int i = 0; i < n; ++i){
	double newsp = w[i].sp+r-s;
	if ((w[i].e-w[i].b)<=tl*newsp){
	  tl-=((w[i].e-w[i].b)/newsp);
	  usedtime+=((w[i].e-w[i].b)/newsp);
	}else{
	  usedtime+=(tl)+((w[i].e-w[i].b-tl*newsp)/w[i].sp);
	  tl=0;
	}	
      }
      cout << setprecision(10)<<usedtime << endl;
    }

}
