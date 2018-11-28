#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#define Int signed long long int  /* 64b Unix : %lld , %llu  */
// #define Int __int64            /* 64b win  : %I64d, %I64u */

// #define DEBUG
#define DB(x) { cout << __LINE__ << ": " << #x << " " << x << endl; }
#define HERE { cout << "HERE\n"; }

#define INF 1000000000

#define MP make_pair
#define PB push_back
#define ST first
#define ND second
#define NL printf("\n");
#define RET return
#define sqr(x) ((x)*(x))
#define myabs(x) (((x)<0)?(-(x)):(x))

#define VAR(a,T) __typeof(T) a=(T)
#define BEG(c) (c).begin()
#define BEGR(c) (c).rbegin()
#define END(c) (c).end()
#define ENDR(c) (c).rend()
#define ALL(c) BEG(c), END(c)
#define POS(c,x) ((c).find(x) != END(c))
#define CLEAR(a, v, b) memset(a, v, b)
#define REVERSE(c) reverse(ALL(c))
#define SORT(c) sort(ALL(c))
#define SIZE(c) ((int) (c).size())
#define SSORT(c) stable_sort(ALL(c))
#define REP(i,e) for(int i = 0; i < (e); ++i)
#define FORU(i,b,e) for(int i = (b); i <= (signed)(e); ++i)
#define FORD(i,b,e) for(int i = (b); i >= (signed)(e); --i)
#define VELU(it,c) for(VAR(it, BEG(c)); it != END(c); ++it)
#define VELD(it,c) for(VAR(it, BEGR(c)); it != ENDR(c); ++it)
#define TLE FORU(yy,0,1000000000) FORU(xx,0,1000000000) cout << "\n";

int main() {

  int N;
  string line;
  string p = "welcome to code jam";
  int C [20][505];

  scanf("%d\n",&N);
  FORU(testcase,1,N) {
    getline(cin, line);

    if (line.size() < 19) {
    	printf("Case #%d: %04d\n",testcase,0);
    } else {
    	int L = line.size();

      FORU(r,0,19) memset(C[r], 0, (1+L)*sizeof(int));

      FORU(r,1,19) {
      	FORU(c,r,L) {
      		C[r][c] = C[r][c-1];
      		if (p[r-1] == line[c-1]) {
      			if (r == 1) C[r][c] += 1; else C[r][c] += C[r-1][c];
      			C[r][c] %= 10000;
      		}
      	}
      }

      /*
      FORU(r,0,19) {
				FORU(c,0,L) {
					cout << C[r][c] << " ";
				} cout << endl;
			}
			*/

      printf("Case #%d: %04d\n",testcase,C[19][L]);
    }

  }

  return 0;
}
