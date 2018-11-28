#include <cstdio>
using namespace std;

int n;
char shed[101][101];

int OP[101], WIN[101];

double WP[101];
double OWP[101];
double OOWP[101];

void countwp()
{
	for(int i = 1; i <= n; ++i)
	{
		for(int j = 1; j <= n; ++j)
		{
			if(shed[i][j] != '.') OP[i]++;
			if(shed[i][j] == '1') WIN[i]++;
		}
		WP[i] = (double) WIN[i] / OP[i];
	}
}

void countowp()
{
	for(int i = 1; i <= n; ++i)
	{
		double sum = 0;
		int opp = 0;
		
		for(int j = 1; j <= n; ++j)
		{
			if(shed[i][j] != '.')
			{
				sum += (double) (WIN[j] - (shed[j][i] == '1')) / (OP[j] - 1);
				opp++;
			}
		}
		
		OWP[i] = sum / opp;
	}
}

void countoowp()
{
	for(int i = 1; i <= n; ++i)
	{
		double sum = 0;
		int opp = 0;
		
		for(int j = 1; j <= n; ++j)
		{
			if(shed[i][j] != '.')
			{
				sum += OWP[j];
				opp++;
			}
		}
		
		OOWP[i] = sum / opp;
	}
}

int main()
{
	int t; scanf("%i", &t);
	
	for(int k = 1; k <= t; ++k)
	{
		scanf("%i", &n);
		
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= n; ++j)
				scanf("%1s", &shed[i][j]);
		
		countwp();
		countowp();
		countoowp();
		
		printf("Case #%i:\n", k);
		for(int i = 1; i <= n; ++i)
			printf("%.7lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		
		for(int i = 1; i <= n; ++i) OP[i] = WIN[i] = WP[i] = OWP[i] = OOWP[i] = 0;
		
	}
	return 0;
}
