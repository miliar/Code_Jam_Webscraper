#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 1005

char dat[SZ][SZ];

vector<double> wp;
vector<double> owp;

int n;

double getwp(int ind)
{
	double ret = 0.0;
	double cnt = 0.0;
	int i;
	for(i = 0; i < n; i++)
	{
		if(dat[ind][i] == '.')
			continue;
		if(dat[ind][i] == '1')
			ret = ret + 1.0;
		cnt = cnt + 1.0;
	}
	return (ret / cnt);
}

double getowp(int ind)
{
	double ret = 0.0;
	double cnt = 0.0;
	int i, j;
	for(i = 0; i < n; i++)
	{
		if(i == ind || dat[ind][i] == '.')
			continue;
		double tmp = 0.0;
		double tcnt = 0.0;
		for(j = 0; j < n; j++)
		{
			if(j == ind)
				continue;
			if(dat[i][j] == '.')
				continue;
			if(dat[i][j] == '1')
				tmp = tmp + 1.0;
			tcnt = tcnt + 1.0;
		}
		ret = ret + tmp / tcnt;
		cnt = cnt + 1.0;
	}
	return (ret / cnt);
}

int main()
{
	//freopen("A-small-attempt1.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int inp, tmp, r, kase, k, i, j, pg, pd;
	char ch;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d", &n);
		for(i = 0; i < n; i++)
		{
			scanf(" %s", dat[i]);
		}
		wp.clear();
		owp.clear();
		for(i = 0; i < n; i++)
		{
			double d = getwp(i);
			wp.push_back(d);
			d = getowp(i);
			owp.push_back(d);
		}

		printf("Case #%d:\n", kase);

		for(i = 0; i < n; i++)
		{
			double res = 0.25 * wp[i];
			res = res + 0.5 * owp[i];
			k = 0;
			double tmp = 0;
			for(j = 0; j < n; j++)
			{
				if(i == j || dat[i][j] == '.')
					continue;
				tmp += owp[j];
				k++;
			}
			res = res + 0.25 * tmp / k;
			printf("%.9lf\n", res);
		}

		
		
	}
	return 0;
}

