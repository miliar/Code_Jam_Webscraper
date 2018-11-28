#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)
#define ALL(c) c.begin(), c.end() 

#define MAXN 50

typedef struct segm {
  int len;
  int id;
  int speedup;
  double timesavepersec, maxsec;
  
  bool operator<(const segm other) const {
    return other.timesavepersec < timesavepersec;
  }
} segm;

int X,S,R,T,N;

inline void solve() { 
  cin >> X >> S >> R >> T >> N;
  vector<segm> segs(N+1);
  
  double timesum = 0;
  int segsum = 0, cnt = 0;

  REP(i, N){
    int B,E,W;
    cin >> B >> E >> W;
    segs[i].len = E - B;
    segsum += segs[i].len;
    segs[i].speedup = W;
    segs[i].id = cnt++;
  }
  segs[N].len = X - segsum;
  segs[N].speedup = 0;
  segs[N].id = cnt++;
 
  FORI(it, segs){
    int len = it->len;
    int speedup = it->speedup;
    timesum += len / double(S + speedup);
    it->maxsec = len / double(R + speedup);
    double fasterpersec = (R - S);
    it->timesavepersec =  fasterpersec / double(S + speedup);
    //cerr << "seg " << it->id << " len=" << len << " fasterpersec: " << it->timesavepersec << " maxsec: " << it->maxsec << endl;   
  }


  sort(ALL(segs));

  double runtime = T;
  FORI(it, segs){
    double secs = min(runtime, it->maxsec);
    timesum -= secs * it->timesavepersec;
    runtime -= secs;
    //cerr << "save on " << it->id << " persec: " << it->timesavepersec << " for " << secs << endl;  
    if(runtime <= 0) break;
  }
  printf("%.7lf", timesum);
  //cout << timesum;
}

int main() {
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ": ";
    solve();
    cout << endl;
  }
} 
