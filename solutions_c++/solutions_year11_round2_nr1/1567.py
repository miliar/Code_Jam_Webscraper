#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

char table[105][105];
double wp[105];
double owp[105];
double oowp[105];

void GetWP(int index)
{
	int len = strlen(table[index]);
	int i, win, lose;
	win = lose = 0;
	for(i = 0; i < len; i++)
	{
		if(table[index][i] == '.')
			continue;
		else
		{
			if(table[index][i] == '1')
				win++;
			else
				lose++;
		}
	}

	wp[index] = double(win)/double((win+lose));
}

double GetWPAfter(int index, int i)
{
	int len = strlen(table[i]);
	int j;
	int win = 0;
	int lose = 0;
	for(j = 0; j < len; j++)
	{
		if(j == index)continue;
		if(table[i][j] != '.')
		{
			if(table[i][j] == '1')
				win++;
			else
				lose++;
		}
	}
	if(win == 0)
		return 0;
	else
		return double(win)/double(win+lose);
}

void GetOWP(int index)
{
	int len = strlen(table[index]);
	int i;
	double sum = 0;
	int cnt =0;
	for(i = 0; i < len; i++)
	{
		if(table[index][i] != '.')
		{
			sum += GetWPAfter(index, i);
			cnt++;
		}
	}

	owp[index] = sum/cnt;
}

void GetOOWP(int index)
{
	int len = strlen(table[index]);
	int i;
	double sum = 0;
	int cnt =0;
	for(i = 0; i < len; i++)
	{
		if(table[index][i] != '.')
		{
			sum += owp[i];
			cnt++;
		}
	}

	oowp[index] = sum/cnt;
}

double GetRPI(int index)
{
	return 0.25 * wp[index] + 0.50 * owp[index] + 0.25 * oowp[index];
}
int main() {

#define GETANS

#ifdef GETANS
	 freopen("A-large.in","rt",stdin);
	freopen("ans.out","wt",stdout);
#endif

	int c,t;
	c = 0;
	scanf("%d", &t);
	while(t--)
	{
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));

		c++;
		int n;
		int i,j;
		scanf("%d", &n);
		gets(table[0]);
		for(i = 0; i < n; i++)
		{
			gets(table[i]);
			GetWP(i);
		}

		for(i = 0; i < n; i++)
		{
			GetOWP(i);
		}

		for(i = 0; i < n; i++)
		{
			GetOOWP(i);
		}

		
		printf("Case #%d:\n",c);
		for(i = 0; i < n; i++)
		{
			printf("%.10lf\n", GetRPI(i));
		}
	}

	return 0;
}