//* Problem  : 
//* Contest  : Google Code Jam 2008. Online Round 2
//* Date     : 2008.08.02
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef pair <int,int> PIII;
typedef vector <int> VI;
typedef vector <vector<int> > VVI;
typedef vector <pair<int,int> > VPII;
typedef vector <vector<pair<int,int> > > VVPII;

#define int64 long long
#define PI (2.0 * acos(0.0))
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define FORSZ(i, a) FOR(i, SZ(a))
#define FORE(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define FORR(i, a, b) for (int i = (int)(a); i >= int(b); i--)
#define INF 1000000000
#define INFL 1000000000000000000LL
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()

int it, nt;
inline int si(){int tt; scanf("%d", &tt); return tt;}

int n, k, res;

char s[2020];

int a[12];

char t[2000];

void process()
{
	for (int i = 0; i < n; i += k)
	{
		for (int kk = 0; kk < k; kk++)
			t[i+kk] = s[i+a[kk]];
	}
	t[n] = 0;
}

int calc()
{
	int res = 1;
	for (int i = 1; i < n; i++)
		res += t[i] != t[i-1];
	return res;
}

void solve()
{
	res = INF;
	FOR(i,k)
		a[i] = i;
	do
	{
		process();
		int t = calc();
		res = min(res, t);
	}
	while (next_permutation(a, a + k));
}

void result()
{
	printf("Case #%d:", it);
	printf(" %d\n", res);
}


int main()
{
	freopen("1064", "r", stdin);
	freopen("A-small.out", "w", stdout);	
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		k = si();
		scanf("%s", s);
		n = strlen(s);
		solve();
		result();
	}
	return 0;
}

