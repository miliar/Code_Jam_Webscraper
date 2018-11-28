#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

long double walk, run;
long double remain;

class Way{
public:
  long double  d, plus;
  long double diff;
  long double walkTime;
  long double runTime;
  long double simpleRunTime;
  void makeDiff(){
    walkTime = (long double)d / (long double)(plus + walk);
    long double runLength = min((long double)d, remain * ( plus + run));
    simpleRunTime = runTime = (long double) runLength / (long double)(run + plus);
    if(runLength < d){
      long double walkLength = d - runLength;
      runTime += (long double) walkLength / (long double)(walk + plus);
    }
    diff = abs(walkTime - runTime); 
  }
  bool operator<(const Way &w)const{
    if(remain < EPS)return diff < w.diff;
    return diff/simpleRunTime < w.diff/w.simpleRunTime;
  }
};

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1 << ": ";
    int X, n;
    vector<Way> V;
    cin >> X >> walk >> run >> remain >> n;
    rep(i, n){
      int from, end, plus;
      cin >> from >> end >> plus;
      X -= end - from;
      Way w;
      w.d = end - from;
      w.plus = plus;
      V.push_back(w);
    }
    Way w;
    w.d = X;
    w.plus =0;
    V.push_back(w);
    long double ans = 0;
    while(V.size() != 0){
      FOR(it, V)it->makeDiff();
      sort(ALL(V));
      ans += min(V.back().runTime, V.back().walkTime);
      remain -= V.back().runTime;
      remain = max((long double)0, remain);
      V.pop_back();
    }
    cout << flush;
    printf("%.9Lf\n", ans);
  }
  return 0;
}
