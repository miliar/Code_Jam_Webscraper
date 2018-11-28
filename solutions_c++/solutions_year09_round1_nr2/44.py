#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <utility>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-8;

struct State {
  int h;
  int w;
  int t;
};

bool operator>(const State& a, const State& b) {
  return a.t > b.t;
}

int nCases;
int H, W;
int SX[24][24];
int WX[24][24];
int CY[24][24];
int ST[24][24];
int WT[24][24];
bool visited[48][48];

int main(){
  cin >> nCases;
  REP(ic, nCases){
    cin >> H >> W;
    REP(h, H){
      REP(w, W){
        int a, b, c;
        cin >> a >> b >> c;
        int cy = a + b;
        int st = c % cy;
        int wt = (c+a) % cy;
        SX[h][w] = a;
        WX[h][w] = b;
        CY[h][w] = cy;
        ST[h][w] = st;
        WT[h][w] = wt;
      }
    }
    priority_queue<State, vector<State>, greater<State> > q;
    while(!q.empty()){
      q.pop();
    }
    State si = {2*H-1, 0, 0};
    q.push(si);
    memset(visited, 0, sizeof(visited));
    const int desth = 0;
    const int destw = 2*W-1;
    int ret = -1;
    while(!q.empty()){
      State s = q.top();
      q.pop();
      if(s.h == desth && s.w == destw){
        ret = s.t;
        break;
      }
      if(visited[s.h][s.w]) continue;
      visited[s.h][s.w] = true;
      int ch = s.h/2;
      int cw = s.w/2;
      int sx = SX[ch][cw];
      int wx = WX[ch][cw];
      int cy = CY[ch][cw];
      int st = ST[ch][cw];
      int wt = WT[ch][cw];
      int cost;
      if(s.w > 0 && !visited[s.h][s.w-1]){
        if(s.w & 1){
          int xc = s.t / cy;
          int p = s.t % cy;
          int penalty;
          if(st < wt){
            if(p < st || p >= wt){
              penalty = 0;
            }else{
              penalty = wt-p;
            }
          }else{
            if(p >= wt && p < st){
              penalty = 0;
            }else{
              penalty = (wt+cy-p)%cy;
            }
          }
          cost = 1 + penalty;
        }else{
          cost = 2;
        }
        State sx = {s.h, s.w-1, s.t+cost};
        q.push(sx);
      }
      if(s.w < 2*W-1 && !visited[s.h][s.w+1]){
        if((s.w & 1) == 0){
          int xc = s.t / cy;
          int p = s.t % cy;
          int penalty;
          if(st < wt){
            if(p < st || p >= wt){
              penalty = 0;
            }else{
              penalty = wt-p;
            }
          }else{
            if(p >= wt && p < st){
              penalty = 0;
            }else{
              penalty = (wt+cy-p)%cy;
            }
          }
          cost = 1 + penalty;
        }else{
          cost = 2;
        }
        State sx = {s.h, s.w+1, s.t+cost};
        q.push(sx);
      }
      if(s.h > 0 && !visited[s.h-1][s.w]){
        if(s.h & 1){
          int xc = s.t / cy;
          int p = s.t % cy;
          int penalty;
          if(wt < st){
            if(p < wt || p >= st){
              penalty = 0;
            }else{
              penalty = st-p;
            }
          }else{
            if(p >= st && p < wt){
              penalty = 0;
            }else{
              penalty = (st+cy-p)%cy;
            }
          }
          cost = 1 + penalty;
        }else{
          cost = 2;
        }
        State sx = {s.h-1, s.w, s.t+cost};
        q.push(sx);
      }
      if(s.h < 2*H-1 && !visited[s.h+1][s.w]){
        if((s.h & 1) == 0){
          int xc = s.t / cy;
          int p = s.t % cy;
          int penalty;
          if(wt < st){
            if(p < wt || p >= st){
              penalty = 0;
            }else{
              penalty = st-p;
            }
          }else{
            if(p >= st && p < wt){
              penalty = 0;
            }else{
              penalty = (st+cy-p)%cy;
            }
          }
          cost = 1 + penalty;
        }else{
          cost = 2;
        }
        State sx = {s.h+1, s.w, s.t+cost};
        q.push(sx);
      }
    }
    cout << "Case #" << ic+1 << ": " << ret << endl;
  }

  return 0;
}

