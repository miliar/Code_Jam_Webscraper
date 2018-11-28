#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAX = 1005, M = 30;
double comb[M][M], p[M];
double dp[MAX];
int n;

void init()
{
	for(int i = 0; i < M; i ++)
		comb[i][0] = comb[i][i] = 1;
	for(int i = 2; i < M; i ++)
		for(int j = 1; j < i; j ++)
			comb[i][j] = comb[i-1][j-1] + comb[i-1][j];

	p[1] = 1;
	for(int i = 2; i < M; i ++)
		p[i] = p[i-1] * i;
	p[0] = 1, p[1] = 0, p[2] = 1;
	for(int i = 3; i < M; i ++)
		for(int j = 1; j <= i; j ++)
			p[i] -= comb[i][j] * p[i-j];
	for(int i = 1; i < M; i ++)
		for(int j = 1; j <= i; j ++)
			p[i] /= j;

	dp[0] = dp[1] = 0, dp[2] = 2;
	for(int i = 3; i < MAX; i ++)
	{
		dp[i] = 0;
		for(int j = 1; j <= i && j < M; j ++)
		{
			double t = dp[i-j] * (i-j>=M?p[M-1]:p[i-j]);
			for(int k = 1; k <= j; k ++)
				t /= k;
			dp[i] += t;
		}
		double temp = i >= M?p[M-1]:p[i];
		dp[i] = (dp[i]+1)/(1-temp);
	}
}
int main()
{
	init();
	FILE *f1 = fopen("input.in", "r");
	FILE *f2 = fopen("out.in", "w");
	int numcas;
	fscanf(f1, "%d", &numcas);
	for(int cas = 1; cas <= numcas; cas ++)
	{
		fscanf(f1, "%d", &n);
		int cnt = 0;
		for(int i = 0; i < n; i ++)
		{
			int v;
			fscanf(f1, "%d", &v);
			if(v != i+1) cnt ++;
		}
		if(dp[cnt] > -1e-10 && dp[cnt] < 1e-10)
			fprintf(f2, "Case #%d: 0\n", cas);
		else
			fprintf(f2, "Case #%d: %.6lf\n", cas, dp[cnt]+1e-10);
	}
	fclose(f1);
	fclose(f2);

	return 0;
}