#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 10001;

int dist[N];
int length[N];
int n;

int maxi[N];

bool solve()
{
	memset(maxi, -1, sizeof(*maxi) * n);
	maxi[0] = dist[0];

	for (int i = 0; i < n; i++)
	{
		if (maxi[i] == -1)
		{
			return false;
		}

		for (int j = i + 1; j < n; j++)
		{
			int d = dist[j] - dist[i];
			if (d > maxi[i])
			{
				break;
			}

			maxi[j] = max(maxi[j], min(d, length[j]));
		}
	}

	return true;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		printf("Case #%d: ", t + 1);
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d %d", dist + i, length + i);
		}
		scanf("%d", dist + n);
		length[n] = 0;
		++n;
		if (solve())
		{
			printf("YES\n");
		}
		else
		{
			printf("NO\n");
		}
	}
}