#include <cstdio>
#include <cstring>

char s[60000];
int q[1<<18];
int step[18][1<<16], test;
void work()
{
	int k;
	scanf("%d%s", &k, s);
	int cnt2[30][30] = {}, cnt[30][30] = {};
	for (int i = 0; s[i]; i += k)
	{
		if (i)
		{
			for (int j = i - k; j < i; ++j)
				for (int t = i; t < i + k; ++t)
					if (s[j] == s[t])
					{
						++cnt2[j - i + k][t - i];
					}
		}
		for (int j = i; j < i + k; ++j)
			for (int t = j + 1; t < i + k; ++t)
				if (s[j] == s[t])
				{
					++cnt[j - i][t - i];
					++cnt[t - i][j - i];
				}
	}
	int len = strlen(s), ans = len;
	for (int front = 0; front < k; ++front)
	{
		memset(step, -1, sizeof(step));
		int head = 0, tail = 0;
		q[0] = front << 19 | (1 << front);
		step[front][1 << front] = 0;
		while (head <= tail)
		{
			int cur = q[head++];
			int curp = cur >> 19, cs = cur & 0xFFFF;
			for (int i = 0; i < k; ++i)
			{
				if (cs & (1 << i))
					continue;
				int ns = cs | (1 << i);
				if (step[i][ns] == -1)
				{
					step[i][ns] = step[curp][cs] + cnt[curp][i];
					q[++tail] = i << 19 | ns;
				}
				else if (step[i][ns] < step[curp][cs] + cnt[curp][i])
					step[i][ns] = step[curp][cs] + cnt[curp][i];
			}
		}
		int t = (1 << k) - 1;
		for (int last = 0; last < k; ++last)
		{
			if (step[last][t] == -1)
				continue;
			if (ans > len - step[last][t] - cnt2[last][front])
				ans = len - step[last][t] - cnt2[last][front];
		}
	}
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
