#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int vec[4][2] = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

bool ex[102][102];
int added[200][200];

vector<pair<int, int> > next, toUpdate, tmp;
vector<int> val, valNext;

int main(){
  freopen("Cs.out","wt", stdout);
  freopen("Cs.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  int r;
  int x1, x2, y1, y2;
  FOR (test, tests){
    int ret = 0;
    SET(ex, 0);
    SET(added, 255);
      
    cin >> r;
    FOR (i, r){
      cin >> x1 >> y1 >> x2 >> y2;
      ffor (x, x1, x2 + 1)
        ffor (y, y1, y2 + 1)
          ex[x][y] = true;
    }
    
    ffor (x, 1, 101)
      ffor (y, 1, 101)
        if (ex[x][y] && !ex[x - 1][y] && !ex[x][y - 1]){
          toUpdate.pb(mp(x, y));
          val.pb(0);
        }
        else if (!ex[x][y] && ex[x - 1][y] && ex[x][y - 1]){
          toUpdate.pb(mp(x, y));
          val.pb(1);
        }

    pair<int, int> xy;
    int x, y;
    while (toUpdate.sz){
      ret++;
      
      FOR (i, toUpdate.sz){
        xy = toUpdate[i];
        ex[xy.first][xy.second] = val[i];
      }
      
      next.clear();
      valNext.clear();
      FOR (i, toUpdate.sz){
        xy = toUpdate[i];

        FOR (k, 4){
          x = xy.first + vec[k][0];
          y = xy.second + vec[k][1];
          if (added[x][y] == ret)
            continue;
          if (ex[x][y] && !ex[x - 1][y] && !ex[x][y - 1]){
            next.pb(mp(x, y));
            valNext.pb(0);
            added[x][y] = ret;
          }
          else if (!ex[x][y] && ex[x - 1][y] && ex[x][y - 1]){
            next.pb(mp(x, y));
            valNext.pb(1);
            added[x][y] = ret;
          }
        }
      }
      
      toUpdate.clear();
      val.clear();
      FOR (i, next.sz){
        toUpdate.pb(next[i]);
        val.pb(valNext[i]);
      }
    }
    
    cout << "Case #" << (test + 1) << ": ";
    cout << ret << "\n";    
  }
  return 0;
}
