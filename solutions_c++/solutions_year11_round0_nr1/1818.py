#include <stdio.h>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;

const int N = 100 + 5;

int n;
PII p[N];

int Sign(int a)
{
	if (a < 0) return -1;
	if (a > 0) return +1;
	return 0;
}

int Solve()
{
	int res = 0, nn = 0;
	int pos[2] = {1, 1}, next[2] = {1, 1};
	for (int i = 0; i < 2; i++)
		for (int j = 0; j < n; j++)
			if (p[j].first == i)
			{
				next[i] = p[j].second;
				break;
			}
	while (nn < n)
	{
		res++;
		bool pushed = false;
		for (int i = 0; i < 2; i++)
			if (!pushed && p[nn].first == i && p[nn].second == pos[i])
			{
				pushed = true;
				for (int j = nn + 1; j < n; j++)
					if (p[j].first == i)
					{
						next[i] = p[j].second;
						break;
					}
			}
			else
			{
				pos[i] += Sign(next[i] - pos[i]);
			}
		if (pushed) nn++;
	}
	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	for (int tn = 1; tn <= tt; tn++)
	{
		printf("Case #%d: ", tn);
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			char c[2];
			int b;
			scanf("%s %d", c, &b);
			p[i] = make_pair(c[0] == 'O' ? 1 : 0, b);
		}
		printf("%d\n", Solve());
	}
	
	return 0;
}