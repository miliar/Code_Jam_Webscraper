#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>
#include <queue>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

#define ci(c) ((c)=='O'?0:1)
#define anotheri(c) ((c)==0?1:0)

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    int n;
    cin >> n;
    int i,j;
    queue< pair<int, int> > all;
    vector< queue<int> > next(2, queue<int>());
    REP(i,n){
      char color;
      int pos;
      cin >> color >> pos;
      int colori = ci(color);
      next[colori].push(pos);
      all.push(make_pair(colori, pos));
    }
    map<int, int> pos;
    pos[0] = 1;
    pos[1] = 1;
    int r=0;
    while(!all.empty()){
      pair<char, int> nextpair=all.front();
      int nc = nextpair.first;
      int np = nextpair.second;
      // move nc
      int turn = abs(pos[nc]-np)+1;
      pos[nc] = np;
      next[nc].pop();

      int another = anotheri(nc);
      queue<int> aq = next[another];
      if(pos[another] > aq.front()){
        pos[another] -= min(pos[another]-aq.front(), turn);
      } else if(pos[another] < aq.front()){
        pos[another] += min(aq.front()-pos[another], turn);
      }
      all.pop();
      r+=turn;
    }
    gp(r);
  }
  return 0;
}

