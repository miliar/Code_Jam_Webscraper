#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
typedef vector<PII> CONF;
#define LL long long

const int INF = 100000000;
const int MAX = 100;

int hx[4] = {-1, 0, 1, 0};
int hy[4] = {0, 1, 0, -1};

int n, m, box, ans;
VS a;
CONF start, goal;
set<CONF> ss;

void refine(CONF &cf)
{
	sort(ALL(cf));
}

bool isNear(PII &x, PII &y)
{
	return (x.first == y.first && abs(x.second - y.second) == 1) ||
		   (x.second == y.second && abs(x.first - y.first) == 1) ;
}

bool isSafe(CONF &cf)
{
	bool ex[5];
	memset(ex, false, sizeof(ex));
	queue<PII> q;
	q.push(cf[0]);
	ex[0] = true;
	int cnt = 1, i;
	while (!q.empty())
	{
		PII cur = q.front(); q.pop();
		RP(i, box) if (!ex[i] && isNear(cur, cf[i]))
		{
			q.push(cf[i]);
			ex[i] =  true;
			cnt++;
		}
	}
	return cnt == box;
}

CONF nextMov(CONF cf, int v)
{
	bool free[4];
	memset(free, false, sizeof(free));

	int i, j, x, y;
	RP(i, 4)
	{
		x = cf[v].first + hx[i];
		y = cf[v].second + hy[i];

		if (x<0 || x>=n) continue;
		if (y<0 || y>=m) continue;
		if (a[x][y] == '#') continue;

		free[i] = true;
		RP(j, box) if (cf[j].first == x && cf[j].second == y)
		{
			free[i] = false;
			break;
		}
	}

	CONF res;
	if (free[0] && free[2])
	{
		res.pb(PII(cf[v].first + hx[0], cf[v].second + hy[0]));
		res.pb(PII(cf[v].first + hx[2], cf[v].second + hy[2]));
	}
	if (free[1] && free[3])
	{
		res.pb(PII(cf[v].first + hx[1], cf[v].second + hy[1]));
		res.pb(PII(cf[v].first + hx[3], cf[v].second + hy[3]));
	}

	return res;
}

void process()
{
	box = SZ(start);
	sort(ALL(start));
	sort(ALL(goal));
	ss.clear();

	queue<CONF> q;
	queue<bool> safe;
	queue<int> steps;
	q.push(start);
	safe.push(isSafe(start));
	steps.push(0);
	ss.insert(start);
	ans = -1;

	int i, j;

	while (!q.empty())
	{
		CONF cur = q.front(); q.pop();
		bool cSafe = safe.front(); safe.pop();
		int cDis = steps.front(); steps.pop();

		if (cur == goal) { ans = cDis; break; }

		RP(i, box)
		{
			CONF nxt = nextMov(cur, i);
			RP(j, SZ(nxt))
			{
				CONF newCf = cur;
				newCf[i] = nxt[j];
				refine(newCf);
				bool newSafe = isSafe(newCf);

				if (cSafe || newSafe) if (ss.count(newCf) == 0)
				{
					ss.insert(newCf);
					q.push(newCf);
					safe.push(newSafe);
					steps.push(cDis+1);
				}
			}
		}
	}
}

int main()
{
	//freopen("sample.in", "r", stdin); //freopen("sample.out", "w", stdout);
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	int tc, testcase, i, j;
	string str;

	cin >> tc;

	RP(testcase, tc)
	{
		cin >> n >> m;
		a.resize(n);
		start.clear();
		goal.clear();
		RP(i, n)
		{
			cin >> a[i];
			RP(j, m)
			{
				if (a[i][j]=='x') goal.pb(PII(i, j));
				if (a[i][j]=='o') start.pb(PII(i, j));
				if (a[i][j]=='w') { start.pb(PII(i, j)); goal.pb(PII(i, j)); }
			}
		}
		process();
		printf("Case #%d: %d\n", (testcase+1), ans);
	}

	return 0;
}
