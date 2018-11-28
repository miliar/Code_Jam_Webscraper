#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int w, l, u, g;

struct point {
  int x;
  long double y1, y2;

  point(int xx, long double yy1, long double yy2) : x(xx), y1(yy1), y2(yy2) {}

  long double h() { return y2-y1;}
};

const long double eps=1e-8;

vector<point> cake;

long double solve(int d) {
  long double area=0;
  for(size_t i=1;i<cake.size();i++)
    area += static_cast<long double>(cake[i].x-cake[i-1].x)*(cake[i].h()+cake[i-1].h())/2;
  //std::cerr << "solve(" << d << "):" << area << '\n';

  long double cur_area=0;
  for(size_t i=1;i<cake.size();i++){
    long double cur = static_cast<long double>(cake[i].x-cake[i-1].x)*(cake[i].h()+cake[i-1].h())/2;
    
    if(cur_area + cur > area * d / g) {
      //std::cerr << "aha..." << cake[i-1].x << ' ' << cake[i-1].h() << "=>" << cake[i].x << ' ' << cake[i].h() << '\n';
      long double r = (area * d / g - cur_area)/(cake[i].x-cake[i-1].x);
      double a = cake[i-1].h();
      double b = cake[i].h();

      if(abs(b-a)<eps) return cake[i-1].x + (area * d / g - cur_area)/a;

      //if(b>a)
      return cake[i-1].x + (sqrt(a*a+2*r*(b-a))-a) * (cake[i].x-cake[i-1].x)/(b-a);
      //else
      //return cake[i-1].x + (sqrt(a*a+r*(b-a))-a) * (cake[i].x-cake[i-1].x)/(b-a);
    }

    cur_area += cur;
  }
  return -1;
}

int main() {
  int t;
  cin >> t;

  cout.precision(std::numeric_limits< double >::digits10);
  //cout << sizeof(long) << ' ' << sizeof(int) << ' ' << sizeof(long long) << '\n';

  for(int tcase=1;tcase<=t;tcase++){
    cin >> w >> l >> u >> g;
    vector<pair<int, double> > low(l), up(u);
    for(int i=0;i<l;i++)
      cin >> low[i].first >> low[i].second;

    for(int j=0;j<u;j++)
      cin >> up[j].first >> up[j].second;

    cake.clear();

    low.push_back(low[l-1]);
    up.push_back(up[u-1]);

    cake.push_back(point(0, low[0].second, up[0].second));

    for(int i=1,j=1;(i<l)||(j<u);){
      point p(0, 0, 0);
      if((i<l)&&((j>=u)||(low[i].first<up[j].first))) {
	p.x = low[i].first;
	p.y1 = low[i].second;
	if(up[j].first==cake.rbegin()->x)
	  p.y2 = cake.rbegin()->y2;
	else
	  p.y2 = cake.rbegin()->y2+(up[j].second-cake.rbegin()->y2)*(p.x-cake.rbegin()->x)/(up[j].first-cake.rbegin()->x);
	i++;
      } else {
	p.x = up[j].first;
	p.y2 = up[j].second;
	if(low[i].first==cake.rbegin()->x)
	  p.y1 = cake.rbegin()->y1;
	else
	  p.y1 = cake.rbegin()->y1+(low[i].second-cake.rbegin()->y1)*(p.x-cake.rbegin()->x)/(low[i].first-cake.rbegin()->x);
	j++;
      }
      cake.push_back(p);
    }

    cout << "Case #" << tcase << ":\n";
    for(int i=1;i<g;i++) cout << solve(i) << '\n';
  }
}
