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
#include <ctime>
#include <memory.h>

using namespace std;

struct Button
{
	int ind;
	bool blue;
	Button(int ind = 1, bool blue = false)
	{
		this->ind = 0;
		this->blue = blue;
	}
};

int n;
Button b[111];
char s[11];
int d[102][102][102];

struct State
{
	int i, j, k;
};
int bfs()
{
	State st;
	st.i = 0;
	st.j = 0;
	st.k = 0;
	memset(d, -1, sizeof(d));
	int i = 0, j = 0, k = 0;
	d[i][j][k] = 0;
	queue<State> q;
	q.push(st);
	while (!q.empty())
	{
		st = q.front();
		i = st.i; j = st.j; k = st.k;
		q.pop();
		if (k == n)
			return d[i][j][k];
		for (int di = -1; di <= 1; ++di)
		{
			for (int dj = -1; dj <= 1; ++dj)
			{
				int ni = i + di, nj = j + dj, nk = k;
				if (ni >= 0 && ni < 100 && nj >= 0 && nj < 100)
				{
					if (d[ni][nj][nk] == -1)
					{
						d[ni][nj][nk] = d[i][j][k] + 1;
						st.i = ni; st.j = nj; st.k = nk;
						q.push(st);
					}
				}
			}
		}
		for (int di = -1; di <= 1; ++di)
		{
			int ni = i + di, nj = j, nk = k + 1;
			if (ni >= 0 && ni < 100 && b[nk].blue && b[nk].ind == nj)
			{
				if (d[ni][nj][nk] == -1)
				{
					d[ni][nj][nk] = d[i][j][k] + 1;
					st.i = ni; st.j = nj; st.k = nk;
					q.push(st);
				}
			}
		}
		for (int dj = -1; dj <= 1; ++dj)
		{
			int ni = i, nj = j + dj, nk = k + 1;
			if (nj >= 0 && nj < 100 && !b[nk].blue && b[nk].ind == ni)
			{
				if (d[ni][nj][nk] == -1)
				{
					d[ni][nj][nk] = d[i][j][k] + 1;
					st.i = ni; st.j = nj; st.k = nk;
					q.push(st);
				}
			}
		}
	}
	return -1;
}
int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
		{
			int ind = 1;
			scanf("%s %d", s , &ind);
			b[i].ind = ind - 1;
			b[i].blue = (s[0] == 'B');
		}
		printf("Case #%d: %d\n", t + 1, bfs());
	}

	
	return 0;
}
