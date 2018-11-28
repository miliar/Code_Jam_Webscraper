#include <cstdio>
#include <cstring>

int Add(int a, int b)
{
	return (((a^b) & 0xFFFFFFFE) | ((a+b) & 0x01));
}

int Sub(int a, int b)
{
	return (((a^b) & 0xFFFFFFFE) | ((a-b) & 0x01));
}

int main()
{
	int T, t, i, j, sum, val, v1, N, resp;
	int v[1048575][2];
	int n[1000];

	scanf("%d", &T);
	for (t = 1; t <= T; t++)
	{
		memset(v, 0, sizeof(v));
		sum = val = 0;
		resp = 0;

		scanf("%d", &N);
		for (i = 0; i < N; i++)
		{
			scanf("%d", &n[i]);
			val = Add(val, n[i]);
			sum += n[i];
		}

		for (i = 0; i < N; i++)
		{
			v1 = Add(0, n[i]);
			v[v1][0] = Sub(val, n[i]);;
			v[v1][1] = n[i];
		}

		for (i = 0; i <= 1048575; i++)
		{
			if (v[i][1])
			{
				if (i == v[i][0] && (resp < v[i][1]))
				{
					resp = v[i][1];
				}

				if (i == v[i][0] && (resp < sum - v[i][1]))
				{
					resp = sum - v[i][1];
				}

				for (j = i + 1; j < N; j++)
				{
					v1 = Add(i, n[j]);
					if (v[v1][1] == 0)
					{
						v[v1][0] = Sub(v[i][0], n[j]);
						v[v1][1] = v[i][1] + n[i];
					}
				}
			}
		}

		if (resp > 0)
		{
			printf("Case #%d: %d\n", t, resp);
		}
		else
		{
			printf("Case #%d: NO\n", t);
		}
	}

	return 0;
}
