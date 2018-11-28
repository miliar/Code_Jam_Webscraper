#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define DBG(x) cout<< #x << " --> "<< x << "\t"
#define DBE(x) cout<< #x << " --> "<< x << "\n"
#define GI ({int t; scanf(" %d", &t); t;})
typedef pair<int,int> PII;
typedef long long LL;

using namespace std;

int main() {
  int T = GI;
  REP(kase, T) {
    int N = GI, K = GI;
    vector<string> V;
    REP(i, N) {
      string s;
      cin >> s;
      V.pb(s);
    }
    vector<string> S = V;
    //REP(i, N) cout << V[i] << "\n"; cout << endl;
    REP(i, N) REP(j, N) {
      S[i][j] = V[N-j-1][i];
    }
    //REP(i, N) cout << S[i] << "\n"; cout << endl;
    REP(i, N) {
      bool ok = true;
      while(ok) {
	ok = false;
	REP(j, N-1) if (S[j][i] != '.' and S[j+1][i] == '.') {
	  S[j+1][i] = S[j][i];
	  S[j][i] = '.';
	  ok = true;
	}
      }
    }
    //REP(i, N) cout << S[i] << "\n"; cout << endl;
    bool red = false, blue = false;
    REP(i, N) REP(j, N) {
      int x = i, y = j;
      int dx[] = {0, 1, -1, 1};
      int dy[] = {1, 0, 1, 1};
      REP(ii, 4) {
	int ok = 0;
#define OK(a) (0<=a and a<N)
	FOR(k, 1, K) {
	  if (OK(x + k*dx[ii]) and OK(y+k*dy[ii])
	      and S[x + k*dx[ii]][y+k*dy[ii]] == S[x][y])
	    ok++;
	}
	if (ok == K-1) {
	  if (S[x][y] == 'R') red = true;
	  else if (S[x][y] == 'B') blue = true;
	}	
      }      
    }

    printf("Case #%d: ", kase+1);
    if (red and blue)
      printf("Both\n");
    else if (!red and !blue)
      printf("Neither\n");
    else if (red)
      printf("Red\n");
    else
      printf("Blue\n");
	

  }

  
  return 0;
}
