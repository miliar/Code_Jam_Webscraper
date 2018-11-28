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
	long long unsigned int N = get_int();
	int PD = get_int();
	int PG = get_int();

	bool is_possible = true;

	if (PG == 0)
	{
		if (PD != 0) is_possible = false;
	}
	else if (PG == 100)
	{
		if (PD != 100) is_possible = false;
	}
	else
	{
		if (N == 1)
		{
			if (PD != 0 && PD != 100) is_possible = false;
		}
		else if (N < 100)
		{
			bool success = false;

			for (long long unsigned int n=1; n<=N; ++n)
			{
				double coef = 100.f / (double)n;

				for (long long unsigned int i=1; i<n; ++i)
				{
					double p = coef * (double)i;

					if (p == (double)PD)
					{
						success = true;
						break;
					}
				}
			}

			if (success == false) is_possible = false;
		}
	}

	printf("%s", (is_possible) ? "Possible" : "Broken");
}

int main()
{
	int T = get_int();
	FOR (t, T)
	{
		printf("Case #%d: ", t + 1);
		solve();
		printf("\n");
	}
}
