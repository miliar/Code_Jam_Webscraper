#include<iostream>
#include<stdio.h>

using namespace std;

struct data
{
	int win, tot;
};

void cas()
{
	int i, j;
	int n;
	cin >> n;
	char ar[n][n];
	data d[n];
	
	for (i = 0; i < n; i++)
	{
		d[i].win = d[i].tot = 0;
		for (j = 0; j < n; j++)
		{
			cin >> ar[i][j];
			if (ar[i][j] != '.') 
			{
				d[i].tot++;
				if (ar[i][j] == '1') d[i].win++;
			}
		}
	}
	double owp[n];
	double temp;
	for (i = 0; i < n; i++)
	{
		temp = 0.0;
		for (j = 0; j < n; j++)
		{
			if (ar[i][j] == '.') continue;
			if (ar[j][i] == '1') temp += (double)(d[j].win - 1) / (double)(d[j].tot-1);
			else if (ar[j][i] == '0') temp += (double)(d[j].win)/ (double)(d[j].tot-1);
		}
		owp[i] = temp/(double)d[i].tot;
	}
	double oowp[n];
	for (i = 0; i < n; i++)
	{
		temp = 0.0;
		for (j = 0; j < n; j++)
		{
			if (ar[i][j] != '.')
			{
				temp += owp[j];
			}
		}
		oowp[i] = temp/(double)d[i].tot;
	}
	for (i = 0; i < n; i++)
	{
		temp = 0.25 * ((double)d[i].win/(double)d[i].tot) + 0.50 * owp[i] + 0.25 * oowp[i];
		printf("%.12f\n", temp);
	}
	return;
}

int main()
{
	int t, i;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d:\n", i);
		cas();
	}
	return 0;
}
