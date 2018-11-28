#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751

map<string, vector< pair<int, int> > > MAP;
int Y;

/*
int Sol () {

  VS COL;
  VI MIN, MAX;
  FOREACH(it, MAP) {
    REP(i, (it->second).sz) {
      COL.pb(it->first);
      MIN.pb(it->second[i].first);
      MAX.pb(it->second[i].second);
    }
  }



  int N = COL.sz;
  int best = INF;

//  cout << N << " " << best << endl;

  REP(i, 1 << N) {
   // cout << i << endl;
    set<string> CO;
    REP(k, N) if(i & (1 << k)) CO.insert(COL[k]);

 //   cout << "#" << i << " " << CO.sz << endl;
    if(CO.sz > 3) continue;

    bool okk = true;
    for(int j = 1; j <= 10000; j++) {
      bool ok = false;
      REP(k, N) if(i & (1 << k)) if(MIN[k] <= j && MAX[k] >= j) {ok = true; break;}
      if(ok == false) {okk = false; break;}
    }

    if(okk && __builtin_popcount(i) < best) best = __builtin_popcount(i);
  }

  if(best == INF) return 0;
  else return best;
}
*/
int Sol() {







  int best = 1000000;

  FOREACH(it1, MAP) 
  FOREACH(it2, MAP) 
  FOREACH(it3, MAP) {
//    cout << it1->first << " " << it2->first << " " << it3->first << " " << endl;
    vector<pair<int, int> > V;
    V.insert(V.end(), it1->second.begin(), it1->second.end());
    V.insert(V.end(), it2->second.begin(), it2->second.end());
    V.insert(V.end(), it3->second.begin(), it3->second.end());

//    cout << "bubu7" << endl;


    SORT(V);
    UNIQ(V);
//    REP(i, V.sz) cout << V[i].first << " " << V[i].second << " # " ;
//    cout << endl;

    int last = 0;    
    int k = 0;
    int nb = 0;

    while(k < V.sz) {
//      cout << V.sz << " " << k << endl;
      int next = -1;
      for(; k < V.sz && V[k].first <= last +1; k++) {
       /* if(V[k].second > last)*/ next = max(next, V[k].second);
      }
      nb++;
//     if(Y == 45) cout << nb << " " << next << " " << last << endl;
      last = next;
      if(last == -1 || last >= 10000) break;
    }
    if(last == -1) continue;
    if(last >= 10000 && nb <= best) best = nb;
  }

  if(best == 1000000) return 0;
  else return best;
}


int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N;
    Y = t;
    cin >> N;
    MAP.clear();
    REP(n, N) {
      
      string C;
      int A, B;

     
      cin >> C >> A >> B;

      MAP[C].push_back(pair<int, int> (A, B));
    }
    int sol = Sol();
    if(sol == 0) cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    else cout << "Case #" << t << ": " << sol << endl;
  }
}
