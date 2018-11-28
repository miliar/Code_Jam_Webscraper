#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<algorithm>
#include<functional>
#include<map>
#include<set>
#include<utility>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

using namespace std;

#define FOR(i,s,n) for (int i=(int)(s); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(), (c).end()
const int inf(1<<24);

int N, M;
bool V;

struct node {
  int gate, changable, value;
  node(int g=0, int c=0, int v=0) : gate(g), changable(c), value(v) {}
};
vector<node> btree;

bool eval(int pos = 0)
{
  //cerr << pos << " " << btree[pos].value << endl;
  if ((pos+1)*2-1 >= M) return btree[pos].value;

  bool left  = eval((pos+1)*2-1);
  bool right = eval((pos+1)*2);
  return btree[pos].gate ? (left && right) : (left || right);
}

int dfs(int depth = 0, int changed = 0, int ans = inf)
{
  if (depth >= (M-1)/2) {
    bool t = eval();
    //cerr << "$ " << t << ":" << V << " " << changed << endl;
    return ((t == V) ? min(ans, changed) : ans);
  }
  
  ans = min(ans, dfs(depth+1, changed, ans));
  if (btree[depth].changable) {
    int g = btree[depth].gate;
    btree[depth].gate = g ? 0 : 1;
    ans = min(ans, dfs(depth+1, changed+1, ans));
    btree[depth].gate = g;
  }
  
  return ans;
}

int main()
{
  cin >> N;
  REP(i, N) {
    cin >> M >> V;
    //cerr << "# " << N << " " << M << " " << V << endl;
    btree.resize(M);
    REP(j, (M-1)/2) {
      cin >> btree[j].gate >> btree[j].changable;
    }
    REP(j, (M+1)/2) {
      cin >> btree[(M-1)/2+j].value;
    }
    
    int ans = dfs();
    
    cout << "Case #" << i+1 << ": ";
    if (ans == inf)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << ans << endl;
  }
  return 0;
}
