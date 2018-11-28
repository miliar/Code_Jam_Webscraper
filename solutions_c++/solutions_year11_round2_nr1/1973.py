#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <string>

#define FORr(i,A,B)	for (int i=(A); i<(B); ++i)
#define FOR(i, N)	FORr(i,0,N)

using namespace std;

int 	get_int()		{int a; 	scanf("%d", &a); 	return a;}
double	get_double()	{double a;	scanf("%lf", &a);	return a;}
char	get_char()		{char c; 	scanf("%c", &c); 	return c;}

char str_buf[100000];
string	get_str()		{scanf("%s", str_buf); return str_buf;}

void solve()
{
	int N = get_int();

	int table[100][100];
	double WP[100];
	double OWP[100];
	double OOWP[100];

	FOR(y, N)
	{
		string str = get_str();

		FOR(x, N)
		{
			char ch = str.at(x);
			int val = 0;
			switch (ch)
			{
			case '.': val = -1; break;
			case '0': val = 0; break;
			case '1': val = 1; break;
			}
			table[y][x] = val;
		}
	}

	// wp

	FOR(team, N)
	{
		int total = 0;
		int won = 0;

		FOR(op, N)
		{
			if (table[team][op] == -1) continue;
			++total;
			won += table[team][op];
		}

		WP[team] = (double)won / (double)total;
	}

	// owp

	FOR(team, N)
	{
		double sum = 0.f;
		int num = 0;

		FOR(op, N)
		{
			if (table[op][team] == -1) continue;

			int total = 0;
			int won = 0;

			FOR(opop, N)
			{
				if (opop == team) continue;
				if (table[op][opop] == -1) continue;

				++total;
				won += table[op][opop];
			}

			sum += (double)won / (double)total;
			++num;
		}

		OWP[team] = sum / (double)num;
	}

	// oowp

	FOR(team, N)
	{
		double sum = 0.f;
		int num = 0;

		FOR(op, N)
		{
			if (table[op][team] == -1) continue;

			sum += OWP[op];
			++num;
		}

		OOWP[team] = sum / (double)num;
	}

	// RPI

	FOR(team, N)
	{
		printf("%.12f\n", 0.25f * WP[team] + 0.5f * OWP[team] + 0.25f * OOWP[team]);
	}
}

int main()
{
	int T = get_int();
	FOR (t, T)
	{
		printf("Case #%d:\n", t + 1);
		solve();
//		printf("\n");
	}
}
