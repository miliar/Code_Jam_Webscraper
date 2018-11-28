#include <set>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  const int t = getInt();

  REP(cc, t){
    const int n = getInt();
    const int w = getInt();
    const int h = getInt();

    vector<pair<int, int> > r(n);

    REP(i,n){
      r[i].first  = getInt();
      r[i].second = i;
    }

    printf("Case #%d: ", cc + 1);

    sort(r.rbegin(), r.rend());

    vector<int> x(n);
    vector<int> y(n);

    int mR = 0;
    int xx = 0;
    int yy = 0;

    REP(i,n){
      int rr = r[i].first;
      int idx = r[i].second;

      mR = max(mR, rr);

      if(yy == 0){
	x[idx] = xx;
	y[idx] = yy;
      }else{
	yy += rr;

	if(yy <= h){
	  x[idx] = xx;
	  y[idx] = yy;
	}else{
	  xx += mR + rr;
	  yy = 0;
	  mR = rr;

	  x[idx] = xx;
	  y[idx] = yy;
	}
      }

      yy += rr;

      if(x[idx] > w || y[idx] > h) throw 0;
    }

    REP(i,n) printf("%d.0 %d.0%c", x[i], y[i], i == n - 1 ? '\n' : ' ');
  }

  return 0;
}
