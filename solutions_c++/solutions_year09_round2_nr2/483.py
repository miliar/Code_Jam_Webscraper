#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <cstring>
#include <map>
#include <sstream>
#include <cstdlib>
#include <cassert>
#include <algorithm>

using namespace std;

#define LET(a,x) typeof(x) a(x)
#define FOR(x,a,b) for(LET(x,a);x!=b;x++)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,v.begin(),v.end())
#define DBG(x) cerr << #x << "-->"<<x<<"; "
#define DBE(x) cerr << #x << "-->"<<x<<";\n"
#define sz size()
#define pb push_back
#define SET0(a) memset(a,0,sizeof(a))
#define SET1(a) memset(a,-1,sizeof(a))

const int INF = (int)1e9;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define GI ({int t; scanf(" %d",&t); t;})

map<int,int> getdig(string s) {
    map<int,int> M;
    REP(i,s.sz)
	M[s[i]-'0'] ++;
    return M;
}

bool desc(string s) {
    REP(i,s.sz-1)
	if(s[i] < s[i+1])
	    return false;
    return true;
}

string doit(string s) {
    int N = s.sz;
    map<int,int> dig = getdig(s);
    if (desc(s)) {
	string r = "";
	dig[0] ++;
	EACH(x, dig)
	    REP(i, x->second)
	       r += '0' + x->first;
	if (r[0] == '0') {
	    REP(i, r.sz) if(r[i] != '0') {
		swap(r[0], r[i]);
		break;
	    }
	}
	return r;
    }
    else {
	for(int i=s.sz-2; i>=0; i--) {
	    int least = 1000, m = -1;
	    for(int j=i+1; j<s.sz; j++)
		if (least > s[j] and s[j] > s[i]) {
		    least = s[j];
		    m = j;
		}
	    if (m != -1) {
		swap(s[m], s[i]);
		sort(s.begin()+i+1,s.end());
		return s;
	    }
	}
	assert(0);
    }
}


int main() {
    int T = GI;
    REP(kase, T) {
	string s;
	cin >> s;
	cout << "Case #" << kase+1 << ": " << doit(s) << endl;

    }
    return 0;
}
