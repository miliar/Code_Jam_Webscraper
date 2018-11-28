//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

char table[100][128];
int T, t, n;
double OWP[100];
double wp(int x, int ex)
{
	int wins = 0;
	int total = 0;
	for (int i = 0; i < n; ++i)
	{
		if (i == ex) continue;

		if(table[x][i] == '.')
			continue;
		else if (table[x][i] == '1')
		{ ++wins; ++ total; }
		else
		{
			++total;
		}
	}
	return (double)wins / (double) total;
}

double owp(int x)
{
	double total =  0.0;
	int count = 0;
	for (int i = 0; i < n; ++i)
	{
		if (table[x][i] == '1' || table[x][i] == '0')
		{
			total += wp(i, x);
			count += 1;
		}
	}
	return total / count;
}

double oowp(int x)
{
	double total =  0.0;
	int count = 0;
	for (int i = 0; i < n; ++i)
	{
		if (table[x][i] == '1' || table[x][i] == '0')
		{
			total += OWP[i];
			++count;
		}
	}
	return total / count;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%d", &n);
		for (int i = 0; i<n; ++i)
			scanf("%s", table[i]);

		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i)
		{
			OWP[i] = owp(i);
		}
		for (int i = 0; i < n; ++i)
		{
			printf("%.8lf\n", 0.25 * wp(i, -1) + OWP[i] * 0.5 + 0.25 * oowp(i));			
		}
		
	}

	return 0;
}