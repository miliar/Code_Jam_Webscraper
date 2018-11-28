#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(x,v) FOR(x,(v).begin(),(v).end())
#define sz size()
#define pb push_back
#define DBG(x) cout<< #x << " --> "<< x << "\t"
#define DBE(x) cout<< #x << " --> "<< x << "\n"
#define GI() ({int; scanf(" %d", &t); t;})
typedef pair<int,int> PII;
typedef long long LL;

#define findclose(tt,j) ( {int t; \
	    for (t = j+1; tt[t] != ')'; t++ ); \
	    t; } )

int main() {
    int L, D, N;
    cin >> L >> D >> N;
    string s;
    vector<string> w;
    REP(i,D) {
	cin >> s;
	w.pb(s);
    }
    sort(w.begin(), w.end());
    REP(i,N) {
	int j=0;
	string st; cin >> st;
	vector<string> wc = w;
	REP(ii, L) {	    
	    string ch;
	    if (st[j] == '(') {
		int k = findclose(st,j);
		ch = st.substr(j+1, k-(j+1));
		j = k+1;
	    }
	    else ch = st[j++];
	    vector<string> tp;
	    REP(j, wc.sz) 
		if(find(ch.begin(), ch.end(), wc[j][ii]) != ch.end())
		    tp.pb(wc[j]);
	    wc = tp;
	}
	cout << "Case #" << i+1 << ": " << wc.sz << endl;
    }
    
    return 0;
}
