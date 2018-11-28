#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}
template<class T>void pv(T a,T b){for(T i=a;i!=b;++i)cout<<*i<<' ';cout<<endl;}

int N, M;

vector< vector<int> > room;

int ans;
vector<int> ans_v;

int from[2011], to[2011];
int mark[2011];
vector<int> color;
bool ok;
bool check(int C) {

  REP(r, room.size()) {
    const vector<int> &R = room[r];
    memset(mark, 0, sizeof(mark));
    REP(i, R.size()) {
      mark[ color[R[i] - 1] ] = true;
    }

    REP(i, C) {
      if (!mark[i]) return false;
    }
    
  }
  return true;
}

void rec(int n, int C) {
  if (n == N) {
    if (check(C)) {
      ok = true;
      ans = C;
      ans_v = color;
    }
    return ;
  }
  if (ok) return;
  for (int i = 0; i < C; i++) {
    color[n] = i;
    rec(n + 1, C);
  }
}

bool search(int C) {
  color = vector<int> (N, -1);
  color[0] = 0;
  ok = false;
  rec(1, C);
  return ok;
}

void solve() {
  cin >> N >> M;
  REP(i, M) cin >> from[i];
  REP(i, M) cin >> to[i];  
  
  room.clear();
  {vector<int> v; REP(i, N) v.push_back(i + 1); room.push_back(v);}

  REP(i, M) {
    REP(j, room.size()) {
      vector<int> v = room[j];
      if (count(ALL(v), from[i]) > 0 && count(ALL(v), to[i]) > 0) {
        int a = find(ALL(v), from[i]) - v.begin();
        int b = find(ALL(v),   to[i]) - v.begin();

        vector<int> x, y;
        for (int i = a; i <= b; i++) x.push_back(v[i]);
        for (int i = b; i <= a + v.size(); i++) y.push_back(v[i % v.size()]);
                
        room.erase(room.begin() + j);
        sort(ALL(x));
        sort(ALL(y));
        room.push_back(x);
        room.push_back(y);
        
        break;
      }
    }
  }
  
  ans = 1;
  for (int co = 2; ; co++) {
    if ( search(co) ) {
    } else {
      break;
    }
  }
  
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    
    printf("Case #%d: ", tno);
    solve();
    printf("%d\n", ans);

    REP(i, ans_v.size()) {
      if (i) cout << " ";
      cout << ans_v[i] + 1;
    }
    cout << endl;
  }
  return 0;
}
