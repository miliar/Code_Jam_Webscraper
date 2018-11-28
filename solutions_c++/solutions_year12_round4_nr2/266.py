#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
const int INF = 1e9;
const double EPS = 1e-9;

int R[1500];
int V[1500];
struct point
{
	int x, y;
	point(){}
	point(int _x, int _y)
	{
		x = _x;
		y = _y;
	}
	void print()
	{
		printf("%d %d ", x, y);
	}
	point operator - (const point & other)
	{
		return point (x - other.x, y - other.y);
	}
	double dist()
	{
		return sqrt(x*1.*x + y*1.*y);
	}
} X[1500];
int N, W, L;
bool cmp(int a, int b)
{
	return R[a] > R[b];
}
bool tr(int i, int x, int y)
{
	int nm = V[i];
	x += R[nm];
	y += R[nm];
	if (x < 0) x = 0;
	if (y < 0) y = 0;
	if (x > W) x = W;
	if (y > L) y = L;
	for (int j = 0; j < i; ++j)
	{
		int t = V[j];
		if (labs(x - X[t].x) < R[nm] + R[t] && labs(y - X[t].y) < R[nm] + R[t]) return false;
	}
	X[nm] = point(x, y);
	return true;
}
void solve()
{
	scanf ("%d%d%d", &N, &W, &L);
	for (int i = 0; i < N; ++i)
	{
		scanf ("%d", &R[i]);
		V[i] = i;
	}
	sort(V, V + N, cmp);
	for (int i = 0; i < N; ++i)
	{
		bool f = false;
		if (!tr(i, -R[V[i]], -R[V[i]]))
		{
			for (int j = 0; j < i; ++j)
			{
				if (tr(i, X[V[j]].x - R[V[j]], X[V[j]].y + R[V[j]]))
				{
					f = true;
					break;
				}
				if (tr(i, X[V[j]].x + R[V[j]], X[V[j]].y - R[V[j]]))
				{
					f = true;
					break;
				}
			}
			if (!f)
				throw 42;
		}
	}
	for (int i = 0; i < N; ++i)
	{
		X[i].print();
		/*for (int j = 0; j < i; ++j)
		{
			if ((X[i] - X[j]).dist() < R[i] + R[j] - 1e-9)
				throw 42;
		}*/
	}
	puts("");
}
int main()
{
	freopen("Btest.txt", "r", stdin);
	freopen("Bout.txt", "w", stdout);

	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}