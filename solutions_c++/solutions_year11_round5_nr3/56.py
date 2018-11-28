#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int t, ct = 0;
int x, y;

int Y[10000][2];
vector<int> X[10000];
int vst[10000], vst2[10000];
bool fail;

queue<int> Q;

void connect (int pos, int x1, int y1, int x2, int y2)
{
	int p1 = x1 * y + y1, p2 = x2 * y + y2;
//	printf ("%d->%d\n", p1, p2);
	
	Y[p1][pos] = p2;
	X[p2].push_back(p1);
}

void del (int x, int y, bool matched)
{
//	printf ("del %d %d %d\n", x, y, (int) matched);
	for (vector<int>::iterator it = X[y].begin(); it != X[y].end(); it ++)
		if (*it == x)
		{
			X[y].erase(it);
			break;
		}
//	X[y].erase(x);
	if (X[y].size() == 1)
		Q.push (y);
	if (matched)
		vst2[y] = true;
	if (X[y].size() == 0 && !vst2[y])
		fail = true;
}

void dfs (int x)
{
	if (vst[x]) return;
	vst[x] = 1;
	for (int i = 0; i < 2; i ++)
		for (int j = 0; j < X[Y[x][i]].size(); j ++)
			dfs (X[Y[x][i]][j]);
}

int solu ()
{
	int ans = 1;
	
	for (int i = 0; i < x * y; i ++)
		vst[i] = 0;
	for (int i = 0; i < x * y; i ++)
		vst2[i] = 0;
	Q=queue<int>();
	for (int i = 0; i < x * y; i ++)
		if (X[i].size() == 1)
		{
			Q.push (i);
		}
		else if (X[i].size() == 0)
			return 0;
	
	fail = false;
	
	while (!Q.empty())
	{
		int i = X[Q.front ()][0], j = Q.front(); Q.pop();
		
		if (vst[i])
			return 0;
		vst[i] = 1;
		
		del (i, Y[i][0], Y[i][0] == j);
		del (i, Y[i][1], Y[i][1] == j);
	}
	
	if (fail) return 0;

	for (int i = 0; i < x * y; i ++)
		if (!vst[i])
		{
			ans = ans * 2 % 1000003;
			dfs (i);
		}

	return ans;
}

int main ()
{
	for (scanf ("%d", &t); t > 0; t --)
	{
		scanf ("%d%d", &x, &y);
		
		for (int i = 0; i < x * y; i ++)
			X[i].clear();
		
		for (int i = 0; i < x; i ++)
			for (int j = 0; j < y; j ++)
			{
				char c;
				
				do scanf ("%c", &c); while (c <= ' ');
				
				int i2, j2;
				switch (c)
				{
					case '-':
						{
							i2 = i;
							j2 = (j + y - 1) % y;
						}
						break;
					case '|':
						{
							i2 = (i + x - 1) % x;
							j2 = j;
						}
						break;
					case '\\':
						{
							i2 = (i + x - 1) % x;
							j2 = (j + y - 1) % y;
						}
						break;
					case '/':
						{
							i2 = (i + x - 1) % x;
							j2 = (j + 1) % y;
						}
				};
				
				connect (0, i, j, i2, j2);

				switch (c)
				{
					case '-':
						{
							i2 = i;
							j2 = (j + 1) % y;
						}
						break;
					case '|':
						{
							i2 = (i + 1) % x;
							j2 = j;
						}
						break;
					case '\\':
						{
							i2 = (i + 1) % x;
							j2 = (j + 1) % y;
						}
						break;
					case '/':
						{
							i2 = (i + 1) % x;
							j2 = (j + y - 1) % y;
						}
				};

				connect (1, i, j, i2, j2);
			}
		
		printf ("Case #%d: %d\n", ++ ct, solu());
	}

	return 0;
}
