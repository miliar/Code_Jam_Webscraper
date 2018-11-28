#include<iostream>
#include<fstream>

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <ctime>
#include <sys/time.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
template<class T> inline int size(const T& c) { return c.sz; }
#define FORA(i,c) REP(i,size(c))
#define itype(c) __typeof((c).begin())
#define FORE(e,c) for(itype(c) e=(c).begin();e!=(c).end();e++)
#define pb push_back
#define X first
#define Y second
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 
#define TAB '\t'
#define NL cout << endl
#define DUMP(a) FORE(__it,a) cout << *__it << ' ';
#define DUMPP(a) FORE(__it,a) cout << "(" << __it->X << ", " << __it->Y << ")" << ' ';
#define __bitn(a,n) bitset<n>((a))
#define __bit(a) __bitn(a,8)
#define __pr(a) cout << (a) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

#define __min(A,B,C) min((A),min((B),(C)))

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

int to_min(string s) {
	char* res = NULL;
	res = strtok((char*)s.c_str(),":");
	int h = atoi(res);
	res = strtok(NULL,":");
	int m = atoi(res);

	return h*60 + m;
}

int
get_count(VI& dt, VI& rt) {
	int count = 0;
	int bl = 0;
	typedef VI::iterator VII;
	VII e = dt.begin();
	VII f = rt.begin();

	while(f != rt.end() || e != dt.end()) {
		if( f == rt.end() ) { 
			if(bl == 0) count++;
			else bl--;
			e++;
		}
		else
		if( e == dt.end() ) {
			f++;
		}
		else {
			if(*e < *f) {
				if(bl == 0) count++;
				else bl--;
				e++;
			}
			else
			if(*e > *f) { bl++; f++; }
			else {
				e++; f++;
			}
		}
	}
	return count;
}

int main() {
	//ifstream ifs("B-small-attempt1.in");
	//ifstream ifs("test.in");
	ifstream ifs("B-large.in");
	int N;
	ifs >> N;

	FOR(i,1,N) {
		int T, NA, NB;
		ifs >> T >> NA >> NB;

		VI DT_A, DT_B;
		VI RT_A, RT_B;

		REP(j,NA) {
			string a, b;
			ifs >> a >> b;
		//	cout << to_min(a) << " " << to_min(b) << endl;
			DT_A.pb(to_min(a));
			RT_B.pb(to_min(b) + T);
		}
		REP(j,NB) {
			string a, b;
			ifs >> a >> b;
		//	cout << to_min(a) << " " << to_min(b) << endl;
			DT_B.pb(to_min(a));
			RT_A.pb(to_min(b) + T);
		}
		sort(all(DT_A));
		sort(all(RT_A));

		sort(all(RT_B));
		sort(all(DT_B));

		cout << "Case #" << i << ": ";
		cout << get_count(DT_A,RT_A);
		cout << " ";
		cout << get_count(DT_B,RT_B);
		cout << endl;
	}
}
