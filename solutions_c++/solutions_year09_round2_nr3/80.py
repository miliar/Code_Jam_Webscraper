#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

string INF(1, 251);
string undef(1,250);

int W;
VVI board;

const int depth=100;
string *cache[600][depth][20][20];

int dr[]={0,-1,0,1};
int dc[]={1,0,-1,0};

string solvenum(int q,int d,int r, int c);

string solveop(int q,int d, int r, int c) {
  string res=INF;
  REP(dir, 4) {
    int nr=r+dr[dir], nc=c+dc[dir];
    if(nr<0 || nr>=W || nc<0 || nc>=W) continue;
    int nq;
    if(board[r][c]=='+') nq=q-(board[nr][nc]-'0');
    else nq=q+(board[nr][nc]-'0');
    string test=solvenum(nq,d,nr,nc);
    if(test!=INF) res=min(res,(char)board[r][c]+test);
  }
  return res;
}

string solvenum(int q,int d,int r, int c) {
  if(abs(q)>=300) return INF;
  if(d==0) {
    if(q==0) return (string)""+(char)board[r][c];
    else return INF;
  }
  if(cache[q+300][d][r][c]!=&undef) return (*cache[q+300][d][r][c]);
  string res=INF;
  REP(dir, 4) {
    int nr=r+dr[dir], nc=c+dc[dir];
    if(nr<0 || nr>=W || nc<0 || nc>=W) continue;
    string test=solveop(q,d-1,nr,nc);
    if(test!=INF) res=min(res,(char)board[r][c]+test);
  }
  cache[q+300][d][r][c]=new string(res);
  return res;
}


string solve(int q) {
  REP(l, 600) REP(k, depth) REP(i,20) REP(j,20) cache[l][k][i][j]=&undef;
  string res=INF;
  REP(d,depth) {
    REP(i, W) REP(j, W) {
      if(board[i][j]<'0' || board[i][j]>'9') continue;
      int nq=q-(board[i][j]-'0');
      res=min(res,solvenum(nq,d,i,j));
//      res;
    }
    if(res!=INF) break;
  }
  return res;
}

void go() {
  int Q;
  cin >> W >> Q;
  board=VVI(W,VI(W));
  REP(i, W) {
    string s;
    cin >> s;
//    cout << W << " "<< s << endl;
    REP(j, W) board[i][j]=s[j];
  }
  REP(i, Q) {
    int q;
    cin >> q;
    cout << solve(q) << endl;
  }
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) {
    cout << "Case #"<<i+1<<":\n";
    go();
  }
}
