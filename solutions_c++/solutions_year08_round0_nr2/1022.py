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
#define cs c_str()
#define MAX 10000
typedef vector <int> VI;
typedef vector <string> VS;
#define DBGV(x) REP(_i, x.sz) cout << x[_i] << "\t"; cout << endl;

int minutes(string s) {
	int hr, min;
	sscanf(s.cs, "%d:%d", &hr, &min);
	return (hr*60+min);
}

int main() {
	int cases = GI;
	REP(cnt, cases) {
		int a=0, b=0;
		VI depa, depb, arra, arrb;
		int turn = GI;
		int na = GI, nb = GI;
		string arr, dep;
		REP(i, na) {
			cin >> dep >> arr;
			depa.pb(minutes(dep));
			arrb.pb(minutes(arr)+turn);
		}
		REP(i, nb) {
			cin >> dep >> arr;
			depb.pb(minutes(dep));
			arra.pb(minutes(arr)+turn);
		}
		sort(arra.begin(), arra.end());
		sort(arrb.begin(), arrb.end());
		sort(depa.begin(), depa.end());
		sort(depb.begin(), depb.end());
		int pos = 0;
		REP(i, depa.sz) {
			if (arra.sz > pos && depa[i]>=arra[pos]) {
				pos++;
			}
			else {
				a++;
			}
		}
		pos = 0;
		REP(i, depb.sz) {
			if (arrb.sz > pos && depb[i]>=arrb[pos]) {
				pos++;
			}
			else {
				b++;
			}
		}		
		cout << "Case #"<<(cnt+1)<<": "<<a<<" "<<b<<"\n";
	}
	return 0;
}
