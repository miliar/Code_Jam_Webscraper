#include <cstdio>
#include <memory>

int N;
int map[60];

bool fin()
{
	for (int i=1; i<=N; i++)
	{
		if (map[i] > i)
			return false;
	}
	return true;
}

void mswap(int &a, int &b)
{
	int k = a;
	a = b;
	b = k;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		memset(map,0,sizeof(map));
		scanf("%d", &N);
		for (int i=1; i<=N; i++)
		{
			char buf[100];
			scanf("%s", buf);
			for (int j=0; j<N; j++)
			{
				if (buf[j] == '1')
					map[i] = j+1;
			}
		}

		int res = 0;
		for (int i=1; i<N; i++)
		{
			int j = i;
			while (j <= N && map[j] > i)
			{
				j++;
			}
			if (j == i)
				continue;
			while(j != i)
			{
				res++;
				mswap(map[j], map[j-1]);
				j--;
			}
		}

		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}