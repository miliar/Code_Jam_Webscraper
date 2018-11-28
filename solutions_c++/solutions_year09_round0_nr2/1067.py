#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <cstdio>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

const int ADJ[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

struct Cell {
  int alt;
  char label;
  char srcdir;
};

Cell map[104][104];
vector<pair<int, int> > sink;
int h, w;

int nMaps;

int main(){
  cin >> nMaps;
  REP(nc, nMaps){
    memset(map, -1, sizeof(map));
    sink.clear();
    cin >> h >> w;
    REP(i, h){
      REP(j, w){
        int x;
        cin >> x;
        map[i+1][j+1].alt = x;
        map[i+1][j+1].srcdir = 0;
      }
    }
    REP(i, h){
      REP(j, w){
        Cell& c = map[i+1][j+1];
        int minalt = 1000000;
        REP(dir, 4){
          int xi = i+1+ADJ[dir][0];
          int yi = j+1+ADJ[dir][1];
          Cell& ox = map[xi][yi];
          if(ox.alt != -1 && c.alt > ox.alt){
            minalt = min(minalt, ox.alt);
          }
        }
        if(minalt > 100000){
          sink.push_back(make_pair(i+1, j+1));
          continue;
        }
        REP(dir, 4){
          int xi = i+1+ADJ[dir][0];
          int yi = j+1+ADJ[dir][1];
          Cell& ox = map[xi][yi];
          if(ox.alt == minalt){
            ox.srcdir |= 1 << dir;
            break;
          }
        }
      }
    }
    REP(i, sink.size()){
      queue<pair<int, int> > q;
      q.push(sink[i]);
      while(!q.empty()){
        pair<int, int> x = q.front();
        q.pop();
        int xi = x.first;
        int xj = x.second;
        Cell& c = map[xi][xj];
        c.label = i;
        REP(dir, 4){
          if(c.srcdir & (1 << dir)){
            int ni = xi - ADJ[dir][0];
            int nj = xj - ADJ[dir][1];
            q.push(make_pair(ni, nj));
          }
        }
      }
    }
    REP(i, sink.size()){
      int color = -1;
      REP(j, h){
        REP(k, w){
          Cell& c = map[j+1][k+1];
          if(color == -1 && c.label < 'a'){
            color = c.label;
          }
          if(c.label == color){
            c.label = 'a'+i;
          }
        }
      }
    }
    cout << "Case #" << nc+1 << ":" << endl;
    REP(i, h){
      REP(j, w){
        if(j > 0){
          cout << ' ';
        }
        cout << map[i+1][j+1].label;
      }
      cout << endl;
    }
  }

  return 0;
}

