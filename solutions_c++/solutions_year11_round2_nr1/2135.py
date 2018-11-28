#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <string.h>

using namespace std;


char ch[128][128];
int n;
double played[128];
double won[128], owp[128];

void owps()
{
	for(int pos = 0; pos < n; ++pos)
	{
		for(int j = 0; j < n; ++j)
		{
			if(ch[pos][j] != '.')
			{
				if(ch[pos][j] == '1')
				{
					owp[pos] += won[j]/(played[j] - 1);
				}
				else
				{
					owp[pos] += (won[j] - 1) / (played[j] - 1);
				}
			}
		}
		owp[pos] /= played[pos];
	}
}

double rpi(int pos)
{
	double wp = won[pos]/played[pos], oowp = 0;
	for(int j = 0; j < n; ++j)
	{
		if(ch[pos][j] != '.')
		{
			oowp += owp[j];
		}
	}
	oowp /= played[pos];
	return 0.25 * wp + 0.5 * owp[pos] + 0.25 * oowp;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t;

	scanf(" %d ", &t);

	for(int test = 1; test <= t; ++test)
	{
		memset(played, 0, sizeof(played));
		memset(won, 0, sizeof(won));
		memset(owp, 0, sizeof(owp));
		scanf(" %d ", &n);
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < n; ++j)
			{
				scanf(" %c ", &ch[i][j]);
				if(ch[i][j] != '.')
				{
					++played[i];
					if(ch[i][j] == '1')
					{
						++won[i];
					}
				}
			}
		}
		owps();
		printf("Case #%d:\n", test);
		for(int i = 0; i < n; ++i)
		{
			printf("%lf\n", rpi(i));
		}
	}

	return 0;
}
