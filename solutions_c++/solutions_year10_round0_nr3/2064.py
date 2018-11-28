#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <cmath>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long Int;

#define FOR(i, a, b) for(int i=a; i<b; ++i)
#define RFOR(i, a, b) for(int i=b-1; i>=a; --i)
#define FILL(a, val) memset(a, val, sizeof(a))

#define all(c) c.begin(), c.end()
#define sz(c) (int)c.size()
#define pb push_back

#define mp make_pair
#define X first
#define Y second

const double PI = acos(-1.0);
const int INF = 1000000000;

int a[1000];
int b[1000];

pair<int, Int> d[1000][31];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	FOR(t, 0, T)
	{
		int r, n;
		Int k;
		scanf("%d%lld%d", &r, &k, &n);
		FOR(i, 0, n)
			scanf("%d", &a[i]);
		Int res;
		Int s = 0;
		FOR(i, 0, n)
			s += a[i];
		if (s <= k)
		{
			res = s*r;
		}
		else
		{

			res = 0;

			FOR(i, 0, n)
			{
				Int s = 0;
				int ind = 0;
				FOR(j, 0, n)
				{
					ind = (i + j)%n;
					if (s + a[ind] > k)
					{
						break;
					}
					else
						s += a[ind];
				}
				d[i][0] = mp(ind, s);
			}
			FOR(i, 1, 31)
			{
				FOR(j, 0, n)
					d[j][i] = mp(d[d[j][i-1].X][i-1].X, d[d[j][i-1].X][i-1].Y + d[j][i-1].Y);
			}
			int pos = 0;
			FOR(i, 0, 31)
				if (r & (1<<i))
				{
					res += d[pos][i].Y;
					pos = d[pos][i].X;
				}
		}
		printf("Case #%d: %lld", t+1, res);
		if (t != T-1)
			printf("\n");
	}
	return 0;
}

/*
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

*/