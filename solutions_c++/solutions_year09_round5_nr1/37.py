#include <iostream>
#include <fstream>
#include <strstream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

#define cin fin
#define cout fout

#define LIMIT 390001

int d[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};

long ans;
char map[20][20];
int n, m;

int target[6];
int tlen;

struct Tstat {
	int box[6];
	int cost;
};

vector <Tstat> que;

vector <Tstat> table[LIMIT];

int visit[6];

void init()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
			while (!(map[i][j] == '.' || map[i][j] == '#' || map[i][j] == 'x' || map[i][j] == 'o' || map[i][j] == 'w'))
			{
				cin >> map[i][j];
			}
		}

	for (int i = 0; i < LIMIT; i++)
		table[i].clear();
	que.clear();
}

bool istarget(Tstat &newB)
{
	for (int i = 0; i < tlen; i++)
		if (newB.box[i] != target[i]) return false;
	return true;
}

bool update(Tstat &box)
{
	unsigned long key = 0;
	for (int i = 0; i < tlen; i++)
		key = ((key << 8) + box.box[i]) % LIMIT;

	int ll = table[key].size();
	for (int i = 0; i < ll; i++)
	{
		bool flag = true;
		for (int j = 0; j < tlen; j++)
			if (table[key][i].box[j] != box.box[j])
			{
				flag = false;
				break;
			}
		if (flag) return false;
	}

	table[key].push_back(box);

	return true;
}

bool check(int x, int y, int * org)
{
	if (x >= 0 && x < n && y >= 0 && y < m)
	{
		if (map[x][y] == '#') return false;
		for (int i = 0; i < tlen; i++)
			if (org[i] == x * m + y) return false;
		return true;
	} else 
		return false;
}

void dfs(int now, int * a)
{
	int x0, x1, y0, y1;

	visit[now] = 1;
	for (int i = 0; i < tlen; i++)
	if (visit[i] == 0)
	{
		x0 = a[now] / m;
		y0 = a[now] % m;
		x1 = a[i] / m;
		y1 = a[i] % m;

		if (labs(x0-x1) + labs(y0-y1) == 1)
			dfs(i, a);
	}
}

bool dang(int * a)
{
	memset(visit, 0, sizeof(visit));
	dfs(0, a);
	for (int i = 0; i < tlen; i++)
		if (visit[i] == 0) return false;
	return true;
}

bool expand(int *org, int id, int dire, int *dest)
{
	bool org_safe = dang(org);

	int temp;

	int x0 = org[id] / m;
	int y0 = org[id] % m;

	int x1 = x0 + d[dire][0];
	int y1 = y0 + d[dire][1];

	int x2 = x0 - d[dire][0];
	int y2 = y0 - d[dire][1];

	if (check(x1, y1, org) == true && check(x2, y2, org) == true)
	{
		for (int i = 0; i < tlen; i++)
			dest[i] = org[i];
		
		dest[id] = x1 * m + y1;

		while (id > 0 && dest[id] < dest[id-1])
		{
			temp = dest[id]; dest[id] = dest[id-1]; dest[id-1] = temp;
			id--;
		}

		while (id < tlen-1 && dest[id] > dest[id+1])
		{
			temp = dest[id]; dest[id] = dest[id+1]; dest[id+1] = temp;
			id++;
		}		

		bool dest_safe = dang(dest);

		if (org_safe == true || (org_safe == false && dest_safe == true))
			return true;
		else
			return false;
	}

	return false;
}

void solve()
{
	tlen = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 'w' || map[i][j] == 'x')
				target[tlen++] = i*m+j;
		}

	Tstat newB;
	newB.cost = 0;

	int tmp = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			if (map[i][j] == 'o' || map[i][j] == 'w') 
				newB.box[tmp++] = i*m+j;
		}

	int head, tail;

	que.push_back(newB);
	update(newB);

	head = tail = 0;

	while (head <= tail)
	{
		if (istarget(que[head]) == true)
		{
			ans = que[head].cost;
			return;
		}

		for (int i = 0; i < tlen; i++)
			for (int j = 0; j < 4; j++)
			{
				newB.cost = que[head].cost + 1;
				if (expand(que[head].box, i, j, newB.box) == true)
				{
					if (update(newB) == true)
					{
						que.push_back(newB);
						tail++;
					}
				}
			}
		head++;
	}
}

int main()
{
	int cases;

	cin >> cases;
	for (int i = 0; i < cases; i++)
	{
		init();

		ans = -1;
		solve();

		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;
}