#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

typedef struct
{
	int now;
	int step;
} Rec;

int edge[440][440];
int graph[440][440];
int n[440];
int P, W;
bool visit[440];

int get_step ()
{
	queue <Rec> que;


	for (int i=0 ;i<P ;i++)
		visit[i] = false;

	visit[0] = true;
	Rec curr;
	curr.now = 0;
	curr.step = 0;
	que.push (curr);

	while (!que.empty())
	{
		curr = que.front();
		que.pop ();

		if (curr.now==1)
			return curr.step;

		for (int i=0 ;i<n[curr.now] ;i++)
		{
			int x = edge[curr.now][i];
			if (!visit[x])
			{
				visit[x] = true;
				Rec next;
				next.now = x;
				next.step = curr.step+1;
				que.push (next);
			}
		}
	}
}

int limit;
int max_dom = 0;
bool dom[440];

void DFS (int curr, int step, int num)
{
	if (step>limit)
		return;

	if (graph[curr][1])
	{
		if (num > max_dom)
			max_dom = num;
	}
	else
	{
		for (int i=0 ;i<n[curr] ;i++)
		{
			int x = edge[curr][i];
			if (!visit[x])
			{
				visit[x] = true;
				vector <int> mem;
				int d = num;
				for (int j=0 ;j<n[x] ;j++)
				{
					if (!dom[edge[x][j]])
					{
						d++;
						dom[edge[x][j]] = true;
						mem.push_back (edge[x][j]);
					}
				}
				DFS (x, step+1, d-1);
				for (int j=0 ;j<mem.size() ;j++)
					dom[mem[j]] = false;
				visit[x] = false;
			}
		}
	}
}

void solve_case ()
{
	cin >> P >> W;
	for (int i=0 ;i<P ;i++)
		n[i] = 0;
	for (int i=0 ;i<P ;i++)
	{
		for (int j=0 ;j<P ;j++)
			graph[i][j] = 0;
	}
	for (int i=0 ;i<W ;i++)
	{
		char dum;
		int x, y;
		cin >> x >> dum >> y;
		edge[x][n[x]++] = y;
		edge[y][n[y]++] = x;
		graph[x][y] = graph[y][x] = 1;
	}

	int ans = get_step() - 1;
	limit = ans;

	for (int i=0 ;i<P ;i++)
		visit[i] = false;
	visit[0] = true;
	for (int i=0 ;i<P ;i++)
		dom[i] = false;
	dom[0] = true;
	int d = 0;
	for (int i=0 ;i<n[0] ;i++)
	{
		int x = edge[0][i];
		dom[x] = true;
		d++;
	}
	max_dom = 0;
	DFS (0, 0, d);
	cout << ans << " " << max_dom;

	cout << endl;
}

int main ()
{
	int total_cases;

	cin >> total_cases;
	for (int cases=1 ;cases<=total_cases ;cases++)
	{
		cout << "Case #" << cases << ": ";
		solve_case ();
	}

	return 0;
}
