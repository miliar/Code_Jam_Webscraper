#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<cstring>

// Felix J's AI v1.0
#define FOR(i,a,b) for(int i=(a),_n=(b); i<=_n; i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n; i--)
#define FILL(i,v) memset((i),(v),sizeof((i)))
#define DEBUG(x) cout << "  >> " << #x << " => " << x <<endl

using namespace std;
typedef long long LL;

inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

int main() {
	int ntc;
	OPEN("Blarge");
	scanf("%d", &ntc);
	FOR(TC,1,ntc) {
		char s[30];
		scanf("%s", s);
		string x = "0";
		x = x + s;
		sprintf(s, "%s", x.c_str());
		next_permutation(s,s+strlen(s));
		printf("Case #%d: ", TC);
		int idx = -1, _len = strlen(s);
		while(++idx < _len && s[idx] == '0' );
		printf("%s\n", s+idx);
	}
	return 0;
}
