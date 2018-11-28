#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

const double PI = 3.1415926535897932384626433832795;

char buf[10000];
int dist[10007];
double   wh[10007];
int L, N, C, t;

double next(int i)
{
	return (dist[i % C]);
}

double Jump(int id, double time)
{
	if (t <= time) { // все прошли с ускорением 
		return (next(id));
	}
	if (t >= time + 2. * next(id)) { // ускорения нет совсем
		return (2. * next(id));
	}
	double len = (t - time) / 2.;
	return (t - time + next(id) - len);
}

double dfs(int id, double time, int bomb)
{
	if (bomb == -1)
		return (1e100);
	if (id == N)
		return (0);
	double ans1 = 2 * next(id) + dfs(id + 1, time + 2. * next(id), bomb);
	double jump = Jump(id, time);
	double ans2 = jump + dfs(id + 1, jump + 2. * next(id), bomb - 1);
	return (min(ans1, ans2));
}

void solve()
{
	scanf("%d%d%d%d", &L, &t, &N, &C);
	for(int i = 0; i < C; ++i)
		scanf("%d", &dist[i]);

	wh[0] = 0;
	for(int i = 1; i <= N; ++i)
		wh[i] = wh[i - 1] + 2. * next(i - 1);

	if (L == 0) {
		printf("%.0lf\n", wh[N]);
		return;
	}

	if (L == 1) {
		double ans = wh[N];
		double best = 1e100;
		for(int i = 0; i < N; ++i) {
			best = min(best, ans - 2. * next(i) + Jump(i, wh[i]));
		}
		printf("%.0lf\n", best);
		return;
	}

	double ans = wh[N];
	double best = 1e100;
	for(int i = 0; i < N; ++i) {
		for(int j = i + 1; j < N; ++j) {
			double real_1 = Jump(i, wh[i]);
			double real_2 = Jump(j, wh[i] - real_1 + 2. * next(i));
			double new_res = ans - 2. * (next(i) + next(j)) + real_1 + real_2;
			best = min(best, new_res);
		}
	}
	printf("%.0lf\n", best);
	return;
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t;
	gets(buf);
	t = atoi(buf);
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}
