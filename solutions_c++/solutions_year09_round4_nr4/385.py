#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }
#define memfill(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define vi vector<int>
#define vii vector<vector<int> >
#define vs vector<string>
#define pii pair<int, int>
#define dist(a, b) sqrt(1.0 * sqr(a.x - b.x) + 1.0 * sqr(a.y - b.y))
#define bound(x, y, n, m) x >= 0 && y >= 0 && x < n && y < m

struct point
{
	int x, y, r;
};

int n;
point pts[5];

double solve()
{
	if (n <= 2)
		return max(pts[0].r, pts[1].r);
	if (n == 3)
	{
		double p1 = max(pts[0].r * 1.0, (dist(pts[1], pts[2]) + pts[1].r + pts[2].r) / 2);
		double p2 = max(pts[1].r * 1.0, (dist(pts[0], pts[2]) + pts[0].r + pts[2].r) / 2);
		double p3 = max(pts[2].r * 1.0, (dist(pts[1], pts[0]) + pts[1].r + pts[0].r) / 2);
		return min(p1, min(p2, p3));
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d%d%d", &pts[i].x, &pts[i].y, &pts[i].r);
		printf("Case #%d: %0.7lf\n", testCount + 1, solve());
	}
	return 0;
}