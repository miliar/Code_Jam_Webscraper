#include <cstdio>

#define abs(a) ((a>0)?(a):(-a))

using namespace std;

int a[4][102], p[4], pos[4];

void move(int x) {
	if (pos[x] < a[x][p[x]]) {
		pos[x]++;
	} else if (pos[x] > a[x][p[x]]) {
		pos[x]--;
	}
	return ;
}

int main()
{
	int n;
	scanf("%d", &n);
	for (int i=1; i<=n; i++)
	{
		p[0] = p[1] = p[2] = 0;
		int k;
		scanf("%d", &k);
		for (int j=0; j<k; j++)
		{
			char c; int t;
			scanf("%1s %d", &c, &t);
			if (c == 'O')
			{
				a[0][p[0]++] = 1;
				a[1][p[1]++] = t;
			} else {
				a[0][p[0]++] = 2;
				a[2][p[2]++] = t;
			}
		}
		p[0] = p[1] = p[2] = 0;
		pos[1] = pos[2] = 1;
		int time = 0;
		while (p[0] != k)
		{
			time++;
			int cur = a[0][p[0]];
			if (pos[cur] == a[cur][p[cur]])
			{
				move(3-cur);
				p[0]++;
				p[cur]++;
			} else {
				move(cur);
				move(3-cur);
			}
		}
		printf("Case #%d: %d\n", i, time);
	}
	return 0;
}