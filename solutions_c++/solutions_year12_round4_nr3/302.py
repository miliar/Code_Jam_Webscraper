#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 2010;
int see[N], h[N];

const double tH = 100010;

int main ()
{
	freopen("in.txt", "r", stdin);
	FILE *fp = fopen("out.txt", "w");
	int T; scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT)
	{
		int n; scanf("%d", &n);
		for (int i = 0; i < n - 1; i++) scanf("%d", &see[i]), --see[i], h[i] = 0;
		h[n - 1] = 0;
		bool ok = true;
		for (int i = 0; i < n - 1 && ok; i++)
		{
			if (see[i] <= i || see[i] >= n) { ok = false; break; }
			for (int j = i + 1; j < see[i] && ok; j++)
			{
				if (h[j]) ok = false;
			}
			if (!ok) break;
			if (!h[i]) h[i] = 1;
			int tt = i - 1;
			for (; tt >= 0; --tt)
			{
				if (see[tt] > i) break;
			}
			if (tt == -1) h[see[i]] = h[i] + tH * (see[i] - i);
			else
			{
				double kH = (double)(h[see[tt]] - h[tt]) / (see[tt] - tt) * (see[i] - tt) + h[tt];
				double rH = (double)(h[see[tt]] - h[i]) / (see[tt] - i) * (see[i] - i) + h[i];
				if ((int)floor(kH) >= (int)ceil(rH))
				{
					h[see[i]] = (int)ceil(rH);
				}
				else { printf("Case #%d: tH is too small. %f %f %d %d %d %d\n", TT, kH, rH, i + 1, see[i] + 1, tt + 1, see[tt] + 1); }
			}
			// printf("Case #%d: set %d to %d\n", TT, see[i] + 1, h[see[i]]);
			if (h[see[i]] > 1000000000) { printf("Case #%d: tH is too high.\n", TT); while (1); }
		}
		if (!ok) fprintf(fp, "Case #%d: Impossible\n", TT);
		else
		{
			fprintf(fp, "Case #%d:", TT);
			for (int i = 0; i < n; i++) fprintf(fp, " %d", h[i]);
			fprintf(fp, "\n");
		}
	}
	fclose(stdin);
	fclose(fp);
	// while (1);
	return 0;
}
