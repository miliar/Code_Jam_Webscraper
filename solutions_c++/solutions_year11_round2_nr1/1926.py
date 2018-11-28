# include <iostream>
# include <cmath>
# include <algorithm>
# include <list>
# include <string>
# include <vector>
# include <map>
# include <stdio.h>
using namespace std;


int main()
{
	freopen("test.in", "rt", stdin);
	freopen("test.out", "wt", stdout);
	int t;
	scanf("%d ", &t);
	for (int h = 0; h < t; h++)
	{
		int s[105][105] = {0};
		int n;
		scanf("%d ", &n);
		char buf;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				scanf("%c ", &buf);
				if (buf == '0')
					s[i][j] = 1;
				if (buf == '1')
					s[i][j] = 2;
			}
		}
		double res[105] = {0};
		//double wwp[105] = {0};
		double rr = 0;
		int wins[105] = {0};
		//int defs[105] = {0};
		int gams[105] = {0};
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (s[i][j] == 1)
				{
					gams[i]++;
				}
				if (s[i][j] == 2)
				{
					gams[i]++;
					wins[i]++;
				}

			}
		}
		for (int i = 0; i < n; i++)
		{
			double p1 = 0;
			double p3 = 0;
			int c1 = 0;
			for (int j = 0; j < n; j++)
			{
				if (s[i][j] == 1 || s[i][j] == 2)
				{
					c1++;
					double p2 = 0;
					int buf1 = gams[j];
					int buf2 = wins[j];
					buf1--;
					if (s[i][j] == 1 && buf2 > 0)
						buf2--;
					p1 += ((double)buf2 / (double) buf1);
					int c2 = 0;
					for (int k = 0; k < n; k++)
					{
						if (s[j][k] == 1 || s[j][k] == 2)
						{
							c2++;
							int buf11 = gams[k];
							int buf22 = wins[k];
							buf11--;
							if (s[j][k] == 1 && buf22 > 0)
								buf22--;
							p2 += ((double)buf22 / (double) buf11);
						}
					}
					p2 /= (double) c2;
					p3 += p2;
				}
				
			}
			p1 /= (double) c1;
			p3 /= (double) c1;
			res[i] = 0.25 * ((double)wins[i] / (double)gams[i]) + 0.5 * (p1) + 0.25 * (p3);
		}
		printf("Case #%d:\n", h + 1);
		for (int i = 0; i < n; i++)
		{
			printf("%.8lf\n", res[i]);
		}
	}
	return 0;
}