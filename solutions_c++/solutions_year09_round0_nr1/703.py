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

typedef vector<string> vs;

vs parsePattern (string P) {
	vs res;
	int ps = P.size(), loc = 0;
	do {
	  string s = "";
	  if (P[loc] == '(') {
	  	++loc; while (loc < ps && P[loc] != ')') { s += P[loc]; ++loc; }
	  } else {
	  	s = P[loc];
	  }
	  res.PB(s);
	  ++loc;
	} while (loc < ps);
	return res;
}

int main() {

  int L,D,N;
  string W[5005];
  string P;

  scanf("%d %d %d\n",&L,&D,&N);
  FORU(i,1,D) {
  	getline(cin, W[i]);
  }

  FORU(testcase,1,N) {
    int ans = 0;
    getline(cin, P);
    vs pat = parsePattern(P);
    FORU(i,1,D) {
    	bool match = true;
    	FORU(j,0,L-1) {
    		if (pat[j].find(W[i][j]) == string::npos) {
    			match = false; break;
    		}
    	}
    	if (match) ++ans;
    }
    printf("Case #%d: %d\n",testcase,ans);
  }

  return 0;
}
