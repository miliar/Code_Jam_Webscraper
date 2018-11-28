#include <iostream>
#include <cmath>
#include <climits>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cassert>

using namespace std;

typedef long long ll;

const double EPS = 1e-9;

int d, c;
map<int, int> vs;

double calc(double l, double r){
  if(r - l < EPS) return l;

  double m = (l + r) * 0.5;
  double pre = -1e+20;
  for(map<int, int>::iterator iter = vs.begin(); iter != vs.end(); ++iter){
    for(int i = 0; i < iter->second; ++i){
      if(pre + d <= iter->first)
        pre = max(pre + d, iter->first - m);
      else if(pre + d <= iter->first + m)
        pre = min(pre + d, iter->first + m);
      else
        goto no;
    }
  }
  return calc(l, m);
 no:
  return calc(m, r);
}

int main(void){
  int t;
  cin >> t;
  for(int k = 0; k < t; ++k){
    vs.clear();
    cin >> c >> d;
    for(int i = 0; i < c; ++i){
      int p, v;
      cin >> p >> v;
      assert(vs.find(p) == vs.end());
      vs.insert(make_pair(p, v));
    }

    printf("Case #%d: %.8lf\n", k+1, calc(0, 1e+20));
  }

  return 0;
}
