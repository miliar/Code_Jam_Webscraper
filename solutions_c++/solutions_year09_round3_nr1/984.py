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

vs split (string s, string del = " ") { vs res;
	int ss = SIZE(s), sdel = SIZE(del);
	for (int p = 0, q; p < ss; p = q+sdel) {
		if ((q = s.find(del, p)) == (signed)string::npos) q = ss;
		if (q-p>0) res.PB(s.substr(p,q-p));
	} return res;
}

Int base2dec (string const& num, int base = 10) {
  long sign = (num[0] == '-') ? 1 : 0, res = 0;
  Int s = 0LL, e = num.length()-1;
  if (sign) ++s;
  FORU(i,s,e) {
    res *= base;
    res += (num[i]<'a') ? (num[i]-'0') : (num[i]-'a'+10);
  }
  if (sign) res = -res;
  return res;
}

int main() {

  int T;
  string line;

  scanf("%d\n",&T);
  FORU(testcase,1,T) {
  	Int ans = 0LL;
  	set<char> S;
  	getline(cin, line);
  	bool found = true;
  	FORU(i,0,line.size()-1) {
  		S.insert(line[i]);
  	}

  	int base = S.size(); if (base == 1) ++base;
		map<char, char> m; m.clear();

  	// cout << line << " " << base << " ";

  	char d = '0';
		bool oneused = false;
		FORU(i,0,line.size()-1) {
			if (m.find(line[i]) != END(m)) {
				line[i] = m[line[i]];
			} else {
				if (i == 0 && d == '0') {
					m.insert(MP(line[i], '1'));
					line[i] = '1'; oneused = true;
				} else {
					m.insert(MP(line[i], d));
					line[i] = d;
					++d; if (d == '1' && oneused) ++d;
				}
			}
		}

  	// cout << line << endl;
  	ans = base2dec(line, base);
    printf("Case #%d: %lld\n",testcase,ans);
  }

  return 0;
}
