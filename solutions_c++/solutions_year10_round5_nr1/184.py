#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FOR2(i, a, b) for (int i = (a); i > (b); --i)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1 << 29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=last_bit(n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 1000047;
bool no_prime[MAX];
vector<int> primes;

void init()
{
	FOR(i, 2, MAX)
		if (!no_prime[i])
		{
			primes.push_back(i);
			for (int j = i; j < MAX; j += i)
				no_prime[j] = true;
		}
}


ll mod(ll A, ll P)
{
	A %= P;
	if (A < 0) A += P;
	return A;
}

template <class T>
T gcd(T a, T b, T & x, T & y)
{
	if (!b)
	{
		x = (T)1;
		y = (T)0;
		return a;
	}

	T xx, yy;
	T d = gcd(b, a%b, xx, yy);

	x = yy;
	y = xx - (a/b)*yy;
	return d;
}

ll inverse(ll a, ll P)
{
	a = mod(a, P);
	ll x, y;
	gcd(a, P, x, y);
	return mod(x, P);
}

ll input[10];

void Solve(int tc)
{
	ll D, K;
	cin >> D >> K;
	FOR(i, 0, K) cin >> input[i];

	ll maxP = 1;
	FOR(i, 0, D) maxP *= 10;

	ll maxim = 0;
	FOR(i, 0, K) chmax(maxim, input[i]);
	set<ll> sols;

	//find cycle
	map<ll, int> visited;
	FOR(i, 0, K)
	{
		map<ll, int>::iterator iter = visited.find(input[i]);
		if (iter != visited.end() && i == K-1)
			sols.insert(input[iter->second+1]);
		visited[input[i]] = i;
	}

	//solve
	if (K >= 3 && sols.empty())
	{
		ll N1 = input[0], N2 = input[1], N3 = input[2];
		ll A, B;

		FOR(i, 0, primes.size())
		{
			ll P = primes[i];
			if (primes[i] > maxP) break;
			if (primes[i] <= maxim) continue;
		
			if (N1 == 0)
			{
				A = mod(mod(N3-N2, P) * inverse(N2, P), P);
				B = N2;
			}
			else if (N2 == 0)
			{
				A = mod(mod(N2-N3, P) * inverse(N1, P), P);
				B = N3;
			}
			else
			{
				B = mod(mod(N3*N1-N2*N2, P) * inverse(N1-N2, P), P);
				A = mod(mod(N2-B, P) * inverse(N1, P), P);
			}

			bool check = true;
			FOR(j, 0, K-1)
			{
				if (input[j+1] != mod(A*input[j]+B, P))
					check = false;
			}
			if (check)
				sols.insert(mod(A*input[K-1]+B, P));
		}
	}

	cout << "Case #" << tc << ": ";
	if (sols.size() != 1) cout << "I don't know." << endl;
	else cout << *sols.begin() << endl;
}

int main()
{
	init();

	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}