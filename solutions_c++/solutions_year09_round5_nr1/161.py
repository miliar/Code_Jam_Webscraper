#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

const int MAX_N = 14;
const int MAX_Q = 1000000;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

typedef set< pair<int, int> > state;

char a[MAX_N][MAX_N], b[MAX_N][MAX_N];
int m, n, nBox, cnt;

map<state, int> f;
state finish, start;
state q[MAX_Q];
bool mark[MAX_N][MAX_N];
bool pos[MAX_N][MAX_N];
int front, rear;

void enter()
{
	cin >> m >> n;
	start.clear();
	finish.clear();
	for (int i = 0; i < MAX_N; ++i)
		for (int j = 0; j < MAX_N; ++j)
			a[i][j] = '#';
	nBox = 0;
	for (int i = 1; i <= m; ++i)
		for (int j = 1; j <= n; ++j)
		{
			cin >> a[i][j];
			if (a[i][j] == 'o' || a[i][j] == 'w')
			{
				start.insert(pair<int, int>(i, j));
				++nBox;
			}
			if (a[i][j] == 'x' || a[i][j] == 'w')
			{
				finish.insert(pair<int, int>(i, j));
			}
		}
}

void dfs(int x, int y)
{
	if (cnt == nBox) return;
	mark[x][y] = false;
	for (int k = 0; k < 4; ++k)
	{
		int u = x + dx[k];
		int v = y + dy[k];
		if (a[u][v] != '#' && mark[u][v])
		{
			if (pos[u][v])
			{
				++cnt;
				if (cnt == nBox) return;
				else dfs(u, v);
			}
		}
	}
	if (cnt == nBox) return;
}

bool isStable(state s)
{
	vector< pair<int, int> > vs;
	vs.clear();
	for (state::iterator it = s.begin(); it != s.end(); ++it)
	{
		vs.push_back(*it);
	}
	memset(mark, true, sizeof(mark));
	memset(pos, false, sizeof(pos));
	for (int i = 0; i < nBox; ++i)
	{
		pos[vs[i].first][vs[i].second] = true;
	}
	cnt = 1;
	dfs(vs[0].first, vs[0].second);
	return (cnt == nBox);
}

int bfs()
{
	front = rear = 0;
	q[0] = start;
	f.clear();
	f[start] = 1;
	while (front <= rear)
	{
		state x = q[front++];
		
		int d = f[x];
		
		if (x == finish)
		{
			return d - 1;
		}
		
		for (int i = 0; i < MAX_N; ++i)
			for (int j = 0; j < MAX_N; ++j)
				if (a[i][j] != '#') b[i][j] = '.';
				else b[i][j] = a[i][j];
				
		vector< pair<int, int> > vs;
		vs.clear();
		for (state::iterator it = x.begin(); it != x.end(); ++it)
		{
			vs.push_back(*it);
			int u = vs[vs.size() - 1].first;
			int v = vs[vs.size() - 1].second;
			b[u][v] = 'o';
		}
			
		for (int j = 0; j < nBox; ++j)
		{
			int x0 = vs[j].first;
			int y0 = vs[j].second;
			
			for (int i = 0; i < 4; ++i)
			{
				int tu = x0 - dx[i];
				int tv = y0 - dy[i];
				int u = x0 + dx[i];
				int v = y0 + dy[i];
				if (b[tu][tv] == '.' && b[u][v] == '.')
				{
					state y = x;
					state::iterator it = y.begin();
					for (int jj = 0; jj < j; ++jj)
						++it;
					y.erase(it);
					y.insert(pair<int, int>(u, v));
					if (isStable(x) || isStable(y))
					{
						if (y == finish) return d;
						int i = f[y];
						if (i == 0)
						{
							f[y] = d + 1;
							q[++rear] = y;
						}
					}
				}
				
			}
			
		}
	}
	
	return -1;
}

int main()
{
	int nTest;
	cin >> nTest;
	for (int i = 1; i <= nTest; ++i)
	{
		cout << "Case #" << i << ": ";
		
		enter();
		cout << bfs() << endl;
	}
	
	return 0;
}
