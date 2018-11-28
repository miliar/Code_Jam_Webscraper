#include <map>
#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define PB push_back

typedef vector<string> VS;
template<class T> inline int size(const T&c) { return c.size(); }
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}
template<class A,class B> inline bool contains(const A&a, const B&b) { return find(ALL(a),b)!=a.end(); }

inline VS split(string s,string delim=" ")
{
	VS ret; string temp=""; s+=delim;
	REP(i,size(s))
		if(!contains(delim,s[i])) temp+=s[i];
		else if(temp!="") { ret.PB(temp); temp=""; }
  	return ret;
}

// Powered By TimoAI 2.2

map< string, int > dir;
char input[128];

inline int doit(string s) {
	VS vs = split(s,"/");
	int ret = 0;
	// cout << s << endl;
	int level = 0;
	string curr = "";
	FOR(i,0,size(vs)-1) {
		curr += "/" + vs[i];
		// cout << curr << endl;
		if(dir[curr]==0) {
			dir[curr] = 1;
			ret++;
		}
	}
	return ret;
}

int main() {
	OPEN("a");
	REP(ncase,getint()) {

		dir.clear();

		int n=getint();
		int m=getint();
		REP(i,n) {
			scanf("%s",input);
			doit(input);
		}
		int ans = 0;
		REP(i,m) {
			scanf("%s",input);
			ans += doit(input);
		}
		printf("Case #%d: %d\n",ncase+1,ans);
	}
	return 0;
}
