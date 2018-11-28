// google code jam problem A

#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

#define INF 0x7f7f7f7f
const int MAXV = 60010;

struct Swing
{
	int d, l;
} sw[MAXV];

int n, D, dp[MAXV];

bool cmp(const Swing &sa, const Swing &sb)
{
	return sa.d < sb.d;
}

bool solve()
{
	int dis;
	for (int i = n - 1; i >= 0; i--)
	{
		dp[i] = INF;
		for (int j = i + 1; j < n; j++)
            if (sw[j].d > sw[i].d + sw[i].l)
                break;
            else
            {
                dis = sw[j].d - sw[i].d < sw[j].l ? sw[j].d - sw[i].d : sw[j].l;
                if (dis >= dp[j])
                {
                    dp[i] = sw[j].d - sw[i].d;
                    break;
                }
            }
		if (sw[i].d + sw[i].l >= D)
			dp[i] = min(dp[i], D - sw[i].d);
	}

	return sw[0].d >= dp[0];
}

int main()
{
    FILE *fin = fopen("a.in", "r");
    FILE *fout = fopen("a.out", "w");
	int testcase;
	fscanf(fin, "%d", &testcase);
	for (int test = 1; test <= testcase; test++)
	{
		fscanf(fin, "%d", &n);
		for (int i = 0; i < n; i++)
			fscanf(fin, "%d%d", &(sw[i].d), &(sw[i].l));
		fscanf(fin, "%d", &D);
		sort(sw, sw + n, cmp);
		fprintf(fout, "Case #%d: ", test);
		if (solve())
			fprintf(fout, "YES\n");
		else
            fprintf(fout, "NO\n");
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
