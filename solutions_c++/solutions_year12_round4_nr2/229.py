#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

int N, W, L;
ll R[1000];
ll X[1000], Y[1000];
bool collide(int i, int j) {
  ll x = X[i] - X[j], y = Y[i] - Y[j];
  if (x*x + y*y >= (R[i] + R[j]) * (R[i] + R[j])) return false;
  return true;
}
int main() {
  srand((unsigned)time(NULL));
  int tc, cn = 0;
  int i, j;
  cin >> tc;
  while (cn++ < tc) {
    cin >> N >> W >> L;
    vector<p2> list;
    fr (i, N) {
      cin >> R[i];
      list.pb(MP(R[i], i));
    }
    sort(list.rbegin(), list.rend());
    
    do {
      fr (i, N) {
        int trial = 0;
        do {
          X[list[i].S] = rand()%(W + 1);
          Y[list[i].S] = rand()%(L + 1);
          fr (j, i) if (collide(list[i].S, list[j].S)) break;
          if (j == i) break;
        } while (trial++ < 100);
        
        if (trial > 100) {
          break;
        }
      }
    } while (i < N);

    cout << "Case #" << cn << ":";
    for (i = 0; i < N; i++) cout << " " << X[i] << " " << Y[i];
    cout << endl;
  }
  return 0;
}
