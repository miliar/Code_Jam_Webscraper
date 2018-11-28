//105514SN
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, a, b) for(int i=(a);i<int(b);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);

int mem[110][110], n, s, p;
int t[110];
int sur[110], nsur[110];

int surp(int total) {
	int r = 0;
	forn(i, 0, 11) forn(j, 0, 11) forn(k, 0, 11) if(i+j+k == total) {
		if(abs(i-j) <= 2 && abs(i-k) <= 2 && abs(k-j) <= 2) 
			r = max(r, max( max(i, j), k));
	}
	return r;
}

inline int nsurp(int total) {
	int r = 0;
	forn(i, 0, 11) forn(j, 0, 11) forn(k, 0, 11) if(i+j+k == total) {
		if(abs(i-j) <= 1 && abs(i-k) <= 1 && abs(k-j) <= 1) 
			r = max(r, max( max(i, j), k));
	}
	return r;
}

int doit(int k, int sor) {

	if(k <= -1) return 0;
	if(mem[k][sor] != -1) return mem[k][sor];
	
	int &r = mem[k][sor] = 0;

	int m1 = sur[k] , m2 = nsur[k];

	if(sor>0)
		r = max(r, doit(k-1, sor-1) + ((m1>=p) ? 1: 0));

	r = max(r, doit(k-1, sor) + ((m2>=p) ? 1: 0));
	return r;
}

int main(void) {

	int casos;
	cin >> casos;
	forn(q, 0, casos) {
	
		memset(mem, -1, sizeof(mem));
		cin >> n >> s >> p;
		forn(i, 0, n) cin >> t[i];
		forn(i, 0, n) sur[i] = surp(t[i]);
		forn(i, 0, n) nsur[i] = nsurp(t[i]);

//		forn(i, 0, n) cout << sur[i] << " ";cout << endl;
//		forn(i, 0, n) cout << nsur[i] << " ";cout << endl;

		cout << "Case #" << q+1 << ": " << doit(n-1, s) << endl;
	}
	return 0;
}
