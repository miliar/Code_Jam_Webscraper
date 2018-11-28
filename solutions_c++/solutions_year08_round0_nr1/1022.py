#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>

using namespace std;
#define DBGV(x) REP(_i, x.sz) cout << x[_i] << "\t"; cout << endl;
#define LET(x,a) __typeof(a) x(a)
#define IFOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define EACH(it,v) IFOR(it,(v).begin(),(v).end())
#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define COUNT(f,x) ({int _=0;f _+=(x);_;})
#define EXISTS(f,x) ({int _=0;f if(x) {_=1;break;}_;})
#define ALL(f,x) (!EXISTS(f,!(x)))
#define GI ({int t;scanf("%d",&t);t;})
#define INF (int)1e8
#define MEM(a) memset(a, 0, sizeof(a));
#define sz size()
#define pb push_back
#define cs c_str
#define MAX 10000
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int,int> PII;

int main() {
	int cases = GI;
	string tmp;	
	REP(cnt, cases) {
		VS q;
		int res = 0;
		map <string, int> e;
		int ecnt = GI;
		getline(cin, tmp);
		REP(i, ecnt) {
			getline(cin, tmp);
			e[tmp] = i;
		}
		
		int qcnt = GI;
		getline(cin, tmp);		
		REP(i, qcnt) {
			getline(cin, tmp);
			q.pb(tmp);
		}
		/*
		for(map<string,int>::iterator i=e.begin();i!=e.end();++i)
			cout << i->first << " => " << i->second << endl;
		cout << "Queries...\n";
		DBGV(q);
		*/
		vector <bool> flag(e.sz, true);
		REP(i, q.sz) {
			flag[e[q[i]]] = false;
			if (ALL(REP(j, flag.sz), flag[j]==false)) {
				//cout << q[i] << "\t" <<e[q[i]] << endl;
				res++;
				REP(k, flag.sz) flag[k] = true;
				flag[e[q[i]]] = false;
			}
		}
		//DBGV(flag);
		cout << "Case #"<<(cnt+1)<<": "<<res<<"" << endl;	
	}
	return 0;
}
