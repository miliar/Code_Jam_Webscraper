
#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <cmath>
#include <complex>
#include <numeric>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define FOR(i,s) for(__typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define ALLOF(s) ((s).begin()), ((s).end())

typedef long long integer;


struct K {
  long double len;
  long double v;
};

inline bool operator>(const K& a, const K& b) {
  return a.v > b.v;
}

int main(void) {
  int nCases;
  cin >> nCases;

  REP(iCase, nCases) {
    double len, walk, run, n;
    double t;
    cin >> len >> walk >> run >> t >> n;
    
    double no_walkway = len;
    priority_queue<K, vector<K>, greater<K> > q;
    REP(i, n){
      double bg, ed, v;
      cin >> bg >> ed >> v;
      K cur = {ed - bg, v + walk};
      q.push(cur);
      no_walkway -= cur.len;
    }
    q.push((K){no_walkway, walk});
    
    vector<double> hoge;
    while(!q.empty()){
      K cur = q.top();
      q.pop();
//       cerr << res << endl;
      if(t > 0){
	double v = cur.v - walk + run;
	double tt = cur.len / v;
	if(tt <= t){
	  hoge.push_back(tt);
	  t -= tt;
	  continue;
	}else{
	  hoge.push_back(t);
	  cur.len -= v * t;
	  t = 0;
	}
      }
      hoge.push_back(cur.len / cur.v);
    }
    
    sort(hoge.begin(), hoge.end());
    double res = 0;
    REP(i, hoge.size())
      res += hoge[i];
    
    cout << "Case #" << (iCase+1) << ": ";
    printf("%.10f\n", res);
  }
  
  return 0;
}
