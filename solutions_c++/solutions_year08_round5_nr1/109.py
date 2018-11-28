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




int main() {
  cout.precision(16);
  int N;
  cin >> N;
  
  int* T[6010];
  REP(i, 6010) T[i] = new int[6010];

  for(int i = 1; i <= N; i++) {
    int L;
    cin >> L;

    REP(a, 6010)
      memset(T[a], 0, sizeof(int)*6010);
    int X = 3005, Y = 3005, d = 0;

    REP(j, L) {
      string S; int nb;
      cin >> S >> nb;
      REP(a, nb) REP(k, S.len) {
        if(S[k] == 'F') {
          T[X][Y] = d+1;
          if(d == 0) Y++;
          if(d == 1) X--;
          if(d == 2) Y--;
          if(d == 3) X++;
        }
        else if(S[k] == 'L') {
          d = (d + 1)%4;
        }
        else {
          d = (d + 3)%4;
        }
      }
    }
/*
    for(int y = 3000; y < 3020; y++) {
    for(int x = 3000; x < 3020; x++)
      cout << T[x][y] << " ";
      cout << endl;
    }
    cout << endl;
*/

    int nb;
    REP(x, 6009) {
      nb = 0;
      int last = 0;
      REP(y, 6009) {
      if((T[x][y] & 7) == 4 || (T[x+1][y] & 7) == 2) {
        nb++;
        if(nb % 2 == 0) last = y;
        else if(nb != 1) for(int k = last; k < y; k++) T[x][k] |= 8;
        }
      }
    }
    REP(y, 6009) {
      nb = 0;
      int last = 0;
      REP(x, 6009) {
      if((T[x][y] & 7) == 1 || (T[x][y+1] & 7) == 3) {
        nb++;
        if(nb % 2 == 0) last = x;
        else if(nb != 1) for(int k = last; k < x; k++) T[k][y] |= 8;
        }
      }
    }

/*
    for(int y = 3000; y < 3020; y++) {
    for(int x = 3000; x < 3020; x++)
      cout << T[x][y] << " ";
      cout << endl;
    }
    cout << endl;


*/
    int S = 0;
    REP(y, 6009) REP(x, 6009) if(T[x][y] & 8) S++;

    cout << "Case #" << i << ": " << S << endl;
  }
}
