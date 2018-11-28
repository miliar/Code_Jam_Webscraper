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
#define CLR(c) memset(c, 0, sizeof(c))
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

typedef vector<int> vi;
typedef vector<string> vs;

template <class T> inline string toString (const T& t) {
  stringstream ss; ss << t; return ss.str();
}

unsigned long s2i (string &s) {
  unsigned long res = 0, n = s.size(), i = 0, pow = 1<<(n-1);
  while (i < n) {
    res += (s[i]&1) ? pow : 0;
    ++i; pow >>= 1;
  }
  return res;
}

int main() {

  int T;
  Int start, N;

  scanf("%d\n",&T);
  FORU(testcase,1,T) {
  	cin >> N; start = N;
  	int res = 1000000000;

  	while (res == 1000000000) {
  	  string sN = toString(N);
  	  sort (sN.begin(), sN.end());

		  do {
			  long num = atol(sN.c_str());
			  // cout << sN << " " << num << endl;
			  if (num > start && num < res) res = num;
		  } while (next_permutation(sN.begin(), sN.end()));

		  if (res == 1000000000) { N *= 10; }
  	}

    printf("Case #%d: %ld\n",testcase,res);
  }

  return 0;
}
