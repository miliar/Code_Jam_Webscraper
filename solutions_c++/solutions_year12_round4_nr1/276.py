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

int N, Dis[10000], Len[10000], Des;
int DP[10000];
int main() {
  int tc, cn = 0, i, j;
  scanf("%d", &tc);
  while (cn++ < tc) {
    scanf("%d", &N);
    fr (i, N) scanf("%d%d", &Dis[i], &Len[i]);
    scanf("%d", &Des);

    int ok = false;
    memset(DP, 255, sizeof(DP));
    DP[0] = Dis[0];
    fr (i, N) if (DP[i] != -1) {
      if (Dis[i] + DP[i] >= Des) {
        ok = true;
        break;
      }

      for (j = i + 1; j < N; j++) {
        if (Dis[i] + DP[i] < Dis[j]) break;
        int tmp = min(Len[j], Dis[j] - Dis[i]);
        if (DP[j] == -1 || DP[j] < tmp) DP[j] = tmp;
      }
    }

    cout << "Case #" << cn << ": " << (ok ? "YES" : "NO") << endl;
  }
  return 0;
}
