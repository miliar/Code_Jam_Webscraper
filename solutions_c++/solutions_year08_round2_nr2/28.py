#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

// BEGIN CUT HERE
#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef long long i64;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
// END CUT HERE

class DisjointSet
{
	private:
		int nSets;
		VI prev;

	public:
		DisjointSet(int N) : prev(N) {
			REP(i, N)
				prev[i] = i;
			nSets = N;
		}

		int findRoot(int v) {
			if (prev[v] == v)
				return v;
			return prev[v] = findRoot( prev[v] );
		}

		void unite(int u, int v) {
			u = findRoot(u);
			v = findRoot(v);
			if (u != v) {
				nSets--;
				prev[u] = v;
			}
		}

		int getNumSets() { return nSets; }
};

VI primes;

bool isPrime(int P) {
	REP(i, primes.sz) {
		int p = primes[i];
		if (p*p > P)
			break;
		if (P % p == 0)
			return false;
	}
	return true;
}

i64 solve()
{
	i64 A, B, P;
	cin >> A >> B >> P;
	int nums = B-A+1;

	DisjointSet ds(nums);
	while (P <= nums) {
		if (isPrime(P)) {
			i64 first = (A+P-1)/P, last = B/P;
			first *= P;
			last *= P;
			while (first < last) {
				ds.unite(first-A, last-A);
				first += P;
			}
		}
		P++;
	}

	return ds.getNumSets();
}

int main()
{
	primes.pb(2);
	primes.pb(3);
	primes.pb(5);
	for (int i = 7; i < 1024; i += 2)
		if (isPrime(i))
			primes.pb(i);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		cout << "Case #" << iTest << ": " << solve() << endl;
	return 0;
}
