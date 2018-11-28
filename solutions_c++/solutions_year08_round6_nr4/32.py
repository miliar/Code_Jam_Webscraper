#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>

using namespace std;

#define all(x) (x).begin(),(x).end()

int graph[10][10];
int a[100], b[100];
int c[100], p[100];
int N, M;
string ret;

void go(int k)
{
	if (ret == "YES") return;
	if (k == N)
	{
		for (int i = 0; i < M - 1; ++i)
			if (graph[p[a[i]]][p[b[i]]] == 0) return;
		ret = "YES";
		return;
	}
	for (int i = 0; i < N; ++i)
	{
		if (c[i] == 0)
		{
			p[k] = i;			
			c[i] = 1;
			go(k + 1);
			c[i] = 0;
			p[k] = 0;
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		printf("Case #%d: ", cn);
		cin >> N;
		memset(graph, 0, sizeof(graph));

		for (int i = 0; i < N - 1; ++i)
		{
			int x, y;
			cin >> x >> y;
			x--, y--;
			graph[x][y] = 1;
			graph[y][x] = 1;
		}

		cin >> M;
		ret = "NO";
		for (int i = 0; i < M - 1; ++i)
		{
			cin >> a[i] >> b[i];
			a[i]--; b[i]--;
		}
		go(0);
		cout << ret << endl;
	}
}

