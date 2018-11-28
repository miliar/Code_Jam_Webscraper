#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define X first
#define Y second
#define PB push_back
#define FOR(x,y) for (int x = 0; x < int(y); ++x)
#define debug(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef long double ld;
typedef pair<int, int> P;
typedef vector<bool> Vb;
typedef vector<Vb> Mb;
typedef vector<char> Vc;
typedef vector<Vc> Mc;
typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef vector<P> Vp;
typedef vector<Vp> Mp;
typedef vector<string> Vs;
typedef vector<Vs> Ms;

typedef queue<P> Q;
typedef queue<Mb> Q2;
typedef priority_queue<int> PQ;
typedef stack<int> STACK;
typedef set<Mb> SET;
typedef SET::iterator Sit;
typedef map<int, int> MAP;
typedef MAP::iterator Mit;
typedef stringstream SS;

template <class Ta, class Tb> inline Tb cast(Ta a) { SS ss; ss << a; Tb b; ss >> b; return b; };

const double EPS = 1e-9;
const int INF = 1000000000;
const int MOD = 1000000007;
const int diri[] = { 1, 0, 0 };
const int dirj[] = { 0, 1, -1 };

int R, C;
Mc mapa;

Mb reachable(int r, int c) {
  Mb res(R, Vb(C, false));
  res[r][c] = true;
  
  Q q;
  q.push(P(r, c));
  
  while (q.size()) {
    int x = q.front().X;
    int y = q.front().Y;
    q.pop();
    
    for (int k = 0; k < 3; ++k) {
      int i = x - diri[k];
      int j = y + dirj[k];
      if (0 <= i and i < R and 0 <= j and j < C and mapa[i][j] != '#' and not res[i][j]) {
        res[i][j] = true;
        q.push(P(i, j));
      }
    }
  }
  
  return res;
}

Mb move(Mb mat, int dr, int dc) {
  Mb res(R, Vb(C, false));
  for (int r = 0; r < R; ++r)
    for (int c = 0; c < C; ++c) {
      if (not mat[r][c]) continue;
      int i = r + dr;
      int j = c + dc;
      if (0 <= i and i < R and 0 <= j and j < C and mapa[i][j] != '#') res[i][j] = true;
      else res[r][c] = true;
    }
  return res;
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    cin >> R >> C;
    mapa = Mc(R, Vc(C));
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
        cin >> mapa[i][j];
    
    Vp v(10, P(-1, -1));
    for (int i = 0; i < R; ++i)
      for (int j = 0; j < C; ++j)
        if ('0' <= mapa[i][j] and mapa[i][j] <= '9')
          v[mapa[i][j] - '0'] = P(i, j);
    
    cout << "Case #" << cas << ":" << endl;
    for (int cave = 0; cave < 10; ++cave) {
      
//       cerr << "cave=" << cave << endl;
      if (v[cave].X == -1) break;
      
//       cerr << "A" << endl;
      Mb ini = reachable(v[cave].X, v[cave].Y);
//       cerr << "B" << endl;
      int ini_ones = 0;
      for (int i = 0; i < R; ++i)
        for (int j = 0; j < C; ++j)
          if (ini[i][j]) ++ini_ones;
      
      Q2 q;
      q.push(ini);
      
      SET vist;
      vist.insert(ini);
      
      bool ok = false;
      
      while (q.size()) {
        Mb current = q.front();
        q.pop();
        
        Vp tmp;
        for (int i = 0; i < R; ++i)
          for (int j = 0; j < C; ++j)
            if (current[i][j]) tmp.PB(P(i, j));
        if (tmp.size() == 1 and tmp[0] == v[cave]) {
          ok = true;
          break;
        }
        
        for (int k = 0; k < 3; ++k) {
          Mb next = move(current, diri[k], dirj[k]);
          
          bool valid = true;
          for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j)
              if (next[i][j] and not ini[i][j])
                valid = false;
          
          if (valid and vist.count(next) == 0) {
            vist.insert(next);
            q.push(next);
          }
        }
      }
      
      cout << cave << ": " << ini_ones << " ";
      if (ok) cout << "Lucky" << endl;
      else cout << "Unlucky" << endl;
    }
    
  }
}
