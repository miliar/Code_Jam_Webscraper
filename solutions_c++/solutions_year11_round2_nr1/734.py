#include <cstdio>

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w" ,stdout);
	const int N = 111;
	char c[N][N];
	double wp[N], owp[N], oowp[N];
	int cnt[N];
	int test;
	scanf("%d", &test);
	for (int testi = 0; testi < test; ++testi)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%s", c[i]);
		}
		for (int i = 0; i < n; ++i)
		{
			int cnt0 = 0, cnt1 = 0;
			for (int j = 0; j < n; ++j)
			{
				cnt0 += c[i][j] == 48;
				cnt1 += c[i][j] == 49;
			}
			cnt[i] = cnt0 + cnt1;
			if (cnt[i])
			{
				wp[i] = double(cnt1)/cnt[i];
			}
			else
			{
				wp[i] = 0;
			}
			//printf("wp cnt %lf %d\n", wp[i], cnt[i]);
		}
		for (int i = 0; i < n; ++i)
		{
			double sum = 0;
			int ccnt = 0;
			for (int j = 0; j < n; ++j)
			{
				if (c[i][j] == '.')
				{
					continue;
				}
				++ccnt;
				if (cnt[j] > 1)
				{
					sum += ((wp[j] * cnt[j]) - (c[j][i] == 49)) / (cnt[j] - 1);
				}
			}
			if (ccnt > 0)
			{
				owp[i] = sum / ccnt;
			}
			else
			{
				owp[i] = 0;
			}
		}
		for (int i = 0; i < n; ++i)
		{
			
			double sum = 0;
			int cnt = 0;
			for (int j = 0; j < n; ++j)
			{
				if (c[i][j] == '.')
				{
					continue;
				}
				sum += owp[j];
				++cnt;
			}
			if (cnt)
			{
				oowp[i] = sum / cnt;
			}
			else
			{
				oowp[i] = 0;
			}
		}
		
		printf("Case #%d:\n", testi + 1);
		for (int i = 0; i < n; ++i)
		{
			double ans = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.7lf\n", ans);
		}
	}
	return 0;
}