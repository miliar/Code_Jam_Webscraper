#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FOREACH(i,c) for(typeof(c.begin()) i=(c).begin();i!=(c).end();++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

double solve()
{
  map<int,int> speeds;

  int X, S, R, t, N;
  cin >> X >> S >> R >> t >> N;
  int boost = R-S;
  REP(i, N) {
    int B, E, w;
    cin >> B >> E >> w;
    //cout << "B" << B << " " << E << " " << w << endl;
    speeds[w+S] += (E-B);
    X -= (E-B);
  }
  speeds[S] += X;
  double ans = 0;
  double tt = t;
  FOREACH(it, speeds) {
    double len = it->second;
    double speed = it->first;
    //cout << "len, speed = " << len << ", " << speed << endl;
    if(tt*(speed+boost)>len) {
      ans += len/(speed+boost);
      tt -= len/(speed+boost);
    } else {
      ans += tt;
      len -= tt*(speed+boost);
      tt -= tt;
      ans += len/(speed);
    }
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ": ";
    printf("%.9f", solve());
    cout << endl;
  }
}
