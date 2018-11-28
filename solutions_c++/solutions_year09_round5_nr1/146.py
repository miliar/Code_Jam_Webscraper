#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
using namespace std;

typedef long long int64;

struct node
{
	char flag;
	unsigned char a[5];
	char pad[3];
};

const int d[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
char a[20][20];
int cnt;
int n, m;
int f[5];

int find(int x)
{
	if (f[x] != f[f[x]]) f[x] = find(f[x]);
	return f[x];
}

bool connect(node &cur)
{
	for (int i = 0; i < cnt; ++i) f[i] = i;
	for (int i = 0; i < cnt; ++i)
		for (int j = i + 1; j < cnt; ++j)
			if (abs(cur.a[i] / m - cur.a[j] / m) + abs(cur.a[i] % m - cur.a[j] % m) == 1)
			{
				int u, v;
				u = find(i);
				v = find(j);
				if (u != v) f[v] = u;
			}
	int ret = 0;
	for (int i = 0; i < cnt; ++i)
		if (find(i) == i) ret++;
	return ret == 1;
}

int main()
{
	freopen("A-small-attempt1.in", "r", stdin); freopen("A.out", "w", stdout);
	int cas, num = 0;
	scanf("%d", &cas);
	while (cas--)
	{
		scanf("%d %d", &n, &m);
		for (int j = 0; j < m + 2; ++j)
			a[0][j] = a[n + 1][j] = '#';
		for (int i = 1; i <= n; ++i)
		{
			a[i][0] = a[i][m + 1] = '#';
			scanf("%s", a[i] + 1);
		}
		cnt = 0;
		node s, t;
		memset(&s, 0, sizeof(node));
		memset(&t, 0, sizeof(node));
		s.flag = t.flag = -1;
		n += 2; m += 2;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (a[i][j] == 'o' || a[i][j] == 'w')
					s.a[cnt++] = i * m + j;
			}
		cnt = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			{
				if (a[i][j] == 'x' || a[i][j] == 'w')
					t.a[cnt++] = i * m + j;
			}
		
		sort(s.a, s.a + cnt);
		sort(t.a, t.a + cnt);
		vector<node> q;
		set<int64> sa;
		sa.insert(*(int64 *)&s);
		q.push_back(s);
		int step, head;
		bool found = false;
		for (step = 0, head = 0; head < q.size(); ++step)
		{
			int old_tail = q.size();
			for (; head < old_tail; ++head)
			{
				node cur = q[head];
				if (*(int64 *)&cur == *(int64 *)&t)
				{
					found = true;
					break;
				}
				if (cur.flag < 0)
				{
					for (int i = 0; i < cnt; ++i)
					{
						int x, y;
						x = cur.a[i] / m;
						y = cur.a[i] % m;
						for (int j = 0; j < 4; ++j)
						{
							int xx, yy;
							int k;
							xx = x - d[j][0];
							yy = y - d[j][1];
							if (a[xx][yy] == '#') continue;
							for (k = 0; k < cnt; ++k)
								if (k != i && (xx * m + yy == cur.a[k])) break;
							if (k < cnt) continue;
							xx = x + d[j][0];
							yy = y + d[j][1];
							if (a[xx][yy] == '#') continue;
							for (k = 0; k < cnt; ++k)
								if (k != i && (xx * m + yy == cur.a[k])) break;
							if (k < cnt) continue;
								
							node next = cur;
							next.a[i] = xx * m + yy;
							if (connect(next)) next.flag = -1;
							else next.flag = 0;
							
							sort(next.a, next.a + cnt);
							if (sa.find(*(int64 *)&next) != sa.end()) continue;
							sa.insert(*(int64 *)&next);
							q.push_back(next);
						}
					}
				}
				else
				{
					for (int i = 0; i < cnt; ++i)
					{
						int x, y;
						x = cur.a[i] / m;
						y = cur.a[i] % m;
						for (int j = 0; j < 4; ++j)
						{
							int xx, yy;
							int k;
							xx = x - d[j][0];
							yy = y - d[j][1];
							if (a[xx][yy] == '#') continue;
							for (k = 0; k < cnt; ++k)
								if (k != i && (xx * m + yy == cur.a[k])) break;
							if (k < cnt) continue;
							xx = x + d[j][0];
							yy = y + d[j][1];
							if (a[xx][yy] == '#') continue;
							for (k = 0; k < cnt; ++k)
								if (k != i && (xx * m + yy == cur.a[k])) break;
							if (k < cnt) continue;
							node next = cur;
							next.a[i] = xx * m + yy;
							
							if (!connect(next)) continue;
							next.flag = -1;
							
							sort(next.a, next.a + cnt);
							if (sa.find(*(int64 *)&next) != sa.end()) continue;
							sa.insert(*(int64 *)&next);
							q.push_back(next);
						}
					}
				}
			}
			if (found) break;
		}
		printf("Case #%d: ", ++num);
		if (!found) puts("-1");
		else printf("%d\n", step);
	}
	return 0;
}
