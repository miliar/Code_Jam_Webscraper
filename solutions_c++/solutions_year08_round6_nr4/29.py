#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cassert>
using namespace std;

#define FOR(i, a, b) for(__typeof(a) i = (a); i < (b); i++)
#define FOREACH(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define PB push_back
#define CLEAR(a, b) memset(a, (b), sizeof(a))
#define SZ(v) (int)((v).size())
#define MP make_pair

typedef pair<int, int> PII;

const int N = 128;

int n, m;
vector<int> g1[N], g2[N];
map< pair<PII, PII>, int > mth;

bool subgraph();
bool match(int, int, int, int);
bool dfs(const vector<int>*, int);

bool chk[N];
int mate[N];

int main()
{
	int T;
	scanf("%d", &T);
	FOR(t, 1, T+1) {
		mth.clear();
		scanf("%d", &n);
		FOR(i, 0, n) g1[i].clear();
		FOR(i, 1, n) {
			int a, b; scanf("%d %d", &a, &b); a--; b--;
			g1[a].PB(b); g1[b].PB(a);
		}
		scanf("%d", &m);
		FOR(i, 0, m) g2[i].clear();
		FOR(i, 1, m) {
			int a, b; scanf("%d %d", &a, &b); a--; b--;
			g2[a].PB(b); g2[b].PB(a);
		}
		printf("Case #%d: %s\n", t, subgraph() ? "YES" : "NO");
	}
	return 0;
}

bool subgraph()
{
	// it is the matcher of g2-v[0] in g1
	FOR(i, 0, n) {
		if(match(i, 0, -1, -1)) return true;
	}
	return false;
}
bool match(int v1, int v2, int p1, int p2)
{
	if(SZ(g1[v1]) < SZ(g2[v2])) return false;
	PII e1 = MP(v1, p1), e2 = MP(v2, p2);
	if(mth.count(MP(e1, e2))) return mth[MP(e1, e2)] == 1;
	// if g1[v1] && g2[v2] are match or not
	int nk = 0, res = 1;
	vector<int> mg[N];
	FOREACH(i, g2[v2]) if(*i != p2) {
		FOREACH(j, g1[v1]) if(*j != p1 && match(*j, *i, v1, v2)) mg[nk].PB(*j);
		if(SZ(mg[nk]) == 0) { res = 0; break; }
		nk++;
	}
	if(res == 0) {
		mth[MP(e1, e2)] = 0;
		return false;
	}
	CLEAR(mate, -1);
	FOR(i, 0, nk) {
		CLEAR(chk, false);
		if(!dfs(mg, i)) { res = 0; break; }
	}
	mth[MP(e1, e2)] = res;
	return res == 1;
}
bool dfs(const vector<int> *g, int p)
{
	FOREACH(i, g[p]) if(!chk[*i]) {
		assert(*i >= 0 && *i < n);
		chk[*i] = true;
		int t = mate[*i];
		mate[*i] = p;
		if(t == -1 || dfs(g, t)) return true;
		mate[*i] = t;
	}
	return false;
}

