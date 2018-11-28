#include <cmath>
#include <cstdlib>
#include <cassert>
#include <climits>
#include <cfloat>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <string>
#include <boost/lexical_cast.hpp>
#include <boost/foreach.hpp>
#include <boost/tokenizer.hpp>

using namespace std;
using namespace boost;

#define foreach BOOST_FOREACH

typedef vector<vector<int> > matrix;

struct Plant{
  Plant():x(0), y(0), r(0){}
  Plant(int x_, int y_, int r_):x(x_), y(y_), r(r_){}
  int x, y, r;
};

double solve(const vector<Plant>& ps){
  const int n = ps.size();
  assert(n <= 3);
  if(n==1)return ps.front().r;
  if(n==2){
    return max(ps[0].r, ps[1].r);
  }
  double ret(DBL_MAX);
  for(int i=0;i!=n;++i){
    int s = 1;
    double dx(0), dy(0), rs(0);
    for(int j=0;j!=n;++j){
      if(j==i)continue;
      dx += ps[j].x*s;
      dy += ps[j].y*s;
      s = -s;
      rs += ps[j].r;
    }
    const double r1 = (sqrt(dx*dx + dy*dy)+rs)/2.0;
    const double res = max(r1, double(ps[i].r));
    ret = min(ret, res);
  }
  return ret;
}

int main(int argc, char* argv[]){
  int C;
  cin >> C;
  for(int icase=1;icase<=C;++icase){
    int N;
    cin >> N;
    vector<Plant> ps;
    for(int i=0;i!=N;++i){
      int X, Y, R;
      cin >> X >> Y >> R;
      ps.push_back(Plant(X, Y, R));
    }
    cout << "Case #" << icase << ": " << solve(ps) << endl;
  }
  return 0;
}
