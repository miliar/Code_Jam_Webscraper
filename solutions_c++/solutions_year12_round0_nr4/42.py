#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

char g[64][64];

int main(){
  int t = getInt();

  REP(cc, t){
    int h = getInt();
    int w = getInt();
    int d = getInt();

    REP(i,h) scanf("%s", g[i]);

    double sx, sy;
    REP(i,h) REP(j,w){
      if(g[i][j] == 'X'){
	sx = j + 0.5; sy = i + 0.5;
	g[i][j] = '.';
	break;
      }
    }

    vector<double> ans;
    const double PI  = 2 * acos(0);
    const double EPS = 1e-10;

    int lim = 2 * max(d, max(h, w));
    for(int xx = -lim; xx <= lim; xx++){
      for(int yy = -lim; yy <= lim; yy++) if(xx || yy){
	double ds = sqrt(xx * xx + yy * yy);
	double dx = xx / ds;
	double dy = yy / ds;

	// printf("[%d %d]\n", xx, yy);

	double x = sx;
	double y = sy;

	double dist = 0.0;

	while(true){
	  double nt = 10000.0;

	  double nx = 10000.0;
	  if(dx > EPS) nx = ceil(x * 2 + EPS) / 2;
	  else if(dx < -EPS) nx = floor(x * 2 - EPS) / 2;
	  if(std::abs(dx) > EPS) nt = min(nt, (nx - x) / dx);

	  double ny = 10000.0;
	  if(dy > EPS) ny = ceil(y * 2 + EPS) / 2;
	  else if(dy < -EPS) ny = floor(y * 2 - EPS) / 2;
	  if(std::abs(dy) > EPS) nt = min(nt, (ny - y) / dy);

	  x += dx * nt;
	  y += dy * nt;

	  dist += sqrt(nt * nt * dx * dx + nt * nt * dy * dy);
	  // printf(" %.2f %.2f: %.2f\n", x, y, dist);

	  if(dist > d + EPS) break;

	  if(std::abs(sx - x) + std::abs(sy - y) < EPS){
	    ans.push_back(atan2(dx, dy));
	    // printf(" found!!\n");
	  }

	  bool xf  = g[(int)(y - dy * EPS)][(int)(x + dx * EPS)] == '#';
	  bool yf  = g[(int)(y + dy * EPS)][(int)(x - dx * EPS)] == '#';
	  bool xyf = g[(int)(y + dy * EPS)][(int)(x + dx * EPS)] == '#';

	  if(xyf){
	    if(xf && yf){
	      dx *= -1; dy *= -1;
	    }else{
	      if(xf){
		dx *= -1;
	      }else if(yf){
		dy *= -1;
	      }else{
		break;
	      }
	    }
	  }
	}
      }
    }

    sort(ans.begin(), ans.end());

    int cnt = 0;
    REP(i,ans.size()){
      if(i == 0){
	cnt++;
	// printf("%.2f ", ans[i]);
      }else if(std::abs(ans[i - 1] - ans[i]) > EPS &&
	       std::abs(ans[i] - (ans[0] + 2 * PI)) > EPS){
	// printf("%.2f ", ans[i]);
	cnt++;
      }
    }
    // printf("\n\n\n\n\n\n");

    printf("Case #%d: %d\n", cc + 1, cnt);
  }

  return 0;
}
