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

// to be used with getline(cin, string)
template<class T> void split(const string &s, vector<T> &token)
{
	istringstream in(s);
	token.clear();
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(token));
}

#define MAXC 301
#define MAXF 10001
#define INF 10000000

int jump[MAXC][MAXF];
int n;
int nc;

void preprocess()
{
	
}

int main()
{
	int tc, col, t, i, j, k, a, b, cur;
	char tmp[128];
	int ans, best;
	
	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d", &n); nc = 0; ans = INF;
		map<string, int> m;
		ZERO(jump);
		FOR(j, n)
		{
			scanf("%s %d %d", tmp, &a, &b);
			if (m.find(tmp) == m.end()) 
			{
				col = nc;
				m[tmp] = nc++;
			}
			else col = m[tmp];
			FORI(i, a, b) jump[col][i] = max(jump[col][i], b);
		}
		if (nc == 1) 
		{
			best = 0; cur = 1;
			while (cur != 10001 && cur != 0) 
			{
				cur = jump[0][cur];
				if (cur == 0) break; else cur++;
				best++;
			}
			if (cur == 10001) ans = min(best, ans);
		}
		else if (nc == 2)
		{
			i = 0; j = 1;
			best = 0; cur = 1;
			while (cur != 10001 && cur != 0) 
			{
				cur = max(jump[i][cur], jump[j][cur]);
				if (cur == 0) break; else cur++;
				best++;
				if (best > ans) break;
			}
			if (cur == 10001) ans = best;
		}
		else
		{
			FOR(i, nc) if (jump[i][10000] != 0) break;
			if (i != nc) 
		FOR(i, nc)
			FORI(j, i+1, nc-1)
				FORI(k, j+1, nc-1)
				{
					best = 0; cur = 1;
					while (cur != 10001 && cur != 0) 
					{
						cur = max(max(jump[i][cur], jump[j][cur]), jump[k][cur]);
						if (cur == 0) break; else cur++;
						best++;
						if (best >= ans) break;
					}
					if (cur == 10001) 
					{
						ans = best;
					}
				}
		}
		printf("Case #%d: ", t + 1);
		if (ans == INF) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	
	return 0;
}

