#include <vector>
#include <stdio.h>


using namespace std;

#define NMAX 100


int res[NMAX][NMAX];
double wp[NMAX], owp[NMAX], oowp[NMAX], rpi[NMAX];
int n, t;

void buildwp()
{
	for(int i = 0; i < n; i++)
	{
		double won = 0.0, played = 0.0;
		for(int j = 0; j < n; j++)
		{
			if(res[i][j] == 0)
				continue;
			played += 1.0;
			if(res[i][j] == 1)
				won += 1.0;
		}
		wp[i] = won / played;
	}
}

void buildowp()
{
	for(int i = 0; i < n; i++)
	{
		double wps = 0.0, coms = 0.0;
		for(int j = 0; j < n; j++)
		{
	
			if(i == j)
				continue;
			if(res[i][j] != 0)
			{
				double win = 0.0, played = 0.0;
				for(int k = 0; k < n; k++)
				{
					if(k == i)
						continue;
					if(res[j][k] == 0)
						continue;
					played += 1.0;
					if(res[j][k] == 1)
						win += 1.0;
				}
				wps += win / played;
				coms += 1.0;
			}

		}
		owp[i] = wps / coms;

	}
}

void buildoowp()
{
	for(int i = 0; i < n; i++)
	{
		double owps = 0.0, coms = 0.0;
		for(int j = 0; j < n; j++)
		{
			if(res[i][j] != 0)
			{
				owps += owp[j];
				coms += 1.0;
			}
		}
		oowp[i] = owps / coms;
	}
}

void buildrpi()
{
	for(int i = 0; i < n; i++)
		rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
}

int main()
{
	scanf("%d", &t);
	for(int tst = 0; tst < t; tst++)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				char c;
				scanf("%c", &c);
				while(c != '.' && c != '0' && c != '1') scanf("%c", &c);
				if(c == '0')
					res[i][j] = -1;
				if(c == '1')
					res[i][j] = 1;
				if(c == '.')
					res[i][j] = 0;
			}
		buildwp();
		buildowp();
		buildoowp();
		buildrpi();
		printf("Case #%d:\n", tst + 1);
		for(int i = 0; i < n; i++)
			printf("%.12lf\n", rpi[i]);
	}
	return 0;
}