#include<iostream>
#include<iterator>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<string>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<complex>
#include<bitset>
#include<cstdio>
#include<cassert>
#include<cmath>
#include<ctime>
#include<sys/time.h>

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

const LL inf = 100000000;

vector<LL> X;
vector<LL> Y;

int main() {
	int T;
	cin>>T;
	FOR(nr,1,T) {
		X.clear();
		Y.clear();

		int n;
		cin >> n;
		REP(k,n) {
			int x;
			cin >> x;
			X.pb(x);
		}
		REP(k,n) {
			int y;
			cin >> y;
			Y.pb(y);
		}

		sort(all(X));
		sort(all(Y),greater<int>());

		LL sum = 0;
		REP(i,n) {
			sum += X[i]*Y[i];
		}
		cout << "Case #" << nr << ": " << sum;
		cout << endl;
	}
}
