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

int R; //pocet jazd RC
int k; //kapacita
int N; //pocet grup

const int MAX = 1047;
int sizes[MAX];
int next[MAX];
int income[MAX];

void Solve(int tc)
{
	cin >> R >> k >> N;
	FOR(i, 0, N) cin >> sizes[i];

	FOR(i, 0, N)
	{
		next[i] = i;
		income[i] = 0;
		do
		{
			income[i] += sizes[next[i]];
			next[i] = (next[i]+1) % N;
		} while (next[i] != i && income[i] + sizes[next[i]] <= k);
	}

	ll result = 0;
	int ind = 0;
	FOR(i, 0, R)
	{
		result += income[ind];
		ind = next[ind];
	}
	printf("Case #%d: %lld\n", tc, result);
}

int main()
{
	int T;
	cin >> T;
	FOR(step, 0, T) Solve(step+1);

	return 0;
}