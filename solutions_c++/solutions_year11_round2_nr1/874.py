#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

struct Team
{
	double w;
	double l;
	double wp;
	double owp;
	double oowp;
	double res;
	void calc1()
	{
		wp = w / (w+l);
	}
	void final()
	{
		res = 0.25 * wp + 0.5 * owp + 0.25 *oowp;
	}
};

int main()
{
	int Q;
	scanf("%d", &Q);
	
	for (int q = 1; q <= Q; ++q)
	{
		printf("Case #%d:\n", q);
		int n;
		scanf("%d", &n);
		Team teams[n];
		string mines[n];
		memset(teams, 0, sizeof teams);
		string in;
		for (int i = 0; i < n; ++i)
		{
			cin >> in;
			mines[i] = in;
			for (int j = 0; j < in.size(); ++j)
			{
				if (in[j] == '.')
					continue;
				if (in[j] == '1')
					teams[i].w++;
				else
					teams[i].l++;
			}
			teams[i].calc1();
		}
		for (int i = 0; i < n; ++i)
		{
			double owp = 0;
			double d = 0;
			for (int j = 0; j < n; ++j)
			{
				if (j == i)
					continue;
				double w = teams[j].w;
				double l = teams[j].l;
				if (mines[i][j] == '0')
					--w;
				else if (mines[i][j] == '1')
					--l;
				else
					continue;
				++d;
				owp += w/(w+l);
			}
			owp /= d;
			teams[i].owp = owp;
		}
		for (int i = 0; i < n; ++i)
		{
			double oowp = 0;
			double d = 0;
			for (int j = 0; j < n; ++j)
			{
				if (i == j)
					continue;
				if (mines[i][j] == '.')
					continue;
				oowp += teams[j].owp;
				++d;
			}
			oowp /= d;
			teams[i].oowp = oowp;
			teams[i].final();
		}
		for (int i = 0; i < n; ++i)
		{
			printf("%lf\n", teams[i].res);
		}
	}
	
	return 0;
}

