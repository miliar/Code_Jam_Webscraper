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
#define FOREACH(it,c) for(vector<int>::iterator it =(c).begin();it!=(c).end();++it)

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

class max_matcher
{
    public:
        static const int MaxV = 1024;
        
        int V, VLeft;
        vector<int> next[MaxV];

    private:
        int match_size, match[MaxV], prev[MaxV];
        int final;

        /* Find augumenting path */
        bool findpath(int v)
        {
            FOREACH(pv, next[v]) {
                if (prev[*pv] != -1)
                    continue;

                prev[*pv] = v;
                if (match[*pv] == -1) {
                    final = *pv;
                    return true;
                }

                int u = match[*pv];
                if (prev[u] != -1)
                    continue;
                prev[u] = *pv;
                if (findpath(u))
                    return true;
            }
            return false;
        }

        /* Augument the path */
        inline void augument()
        {
            int u = prev[final], v = final;
            while (1) {
                match[u] = v;
                match[v] = u;
                if (prev[u] == u)
                    break;
                v = prev[u];
                u = prev[v];
            }
            match_size++;
        }

    public:
        max_matcher() : V(0), VLeft(0) { clear_match(); }
        max_matcher(int V, int VLeft) : V(V), VLeft(VLeft) { clear_match(); }

        void clear_match()
        {
            match_size = 0;
            for (int i = 0; i < V; i++)
                match[i] = -1;
        }

        size_t max_match()
        {
            while (1) {
                size_t cur_size = match_size;
                for (int i = 0; i < V; i++)
                    prev[i] = -1;

                for (int i = 0; i < VLeft; i++)
                    if ((match[i] == -1) && (prev[i] == -1)) {
                        prev[i] = i;
                        if (findpath(i))
                            augument();
                    }

                if (cur_size == match_size)
                    break;
            }
            return match_size;
        }
};

int R, C, yLeft;
char school[128][128];

int getCoord(int x, int y)
{
	if ((x < 0) || (x >= C) || (y < 0) || (y >= R))
		return -1;
	if (school[y][x] == 'x')
		return -1;
	
	if (x % 2 == 0)
		return (x/2)*R + y; else
		return yLeft + (x/2)*R + y;
}

int solve()
{
	scanf("%d %d\n", &R, &C);
	REP(i, R)
		gets(school[i]);

	yLeft = R*((C+1)/2);
	max_matcher mm(R*C, yLeft);
	REP(x, C) REP(y, R) {
		int c0 = getCoord(x, y);
		if ((c0 == -1) || (c0 >= yLeft))
			continue;

		int v;
		v = getCoord(x-1, y);
		if (v != -1) mm.next[c0].pb(v);
		v = getCoord(x-1, y+1);
		if (v != -1) mm.next[c0].pb(v);
		v = getCoord(x+1, y);
		if (v != -1) mm.next[c0].pb(v);
		v = getCoord(x+1, y+1);
		if (v != -1) mm.next[c0].pb(v);
	}

	int vBad = 0;
	REP(i, R) REP(j, C)
		if (school[i][j] == 'x')
			vBad++;

	int match = mm.max_match();
	return R*C - match - vBad;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 1; iTest <= nTest; iTest++)
		cout << "Case #" << iTest << ": " << solve() << endl;
	return 0;
}
