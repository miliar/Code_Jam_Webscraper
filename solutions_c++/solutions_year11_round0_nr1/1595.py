#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 101;

char OP(char x) { return x == 'B' ? 'O' : 'B'; }
int go_and_push(int &pos, int dest)
{
	int ret = abs(dest - pos) + 1;
	pos = dest;
	return ret;
}

int dir(int a, int b)
{
	if (a == b) return 0;
	if (a < b)
		return 1;
	return -1;
}

int go(int &pos, int dest, int max_step)
{
	if (dest == -1)
		return 0;
	int step = abs(dest - pos);
	pos += min(step, max_step) * dir(pos, dest);
	return min(step, max_step);
}

int n;
char rob[N][2];
int pos[N];

int find(int start, char r)
{
	for (int i = start; i <= n; i ++)
		if (rob[i][0] == r)
			return pos[i];
	return -1;
}


void solve(int cid)
{
	scanf("%d", &n);
	for (int i = 1; i <= n; i ++)
		scanf("%s%d", rob[i], pos + i);

	int ans = 0;
	int p[2] = {1, 1};
	for (int i = 1; i <= n; i ++)
	{
		int id = (rob[i][0] == 'B'),
			v = go_and_push(p[id], pos[i]);
		ans += v;
		go(p[id ^ 1], find(i + 1, OP(rob[i][0])), v);
	}
	printf("Case #%d: %d\n", cid, ans);
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++)
		solve(i);
}

