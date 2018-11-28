#include <cstdio>
#include <algorithm>

using namespace std;

int dist[10000];
int len[10000];
int mm[10000];

int main()
{
	int t;
	scanf("%d", &t);
	for (int c=1; c<=t; ++c)
	{
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; ++i)
		{
			scanf("%d %d", &dist[i], &len[i]);
			mm[i] = 0;
		}

		int to;
		scanf("%d", &to);

		bool ans = false;
		mm[0] = dist[0];
		for (int i=0; i<n; ++i)
		{
			if (dist[i] + mm[i] >= to)
			{
				ans = true;
				break;
			}
			
			for (int j=i+1; j<n; ++j)
			{
				if (mm[i] + dist[i] < dist[j])
					break;

				int temp = min(len[j], dist[j] - dist[i]);
				if (temp > mm[j])
					mm[j] = temp;
			}
		}

		printf("Case #%d: ", c);
		if (ans)
			printf("YES\n");
		else
			printf("NO\n");
	}
	
	return 0;
}