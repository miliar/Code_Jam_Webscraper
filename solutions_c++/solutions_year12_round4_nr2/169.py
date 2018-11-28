#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAX_N = 2000 + 10;
const int LIM = 5;

int N, flag;
double W, L;
double r[MAX_N], x[MAX_N], y[MAX_N];

double disptop(int u, int v)
{
	return sqrt((x[u] - x[v]) * (x[u] - x[v]) + (y[u] - y[v]) * (y[u] - y[v]));
}

double rand_double(int lim)
{
	return (double)(rand() % 10000) / 10000.0 + rand() % lim;
}

int check(int c)
{
	for(int i = 0; i < c; ++ i)
		if (disptop(i, c) < r[i] + r[c])
			return false;
	return true;
}

void DFS(int cur)
{
	if (cur == N) {
		flag = true;
		return;
	}
	
	for(int i = 0; i < LIM; ++ i) {
		x[cur] = rand_double(W);
		y[cur] = rand_double(L);
		if (check(cur)) {
			DFS(cur + 1);
			if (flag)
				return;
		}
	}
	
}

void solve()
{
	cin >> N >> W >> L;
	for(int i = 0; i < N; ++ i) 
		cin >> r[i];
	flag = false;
	DFS(0);
	for(int i = 0; i < N; ++ i)
		printf("%.10f %.10f ", x[i], y[i]);
	cout << endl;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		solve();
	}
	return 0;
}
