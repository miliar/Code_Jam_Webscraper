#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n)  for(int i=0;i<(int)(n);++i)
#define REPD(i,n)  for(int i=(int)(n)-1;i>=0;--i)
#define FOR(i,L,R) for(int i=(int)(L);i<=(int)(R);++i)
#define FORD(i,L,R) for(int i=(int)(R);i>=(int)(L);--i)
#define FOREACH(it,n) for(it = (n).begin(); it != (n).end(); ++it) // __typeof((n).begin()) 
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))

typedef vector< int >     vi;
typedef vector< vi >      vii;
typedef pair< int, int >  pii;
typedef vector< pii >     vpii;
typedef vector< string >  vs;
//typedef long long         i64;
typedef unsigned long     ul;

//const string F = "test";
//const string F = "A-small-attempt0";
const string F = "A-large";
string IN  = F + ".in";
string OUT = F + ".out";

template<class T>
static std::string tostring(T val) {
    std::ostringstream stream;
    stream << val;
    return stream.str();
}

vs parse(string s) {
	vs res;
	bool first = true;
	string tmp = "";
	REP(i,sz(s)) {
		if (s[i] == '/' && first == false) {
			res.pb(tmp);
			tmp = "";
		}
		else {
			if (s[i] == '/')
				first = false;
			else tmp+=s[i];
		}
	}
	if (tmp != "")
		res.pb(tmp);
	return res;
}

void solve(int t) {

	set<string> ROOT;

	int N, M;
	cin >> N >> M;
	REP(i,N) {
		string tmp;
		cin >> tmp;
		vs a = parse(tmp);
		string b = "";
		REP(j,sz(a)) {
			b += "/" + a[j];
			ROOT.insert(b);			
		}
	}

	int res = 0;
	REP(i,M) {
		string tmp;
		cin >> tmp;
		vs a = parse(tmp);
		string b = "";
		REP(j,sz(a)) {
			b += "/" + a[j];
			if (ROOT.find(b) == ROOT.end()) {
				ROOT.insert(b);
				res++;
			}
		}
	}

	cout << "Case #" << t <<": " << res << "\n";
	int kk = 1;
}

int main() {
	freopen(IN.c_str(), "rt", stdin); 
	freopen(OUT.c_str(), "wt", stdout);

	int T;
	cin >> T;
	//scanf("%d",&T);
	FOR(t,1,T)
		solve(t);
	return 0;
}




