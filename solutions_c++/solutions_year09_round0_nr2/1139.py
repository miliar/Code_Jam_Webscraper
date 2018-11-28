#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;
typedef vector<LL> vl;
typedef vector<double> vd;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define SZ(a) (a.size())
#define MP(a, b) make_pair(a, b)
#define SHL(a,b) ((a) << (b)) 
#define SHR(a,b) ((a) >> (b))
#define SE second
#define FI first

template<class T> int bitcount(T a) { int x = 0; while (a) { x += (a & 1); a >>= 1; } return x; }
template<class T> inline T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> inline T sqr(T a) { return a * a; } // NOTE: T must be enough to save sqr!
inline int parity(LL a) { return __builtin_parityl(a); }
inline int parity(int a) { return __builtin_parity(a); }
template<class T> T s2type(string s) { T res; istringstream in(s); in >> res; return res; }
template<class T> string toString(T n) { ostringstream out; out << n; return out.str(); }

const double PI = acos(-1.0);
const double EPS = 1e-11;

typedef pair<int, pii> piii;

int dx[] = { -1, 0, 0, 1 };
int dy[] = { 0, -1, 1, 0 };

int from[100][100];
int al[100][100];
piii zz[10000];
char trans[100];
int t, n, m;

int inside(int r, int c)
{
	return r >= 0 && r < n && c >= 0 && c < m;
}

int main()
{
	int i, j, k, l, ct, r, c, a, count, dir;

	scanf("%d", &t);
	FOR(i, t)
	{
		scanf("%d %d", &n, &m);
		ZERO(trans); MINUS(from); ct = count = 0;
		FOR(j, n) FOR(k, m) { scanf("%d", &al[j][k]); zz[ct++] = MP(al[j][k], MP(j, k)); }
		sort(zz, zz + ct);
		FOR(j, ct)
		{
			a = zz[j].FI; r = zz[j].SE.FI; c = zz[j].SE.SE; l = a; dir = -1;
			FOR(k, 4)
				if (inside(r + dx[k], c + dy[k]) && l > al[r + dx[k]][c + dy[k]]) 
					{ l = al[r + dx[k]][c + dy[k]]; dir = k; }
			from[r][c] = (dir == -1) ? count++ : from[r + dx[dir]][c + dy[dir]];
		}
		printf("Case #%d:\n", i + 1);
		l = 0;
		FOR(j, n) 
		{
			FOR(k, m) printf(k ? " %c" : "%c", trans[from[j][k]] ? trans[from[j][k]] + 'a' - 1 : (trans[from[j][k]] = ++l) + 'a' - 1);
			printf("\n");
		}
	}
	return 0;
}

