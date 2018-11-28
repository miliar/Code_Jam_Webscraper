#include <cstdio>

int R, k, N;
int T;
int g[2005];
int m[1005];
int t[1005];

int getNextIndex(int i, int &val)
{
	int l = i+N;
	val = 0;
	for(; i < l; i++)
	{
		val += g[i];
		if (val + g[i+1] > k)
			break;
	}
	i++;
	while (i >= N)
		i -= N;
	return i;
}

int main()
{
	freopen("p3.in", "r", stdin);
	freopen("p3.out", "w", stdout);

	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; caseNum++)
	{
		scanf("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i++)
		{
			scanf("%d", &g[i]);
			g[i+N] = g[i];
			t[i] = -1;
		}
		g[2*N] = g[0];
		int time, pos = 0;
		int am = 0;
		for (time = 0; time < R; time++)
		{
			if (t[pos] == -1)
			{
				t[pos] = time;
				m[pos] = am;
			}
			else
				break;
			int tmp = pos, tmp2;
			pos = getNextIndex(pos, tmp2);
			am += tmp2;
		}
		if (time < R)
		{
			int ts = time - t[pos];
			int kk = (R - time) / ts;
			am += kk * (am - m[pos]);
			time += kk*ts;
			for (; time < R; time++)
			{
				int tmp = pos, tmp2;
				pos = getNextIndex(pos, tmp2);
				am += tmp2;
			}
		}

		printf("Case #%d: ", caseNum);
		printf("%d\n", am);
		// ANSWER
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
