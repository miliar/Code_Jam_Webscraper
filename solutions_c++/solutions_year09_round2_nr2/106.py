// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
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
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

char buf[50];
string read() {
	scanf("%s",buf);
	return buf;
}

void przerob(string &s) {
	sort(ALL(s));
	int i;
	for(i=0;s[i]=='0';++i);
	swap(s[0],s[i]);
}

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		printf("Case #%d: ",tc);
		string s=read();
		if(next_permutation(ALL(s))) {
			printf("%s\n",s.c_str());
			continue;
		} else {
			s+='0';
			przerob(s);
			printf("%s\n",s.c_str());
		}
	}
	return 0;
}
