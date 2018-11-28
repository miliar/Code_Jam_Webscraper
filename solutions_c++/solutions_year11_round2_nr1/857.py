#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

const int MAXN = 105;

int n;
double wp[MAXN], owp[MAXN], oowp[MAXN], wp_l[MAXN][MAXN];
char mm[MAXN][MAXN];

void go()
{
	for(int i = 0; i < n; i++)
	{
		double a = 0, b = 0;
		for(int j = 0; j < n; j++)
		{
			if(mm[i][j] != '.')  b++;
			if(mm[i][j] == '1')  a++;
		}
		wp[i] = a / b;


		for(int k = 0; k < n; k++)
		{
			double a = 0, b = 0;
			for(int j = 0; j < n; j++)
			{
				if(j == k)  continue;

				if(mm[i][j] != '.')  b++;
				if(mm[i][j] == '1')  a++;

				wp_l[i][k] = a / b;
			}
		}
	}

	/*
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < n; j++)
			printf("%lf ", wp_l[i][j]);
		printf("\n");
	}
	*/

	for(int i = 0; i < n; i++)
	{
		double a = 0, b = 0;
		for(int j = 0; j < n; j++)  if(mm[i][j] != '.')
		{
			a += wp_l[j][i];
			b++;
		}
		owp[i] = a / b;
	}

	for(int i = 0; i < n; i++)
	{
		double a = 0, b = 0;
		for(int j = 0; j < n; j++)  if(mm[i][j] != '.')
		{
			a += owp[j];
			b++;
		}
		oowp[i] = a / b;
	}

	
	for(int i = 0; i < n; i++)
	{
		//printf("#%lf %lf %lf\n", wp[i], owp[i], oowp[i]);
		double rpi = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
		printf("%.8lf\n", rpi);
	}
}

int main()
{
	freopen("d:\\Desktop\\GCJ\\A-large (1).in", "r", stdin);
	freopen("d:\\Desktop\\GCJ\\A-large (1).out", "w", stdout);
	
	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d:\n", ++c);
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%s", mm[i]);
		go();

	}
}