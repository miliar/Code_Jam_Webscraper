#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#define pb push_back
#define all(a) (a).begin(),(a).end()
#define sz(a) (int)((a).size())
#define rep(i,n) for(int i=0; i<n; ++i)
#define fori(T,v,i) for(T::iterator i = v.begin(); i != v.end(); i++)
#define forc(T,v,i) for(T::const_iterator i = v.begin(); i != v.end(); i++)
static const double EPS = 1e-8;

typedef vector<bool> Array;
typedef vector<Array> Mat;
int N, K;

bool ver(char c, vector<string> &g) {
  Mat mat(N, Array(N, false));
  rep (y, N) {
    rep (x, N) {
      if (!mat[y][x] && g[y][x] == c) {
	int len = 0;
	for (int i = 0; y+i < N; i++) {
	  if (g[y+i][x] != c) break;
	  mat[y + i][x] = true;
	  len++;
	}
	if (len >= K) return true;
      }
    }
  }
  return false;
}

bool hor(char c, vector<string> &g) {
  Mat mat(N, Array(N, false));
  rep (y, N) {
    rep (x, N) {
      if (!mat[y][x] && g[y][x] == c) {
	int len = 0;
	for (int i = 0; x+i < N; i++) {
	  if (g[y][x+i] != c) break;
	  mat[y][x+i] = true;
	  len++;
	}
	if (len >= K) return true;
      }
    }
  }
  return false;
}

bool rig(char c, vector<string> &g) {
  Mat mat(N, Array(N, false));
  rep (y, N) {
    rep (x, N) {
      if (!mat[y][x] && g[y][x] == c) {
	int len = 0;
	for (int i = 0; x+i < N && y+i < N; i++) {
	  if (g[y+i][x+i] != c) break;
	  mat[y+i][x+i] = true;
	  len++;
	}
	if (len >= K) return true;
      }
    }
  }
  return false;
}

bool lef(char c, vector<string> &g) {
  Mat mat(N, Array(N, false));
  rep (y, N) {
    rep (x, N) {
      if (!mat[y][x] && g[y][x] == c) {
	int len = 0;
	for (int i = 0; x-i >= 0 && y+i < N; i++) {
	  if (g[y+i][x-i] != c) break;
	  mat[y+i][x-i] = true;
	  len++;
	}
	if (len >= K) return true;
      }
    }
  }
  return false;
}


int main () {
  int T; cin >> T;
  for (int tcase = 0; tcase < T; tcase++) {
    string result = "Neither";
    cin >> N >> K;
    
    vector<string> g;
    rep (i, N) {
      string str; cin >> str;
      g.pb(str);
    }

    rep (i, N) {
      string tmp = "";
      rep (x, N) if (g[i][x] != '.') tmp += g[i][x];
      for (;sz(tmp) < N;) tmp.insert(0, ".");
      g[i] = tmp;
    }

    bool rR = false, rB = false;
    
    rR = ver('R', g);
    rB = ver('B', g);
    if (!rR) rR = hor('R', g);
    if (!rB) rB = hor('B', g);
    if (!rR) rR = rig('R', g);
    if (!rB) rB = rig('B', g);
    if (!rR) rR = lef('R', g);
    if (!rB) rB = lef('B', g);
    if (rR && rB) result = "Both";
    else if (rR)  result = "Red";
    else if (rB)  result = "Blue";
   
    
    cout << "Case #" << (tcase+1) << ": " << result << endl;
  }
  return 0;
}
