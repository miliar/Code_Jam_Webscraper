#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

#define pii pair <int,int>
#define tii pair <pii,int >
#define xx first
#define yy second
#define mp(A,B) make_pair(A,B)

using namespace std;

int main(){
  vector <pii> ord;
  vector <tii> inters;
  int cases;

  scanf("%d", &cases);
  for (int ka = 1; ka <=cases; ka++){
    int x, s, r, t, n;
    int last = 0;
    int sz = 0;
    ord.clear();
    inters.clear();
    scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
    for (int i = 0; i < n; i++){
      int b, e, w;
      scanf("%d %d %d", &b, &e, &w);
      if (b > last){
	inters.push_back( mp( mp(last,b), 0 ) );
	ord.push_back(mp(0,sz++));
      }
      inters.push_back(mp(mp(b,e),w));
      ord.push_back(mp(w, sz++));
      last = e;
    }
    if (last < x){
      inters.push_back( mp( mp(last,x), 0 ) );
      ord.push_back(mp(0,sz++));
    }
    sort(ord.begin(), ord.end());

    double total = 0.0;
    double run = t;
    for (int j = 0; j < ord.size(); j++){
      int i = ord[j].yy;
      double l = inters[i].xx.yy-inters[i].xx.xx;
      int w = inters[i].yy;
      if (run*(w+r) >= l){
	total += (l)/(w+r);
	run -= (l)/(w+r);
	//printf("Correndo %d %lf: %lf\n", i, l, total);
	continue;
      }
      else if (run > 0){
	total += run;
	//printf("correndo o que resta (+%lf)\n", run);
	l -= run*(w+r);
	run = 0;
      }
      total += l/((double)w+s);
      //printf("andando %lf (%lf+%lf): +%lf %lf\n", 	     l, w, s, l/((double)w+s), total);
    }
    printf("Case #%d: %.8lf\n", ka, total);
  }

  return 0;
}
