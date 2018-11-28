// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cassert>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 

const int MAXN = 200;
int main() {
	int ile, n, time;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
    scanf("%d",&n);
    char who[MAXN];
    int position[MAXN];
    REP(i, n) {
      scanf("%c%c%d", &who[i], &who[i], &position[i]);
    }
    time = 0;
    int pNext, pC = 1, pO = 1;
    bool done = false;
		REP(i, n) {
        if (who[i] == 'O') {
          FOR(j, i + 1, n - 1) if (who[j] == 'B') {
            pNext = j;
            break;
          }
          done = false;

          while (!done) {
            time++;
            if (position[i] != pO) {
              if (position[i] > pO) {
                pO++;
              } else {
                pO--;
              }
            } else {
              done = true;
            }
            if (position[pNext] != pC) {
              if (position[pNext] > pC) {
                pC++;
              } else {
                pC--;
              }
            }
          }
        } else {
          FOR(j, i + 1, n - 1) if (who[j] == 'O') {
            pNext = j;
            break;
          }
          done = false;

          while (!done) {
            time++;
            if (position[i] != pC) {
              if (position[i] > pC) {
                pC++;
              } else {
                pC--;
              }
            } else {
              done = true;
            }
            if (position[pNext] != pO) {
              if (position[pNext] > pO) {
                pO++;
              } else {
                pO--;
              }
            }
          }
        }
    }
    printf("Case #%d: %d\n",iile, time);
	}
	return 0;
}

