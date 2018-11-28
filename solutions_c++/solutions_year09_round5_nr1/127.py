#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <cmath>
#include <set>

using namespace std;

typedef long long LL;
typedef vector<string> Vs;
typedef vector<int> Vi;
typedef vector<bool> Vb;
typedef vector<long long> Vll;
typedef vector<double> Vd;
typedef vector<Vi> Mi;
#define forUp(x,y) for(int x=0;x<(y);x++)
#define forDown(x,y) for(int x=(y)-1;x>=0;x--)
#define LET(l,r) forUp(_t,1) for(typeof(r) l=r; !_t; _t=1)
#define forEach(x,c) LET(&_s,(c)) LET(_x,_s.begin()) for(;_x!=_s.end();_x++) LET(&x,*_x)

struct PointI {
  PointI() : x(0), y(0) {}
  PointI(int x, int y) : x(x), y(y) {}
  
  int x,y;
};
typedef vector<PointI> Vp;
bool operator==(const PointI& a, const PointI& b) { return a.x==b.x && a.y==b.y; }
ostream& operator<<(ostream& os, PointI p) {
  return os << "(" << p.x << "," << p.y << ")";
}

int nRows,nCols;
int nBlocks;
Vs m;

const int Inf=1000000000;

const int dx[] = {0, -1, 1, 0};
const int dy[] = {-1, 0, 0, 1};

bool vis[100];

struct State {
  Vp p;
  int d;

  bool isGoal() {
    forUp(i,nBlocks) {
      char ch=m[p[i].y][p[i].x];
      if (ch!='x' && ch!='w') return false;
    }
    return true;
  }

  bool empty(int i, int d) {
    PointI t(p[i].x+dx[d], p[i].y+dy[d]);
    if (t.x<0 || t.x>=nCols) return false;
    if (t.y<0 || t.y>=nRows) return false;
    char ch=m[t.y][t.x];
    if (ch=='#') return false;
    forUp(j,nBlocks) 
      if (j != i && p[j]==t) return false;
    return true;
  }

  void move(int i, int d) {
    p[i].x+=dx[d];
    p[i].y+=dy[d];
  }

  LL encode() {
    LL v=0;
    forUp(i,nBlocks) v=144*v+p[i].y*12+p[i].x;
    return v;
  }

  static bool neighb(PointI &a, PointI &b) {
    return abs(a.x-b.x)+abs(a.y-b.y)==1;
  }

  int dfs(int i) {
    vis[i]=true;
    int v=1;
    forUp(j,nBlocks) if (!vis[j] && neighb(p[j],p[i]))
      v+=dfs(j);
    return v;
  }
  bool stable() {
    forUp(i,nBlocks) vis[i]=false;
    return dfs(0)==nBlocks;
  }
};

State startState() {
  nBlocks=0;
  State s;
  s.d=0;
  forUp(r,nRows) forUp(c,nCols)
    if (m[r][c]=='o' || m[r][c]=='w') {
      s.p.push_back(PointI(c,r));
      nBlocks++;
    }
  return s;
}

int bfs() {
  queue<State> q;
  map<LL,bool> vis;
  q.push(startState());
  if (startState().isGoal()) return 0;

  while (!q.empty()) {
    State s=q.front(); q.pop();
    bool wasStable=s.stable();
    forUp(i,nBlocks) forUp(d,4)
      if (s.empty(i,d) && s.empty(i,3-d)) {
        s.move(i,d); s.d++;
        if (s.isGoal()) return s.d;
        if (wasStable || s.stable()) {
          LL enc=s.encode();
          if (!vis[enc]) {
            vis[enc]=true;
            q.push(s);
          }
        }
        s.move(i,3-d); s.d--;
      }
  }

  return -1;
}

int main() {
//   freopen("a2.in","r",stdin);
  int nCases;
  cin >> nCases;
  forUp(cnr,nCases) {
    cin >> nRows >> nCols;
    string s;
    getline(cin,s);
    m=Vs(nRows,string(nCols, ' '));
    forUp(r,nRows)
      getline(cin,m[r]);

    int res=bfs();
    cout << "Case #" << cnr+1 << ": " << res << endl;
  }
  
  return 0;
}






