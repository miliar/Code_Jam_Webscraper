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


int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

string solve(int q, VS M) {
  int N = M.sz;
  map<int,string> T[N][N];
  int MM[N][N];
  for(int x = 0; x < N; x++) for(int y = 0; y < N; y++) 
  if(M[x][y] >= '0' && M[x][y] <= '9') {
    MM[x][y] = M[x][y] - '0';
    T[x][y][MM[x][y]] = M[x][y];
  }
  else MM[x][y] = -1;

  while(true) {
    string best = "z";
    REP(x, N) REP(y, N) if(MM[x][y] >= 0) if(T[x][y].find(q) != T[x][y].end()) if(T[x][y][q] < best) best = T[x][y][q];
    if(best != "z") return best;
  
    map<int,string> T2[N][N];
    REP(x, N) REP(y, N) if(MM[x][y] >= 0) FOREACH(it, T[x][y]) {

      REP(s1, 4) if(x + dx[s1] >= 0 && x + dx[s1] < N && y + dy[s1] >= 0 && y + dy[s1] < N) {
        int x2 = x + dx[s1];
        int y2 = y + dy[s1];
        int mult = 1; if(M[x2][y2] == '-') mult = -1;
        REP(s2, 4) if(x2 + dx[s2] >= 0 && x2 + dx[s2] < N && y2 + dy[s2] >= 0 && y2 + dy[s2] < N) {
          int x3 = x2 + dx[s2];
          int y3 = y2 + dy[s2];
          int sum = it->first + mult*MM[x3][y3];
          string str = it->second + M[x2][y2] + M[x3][y3];
      //    cerr << M[x2][y2] << endl;
          if(T2[x3][y3].find(sum) == T2[x3][y3].end() || str < T2[x3][y3][sum]) T2[x3][y3][sum] = str;
        }
      }
    }

    REP(x, N) REP(y, N) if(MM[x][y] >= 0) T[x][y].swap(T2[x][y]);

  }



}




int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    int W, Q;
    cin >> W >> Q;
    string line;
    getline(cin, line);
    VS M;
    REP(k, W) {
      getline(cin, line);
      M.pb(line);
//      cerr << line << endl;
    }
    cout << "Case #" << i << ":" << endl;
    REP(k, Q) {
      int q;
      cin >> q;
      cout << solve(q, M) << endl;
    }
  }
}
