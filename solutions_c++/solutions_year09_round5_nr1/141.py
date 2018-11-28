#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <algorithm>
using namespace std;

char inp[20][20];
bool curbox[20][20];

const int dx[] = {0, 1, 0, -1};
const int dy[] = {1, 0, -1, 0};

int r, c, n;

#define HASHSIZE 500000

int hash(vector<int> &state)
{
	int v1 = 1, v2 = 1;
	for (int i = 0; i < n; ++i)
	{
		v1 *= state[i] >> 16;
		v2 *= state[i] & 0xFFFF;
	}
	return v1 ^ v2;
}

bool check(vector<int>& state)
{
	int q[20], head = 0, tail = 0, vis[10] = {};
	q[0] = state[0];
	vis[0] = 1;
	while (head <= tail)
	{
		int c = q[head++];
		for (int i = 0; i < n; ++i)
			if (!vis[i] && (abs(state[i] - c) == 1 || abs(state[i] - c) == 1<<16))
			{
				vis[i] = 1;
				q[++tail] = state[i];
			}
	}
	return head == n;
}

map<vector<int>, int> V[HASHSIZE];
void work()
{
	for (int i = 0; i < HASHSIZE; ++i)
		V[i].clear();
	memset(curbox, 0, sizeof(curbox));
	memset(inp, '#', sizeof(inp));
	scanf("%d%d", &r, &c);
	vector<int> boxes, end;
	for (int i = 1; i <= r; ++i)
	{
		scanf("%s", inp[i] + 1);
		for (int j = 1; j <= c; ++j)
		{
			if (inp[i][j] == 'o')
			{
				boxes.push_back(i << 16 | j);
				inp[i][j] = '.';
			}
			if (inp[i][j] == 'w')
			{
				boxes.push_back(i << 16 | j);
				inp[i][j] = 'x';
			}
			if (inp[i][j] == 'x')
			{
				end.push_back(i << 16 | j);
			}
		}
	}
	n = boxes.size();
	sort(boxes.begin(), boxes.end());
	sort(end.begin(), end.end());
	if (boxes == end)
	{
		puts("0");
		return;
	}
	queue<vector<int> > q;
	q.push(boxes);
	V[hash(boxes)].insert(make_pair(boxes, 0));
	while (!q.empty())
	{
		boxes = q.front();
		q.pop();
		vector<int> ns = boxes;
		int step = V[hash(boxes)][boxes];
		int connect = check(ns);
		for (int i = 0; i < n; ++i)
			curbox[boxes[i] >> 16][boxes[i] & 0xFF] = 1;
		for (int i = 0; i < n; ++i)
		{
			int ox = boxes[i] >> 16, oy = boxes[i] & 0xFFFF;
			for (int d = 0; d < 4; ++d)
			{
				int nx = ox + dx[d], ny = oy + dy[d];
				if (inp[nx][ny] == '#' || inp[ox + dx[d ^ 2]][oy + dy[d ^ 2]] == '#')
					continue;
				if (curbox[nx][ny] || curbox[ox + dx[d ^ 2]][oy + dy[d ^ 2]])
					continue;
				ns[i] = nx << 16 | ny;
				if (!connect && !check(ns))
					continue;
				sort(ns.begin(), ns.end());
				if (!V[hash(ns)].insert(make_pair(ns, step + 1)).second)
				{
					ns = boxes;
					continue;
				}
				if (ns == end)
					goto ans;
				q.push(ns);
				//printf("%d %d %d %d        ", ns[0] >> 16, ns[0] & 0xF, ns[1] >> 16, ns[1] & 0xF);
				ns = boxes;
			}
			ns[i] = boxes[i];
		}
		for (int i = 0; i < n; ++i)
			curbox[boxes[i] >> 16][boxes[i] & 0xFF] = 0;
	}
	puts("-1");
	return;
ans:
	printf("%d\n", V[hash(end)][end]);
}

int main()
{
	int t, Test = 0;
	scanf("%d", &t);
	while (t--)
	{
		printf("Case #%d: ", ++Test);
		work();
	}
}
