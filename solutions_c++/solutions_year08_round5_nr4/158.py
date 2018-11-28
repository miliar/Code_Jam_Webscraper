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

int Tab[200][200];
int W, H;

int solve(int x, int y) {
  if(Tab[x][y] != -1) return Tab[x][y];
  if(x > W || y > H) return 0;

  int nb1 = solve(x+1, y+2);
  int nb2 = solve(x+2, y+1);

  Tab[x][y] = (nb1 + nb2) % 10007;
  return Tab[x][y];



}


int main() {
  cout.precision(16);
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    memset(Tab, -1, sizeof(Tab));
    int R;
    cin >> H >> W >> R;
    Tab[W][H] = 1;
    REP(k, R) {
      int X, Y;
      cin >> Y >> X;
      Tab[X][Y] = 0;
    }

    cout << "Case #" << i << ": " << solve(1,1) << endl;

  }
}
