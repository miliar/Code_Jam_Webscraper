// c2.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <string.h>

int n;
char line[128][128];
double owp_s[128];

double wp(int i)
{
	int ret = 0;
	int c = 0;
	for (int x = 0; x < n; x++)
	{
		if (line[i][x] == '1')
			ret++;
		if (line[i][x] != '.')
			c++;
	}
	return double(ret)/double(c);
}

double wp(int i, int b)
{
	int ret = 0;
	int c = 0;
	for (int x = 0; x < n; x++)
	{
		if (x == b) continue;
		if (line[i][x] == '1')
			ret++;
		if (line[i][x] != '.')
			c++;
	}
	return double(ret)/double(c);
}

double wp(int i, int b, int bb)
{
	int ret = 0;
	int c = 0;
	for (int x = 0; x < n; x++)
	{
		if (x == b) continue;
		if (x == bb) continue;
		if (line[i][x] == '1')
			ret++;
		if (line[i][x] != '.')
			c++;
	}
	return double(ret)/double(c);
}

double owp(int  i)
{
	double ret = 0;
	int c = 0;
	for (int x = 0; x < n; x++)
	{
		if (line[i][x] != '.')
			ret += wp(x, i), c++;
	}
	return double(ret)/double(c);
}



double oowp(int  i)
{
	double ret = 0;
	int c = 0;
	for (int x = 0; x < n; x++)
	{
		if (line[i][x] != '.')
			ret += owp_s[x], c++;
	}
	return double(ret)/double(c);
}

int _tmain(int argc, _TCHAR* argv[])
{
	int c;
	scanf("%d", &c);
	for (int k = 1; k <= c; k++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%s", line[i]);
		double rpi[128];
		memset(rpi, 0, sizeof(rpi));

		//owp
		for (int i = 0; i < n; i++)
			owp_s[i] = owp(i);
		//wp
		for (int i = 0; i < n; i++)
		{
			double wpi = wp(i);
			double owpi = owp_s[i];
			double oowpi = oowp(i);
			rpi[i] = 0.25*wpi + 0.5*owpi + 0.25*oowpi;
		}

		printf("Case #%d:\n", k);
		for (int i = 0; i < n; i++)
			printf("%.7f\n", rpi[i]);
	}
	return 0;
}

