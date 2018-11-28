#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define DBGV(_v) { REP(_i, _v.size()) { cout << _v[_i] << "\t";} cout << endl;} 
typedef pair<int,int> PII;
#define INF (int)1e6
#define sz size()
string s2 = "welcome to code jam";
int res;

int go(string s, int n) {
	if (n == 18) {
		if (res > 10000) res%=10000;
		REP(i, s.sz) if (s[i] == 'm') res++;
	}
	
	if ( s== "") return 0;

	//cout << s << "\t" << n << "\t" << s2[n] << endl;		
	REP(i, s.size()) {
		if (s[i] == s2[n]) {
			go(s.substr(i+1), n+1);	
		}
	}
}

int main() {
	int kases;
	cin >> kases;
	cin.ignore();
	string s1;
	REP(kase, kases) {
		res = 0;
		getline(cin, s1);
		go(s1, 0);			
		printf("Case #%d: %04d\n", kase+1, res%1000);
	}
	return 0;  
}
