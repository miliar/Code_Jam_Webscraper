#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)

//#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
//#define SIZE(x) int(x.size())

typedef pair<int,int> PII;
typedef long long ll;

class Rect
{
public:
	int x1, y1, x2, y2;
};

inline bool ptin(int x, int y, Rect r) {
	return (x >= r.x1 && x <= r.x2 && y >= r.y1 && y <= r.y2);
}

inline bool adjacent(Rect a, Rect b) {
	if ((a.x2 == b.x1 && a.y2 == b.y1)
		||(b.x2 == a.x1 && b.y2 == a.y1))
		return false;

	int x1, y1, x2, y2;
	x1 = max(a.x1, b.x1);
	y1 = max(a.y1, b.y1);
	x2 = min(a.x2, b.x2);
	y2 = min(a.y2, b.y2);

	return (x1 <= x2 && y1 <= y2);
}

inline bool mysort(const Rect &a, const Rect &b) {
	return (a.x1+a.y1) < (b.x1+b.y1);
}

Rect rects[1010];
bool used[1010];
vector<int> graph[1010];

void ribo(int v, int &x, int &y)
{
	x = rects[v].x2;
	y = rects[v].y2;

	if (used[v])
		return;
	used[v] = true;
	
	int px, py;

	FOR (i, 0, graph[v].size()) {
		ribo(graph[v][i], px, py);
		x = max(x, px);
		y = max(y, py);
	}
	return;
}

void Solve(int testcase)
{
	printf("Case #%d: ", testcase+1);
	int N;
	scanf(" %d", &N);

	FOR (i, 0, N) {
		scanf(" %d %d %d %d", &rects[i].x1, &rects[i].y1, &rects[i].x2, &rects[i].y2);

		if (rects[i].x1 > rects[i].x2) swap(rects[i].x1, rects[i].x2);
		if (rects[i].y1 > rects[i].y2) swap(rects[i].y1, rects[i].y2);
		rects[i].x2++;
		rects[i].y2++;
		graph[i].clear();
	}

	sort(rects, rects+N, mysort);

	FOR (i, 0, N)
		FOR (j, i+1, N)
			if (adjacent(rects[i], rects[j])) {
				graph[i].push_back(j);
				graph[j].push_back(i);
			}

	memset(used, 0, sizeof(used));
	int besttime = -1;
	int rmx, rmy;

	FOR (i, 0, N)
		if (!used[i])
		{
			ribo(i, rmx, rmy);
			if (besttime < (rmx+rmy)-(rects[i].x1+rects[i].y1))
				besttime = (rmx+rmy)-(rects[i].x1+rects[i].y1);
		}


	printf("%d\n", besttime-1);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (t, 0, T)
		Solve(t);

	return 0;
}
