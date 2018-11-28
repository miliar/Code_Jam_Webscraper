#include <iostream>
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
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int MAX = 1007;

struct rec
{
	int l, index;
	double p;
} in[MAX];
int N;

double tim(rec r1, rec r2)
{
	return (r1.l + (1.0-r1.p) * r2.l) / (1.0 - r1.p - (1.0-r1.p)*r2.p);
}

bool comp(rec r1, rec r2)
{
	double t1 = tim(r1, r2), t2 = tim(r2, r1);
	if (EQ(t1, t2)) return r1.index < r2.index;
	return t1 < t2;
}

void Solve(int tc)
{
	scanf("%d", &N);
	REP(i, N)
	{
		in[i].index = i;
		scanf("%d", &in[i].l);
	}
	REP(i, N)
	{
		int temp;
		scanf("%d", &temp);
		in[i].p = temp / 100.0;
	}
	sort(in, in+N, comp);
	printf("Case #%d:", tc);
	REP(i, N) printf(" %d", in[i].index);
	printf("\n");
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}