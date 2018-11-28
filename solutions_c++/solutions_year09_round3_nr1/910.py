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
typedef unsigned long long LL;

inline void OFILE(string f) {
	string in = f + ".in";
	freopen( in.c_str(), "r", stdin);
	string out = f + ".out.txt";
	freopen( out.c_str(), "w", stdout);
}

char s[100];

int convert(char s) {
	if ( '0' <= s && s <= '9' ) return s-'0';
	else return s-'a'+10;
}

int can(int base, int len) {
	for(int i=0; i<len; i++) {
		//DEBUG(convert(s[i]));
		//DEBUG(s[i]);
		if ( convert(s[i]) >= base ) return 0;
	}
	return 1;
}

LL convert(int base, int len) {
	LL ret = LL(0);
	for(int i=0, _n = len; i<_n; i++, len--) {
		ret += LL((LL(convert(s[i])) * LL(pow(double(base), double(len)-1.0))));
	}
	return ret;
}
int tab[255];
int main() {
	OFILE("A5");
	int ntc;
	scanf("%d", &ntc);
	FOR(TC, 1, ntc) {
		scanf("%s", s);
		int len = strlen(s), idx = 2;
		LL ans = (1LL<<63LL);

		memset(tab,-1,sizeof(tab));
		string ss = "";
		int count=0;
		for(int i=0; i<len; i++) {
			if ( tab[s[i]] == -1 ) {
				count++;
				tab[s[i]] = ( count == 2 ) ? 0 : (count==1) ? 1 : idx++;
				ss.push_back('0' + tab[s[i]]);
			} else {
				ss.push_back('0' + tab[s[i]]);
			}
		}
		sprintf(s, "%s", ss.c_str());
		//puts(s);
	       len = strlen(s);
		for(int i=2; i <= 36; i++) {
			if ( can(i, len) ) ans = min(ans, convert(i, len) );
		}
		printf("Case #%d: %I64d\n", TC, ans);
	}
	// system("pause");
	return 0;
}
