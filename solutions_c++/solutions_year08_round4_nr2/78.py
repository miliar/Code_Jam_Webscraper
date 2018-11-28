#include <iostream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <algorithm>
#include <numeric>
#include <math.h>
using namespace std;

#define TR(it, c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define rTR(it, c) for(typeof((c).rbegin()) it = (c).rbegin(); it != (c).rend(); ++it)
#define REP(i,n) for(int i=0; i<(int)(n); ++i)
#define rREP(i, n) for(int i = (int)(n) - 1; i >=0; --i)
#define sz size()
#define all(c) (c).begin(), (c).end()

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<bool> vb;

#define fi first
#define se second

#define MOD 1000000007

template<typename T> 
	ostream &operator << (ostream &os, vector<T> V) {
		TR(it, V) os << *it << " ";
		return os;
	}

template<typename T>
	istream &operator >> (istream &is, vector<T> &V) {
		TR(it, V) is >> *it;
		return is;
	}

template<typename T> 
	string toString(T x) {ostringstream o; o << x; return o.str();}

string operator ~(string &A) { string B; rTR(i, A) B += *i; return B; }	
	
ll gcd(ll a, ll b) {return b ? gcd(b, a%b): a;}

vector< vector<ll> > nOverK(110, vector<ll>(110, -1));
ll get_nOverK(int n, int k){
	if(k>n || n<0 || k<0) return 0;
	ll &ret = nOverK[n][k];
	if(ret==-1) ret = (n==0 ? 1: (get_nOverK(n-1,k) + get_nOverK(n-1,k-1)) % MOD );
	return ret;
}
	
template<typename T>
vector<int> indexify(vector<T> &V) {
	vector<T> S(V);
	sort( all(S) );
	S.resize(unique(all(S)) - S.begin());
	
	map<T, T> M;
	REP(i, S.sz) M[ S[i] ] = i;
	
	vector<int> ret(V.sz);
	
	REP(i, ret.sz) ret[i] = M[ V[i] ];
	V.swap(S);
	
	return ret;
}
	
int pow2_ceil(int x) {
	int b = 31 - __builtin_clz(x);
	if (b != __builtin_ctz(x)) ++b;
	return 1 << b;
}

// === Calculates strongly connected components (SCC) of a directed graph ========			
void tarjan(int v, vector< vector<bool> > &E) {
	static int cnt = 0;
	static stack<int> S;
	static vi idx, lowLink;
	
	if (idx.empty()) { idx.resize(E.sz, -1); lowLink.resize(E.sz); }
	
 	idx[v] = lowLink[v] = cnt++; 
  	S.push(v); 
  	
  	REP(i, E.sz) if (E[v][i]) { 
		if (idx[i] == -1) { 
			tarjan(i, E); 
			lowLink[v] <?= lowLink[i];
		}else{
		 	lowLink[v] <?= idx[i];
      	}
  	}
  	   
   	if (lowLink[v] == idx[v]) {
   		cout << "SCC: ";
   	
   		int i;
    	do {
    		i = S.top(); S.pop();
      		cout << i << " ";
    	} while(i != v);
    	
    	cout << endl;
    }
} // =======================================================================




// ============ Keeps the value in a finite ring (modulus) ============
template <typename T, T mod> class ring {
	T x;
	T &wash(T x) { if ((x %= mod) < 0) x += mod; return x; }
public:	
	ring() {}
	ring(const T &x) : x(wash(x)) {}
	
	ring &operator *=(const T &r) { x = wash(x * (r % mod)); return *this;}
	ring &operator +=(const T &r) { (x += wash(r)) %= mod; return *this;}
	ring &operator -=(const T &r) { return (*this += -r); }
	ring &operator ++()           { if (++x == mod) x = 0; return *this; }
	ring &operator --()           { if (--x < 0) x += mod; return *this; }
	ring  operator ++(int)        { ring tmp = *this; if (++x == mod) x = 0; return tmp; }
	ring  operator --(int)        { ring tmp = *this; if (--x < 0) x += mod; return tmp; }
	
	ring operator *(const T &r)   { return (ring(*this) *= r); }
	ring operator +(const T &r)   { return (ring(*this) += r); }
	ring operator -(const T &r)   { return (ring(*this) -= r); }
	
	ring &operator-() { x=mod-x; return *this;}
	
	operator T() { return x; }
}; // =================================================================

// ====== Sequence-class which sums up consecutive elements in O(log n) =======
template<typename T>
class cumulative {
	int N;
	vector<T> V;
	
public:	
	cumulative() {}
	cumulative(int n) : N( pow2_ceil(n) ), V( vector<T>(2 * N, 0) ) {}

	void add(int i, T x) {
		V[ i += N ] += x;	
		while(i /= 2) V[i] += x;			
	}
	void set(int i, T x) { add(i, x - V[i + N]); }
		
	T getSum(int i) {
		T ret = V[1];
		for (i += N; i > 0; i /= 2)
			if ((i&1) == 0) ret -= V[i+1];
		return ret;
	}
}; // =========================================================================

// ============== Dijkstra-queue ======================
template<typename dist, typename node> class dijkstra {	
	map<node, dist> M;
	set< pair<dist, node> > Q;
public:	
	void push(dist d, node n) {
		typeof( M.find(n) ) it = M.find(n);
				
		if (it != M.end()) {
			if (it->second <= d) return;
			Q.erase( mp(it->second, n) );
		}
		Q.insert( mp(d, n) );
		M[n] = d;
	}
	
	const pair<dist, node> &top() { return *Q.begin();  }
	void pop()   { Q.erase(Q.begin()); }
	bool empty() { return Q.empty();  }	
}; // =================================================




void solve();
void init();

int main() {
	int n; cin >> n;
	init();
	REP(i, n) 
		{ cout << "Case #" << i+1 << ": "; solve(); cout << endl; }		
	return 0;
}


