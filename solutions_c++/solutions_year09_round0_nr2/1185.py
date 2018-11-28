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


char mark(int x, int y, VVI &map, VS &ret, char &c) {
/*  cerr << x << " " << y << " " << c << endl;
  for(int i = 0; i < ret.size(); i++) cerr << ret[i] << endl;
  cerr << "=======" << endl;
*/
  int H = map.size();
  int W = map[0].size();
  int nextx = x, nexty = y;
  if(y > 0) if(map[y-1][x] < map[nexty][nextx]) {nextx = x; nexty = y-1;}
  if(x > 0) if(map[y][x-1] < map[nexty][nextx]) {nextx = x-1; nexty = y;}
  if(x < W-1) if(map[y][x+1] < map[nexty][nextx]) {nextx = x+1; nexty = y;}
  if(y < H-1) if(map[y+1][x] < map[nexty][nextx]) {nextx = x; nexty = y+1;}
  if(ret[nexty][nextx] != ' ') ret[y][x] = ret[nexty][nextx];
  else if(nextx == x && nexty == y) ret[y][x] = ++c;
  else ret[y][x] = mark(nextx, nexty, map, ret, c);


  
  return ret[y][x];


}


VS compute(VVI map) {
  int H = map.size();
  int W = map[0].size();
  VS ret(H, string(W, ' '));
  char c = 'a'-1;

//  cerr << H << " " << W << endl;

  for(int y = 0; y < H; y++)
    for(int x = 0; x < W; x++) {
  //    cerr << "#" << x << " " << y << " " << ret[y][x] << " " << (ret[y][x] == ' ') << endl;
      if(ret[y][x] == ' ') mark(x, y, map, ret, c);
    }
  return ret;
}


int main() {
  cout.precision(16);
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int H, W;
    cin >> H >> W;
    VVI map;
    for(int i = 0; i < H; i++) {
      VI line(W);
      for(int j = 0; j < W; j++) cin >> line[j];
      map.pb(line);
    }
    VS ret = compute(map);
    cout << "Case #" << t << ": " << endl;
    for(int i = 0; i < H; i++) {
      for(int j = 0; j < W; j++) cout << ret[i][j] << " ";
      cout << endl;
    }

  }
}
