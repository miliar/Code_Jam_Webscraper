#include<cstdio>
#include<cstring>

bool visit[1010];
int counter[1010];
int n;

int per[1010];


int main()
{
    freopen("D-large.in","r", stdin);
    freopen("output.txt","w", stdout);
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			int x;
			scanf("%d" , &x);
			per[i] = x - 1;
		}
		memset( counter,  0, sizeof(counter));
		memset(visit, false, sizeof(visit));
		for (int i = 0; i < n; ++i)
			if (!visit[i])
			{
				int j = per[i];
				int total = 1;
				visit[i] = true;
				while (!visit[j])
				{
					++total;
					visit[j] = true;
					j = per[j];
				}
				++counter[total];
			}
		double ans = 0;
		for (int i = 2; i <= n; ++i)
			ans += counter[i] * i;
		printf("Case #%d: %.6lf\n", ca, ans);

	}

}
