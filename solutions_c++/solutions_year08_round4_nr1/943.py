#include <cstdio>
#include <vector>
#include <cmath>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define SORT(A) sort(A.begin(),A.end())
#define MP(a,b) make_pair(a,b)
#define SQR(x) (x*x)
#define eps (1e-7)

#define inf 100000

int V, M;
int inode[10010];
int change[10010];
int onode[10010];

int DFS(int i, int v) {
	if (2 * i > M / 2) {
		if (v) {
			if (inode[i - 1]) {
				if (onode[2 * i - 1 - M / 2] && onode[2 * i - M / 2]) return 0;
				else {
					if (change[i - 1]) {
						if (!onode[2 * i - 1 - M / 2] && !onode[2 * i - M / 2]) return inf;
						else return 1;
					}
					else return inf;
				}
			}
			else {
				if (onode[2 * i - 1 - M / 2] || onode[2 * i - M / 2]) return 0;
				else return inf;
			}
		}
		else {
			if (inode[i - 1]) {
				if (!onode[2 * i - 1 - M / 2] || !onode[2 * i - M / 2]) return 0;
				else return inf;
			}
			else {
				if (!onode[2 * i - 1 - M / 2] && !onode[2 * i - M / 2]) return 0;
				else {
					if (change[i - 1]) {
						if (onode[2 * i - 1 - M / 2] && onode[2 * i - M / 2]) return inf;
						else return 1;
					}
					else return inf;
				}
			}
		}
	}

	int left, right;
	left = DFS(2 * i, v);

	if (2 * i + 1 > M / 2) {
		if (v) {
			if (onode[2 * i - M / 2]) right = 0;
			else right = inf;
		}
		else {
			if (!onode[2 * i - M / 2]) right = 0;
			else right = inf;
		}
	}
	else right = DFS(2 * i + 1, v);

	--i;
	if (v) {
		if (inode[i]) {
			if (change[i]) return MIN(left + right, MIN(left, right) + 1);
			else return (left + right);
		}
		else {
			return MIN(left, right);
		}
	}
	else {
		if (inode[i]) {
			return MIN(left, right);
			
		}
		else {
			if (change[i]) return MIN(left + right, MIN(left, right) + 1);
			else return (left + right);
		}
	}
}

void solve(int id) {
	int ans = DFS(1, V);

	if (ans >= inf)
		printf("Case #%d: IMPOSSIBLE\n", id);
	else printf("Case #%d: %d\n", id, ans);
}

int main() {
	/*freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);*/

	/*freopen("A-small.in", "r", stdin);
	freopen("A-small.txt", "w", stdout);*/

	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);

	int C;
	scanf("%d", &C);
	REP(i, C) {
		scanf("%d %d", &M, &V);
		REP(j, (M - 1) / 2)
			scanf("%d %d", inode + j, change + j);
		REP(j, (M + 1) / 2)
			scanf("%d", onode + j);
		solve(i + 1);
	}
	return 0;
}