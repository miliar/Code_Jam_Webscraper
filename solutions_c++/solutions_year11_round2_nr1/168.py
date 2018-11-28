#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

#define m 111

int n;
char s[m][m];
double wp[m], owp[m], oowp[m];

double getwp(int i, int f)
{
	int wins = 0, loses = 0;
	for(int j = 0; j < n; j++) if(j != f)
		if(s[i][j] == '1') wins++;
		else if(s[i][j] == '0') loses++;
	return 1.0 * wins / (wins + loses);
}

double getowp(int i)
{
	double sum = 0;
	int games = 0;
	for(int j = 0; j < n; j++) if(s[i][j] != '.')
	{
		games++;
		sum += getwp(j,i);
	}
	if(games == 0) return 0;
	return sum / games;
}

void test()
{
	scanf("%d", &n);
	for(int i = 0; i < n; i++) scanf("%s", s[i]);
	for(int i = 0; i < n; i++) wp[i] = getwp(i, n);
	for(int i = 0; i < n; i++) owp[i] = getowp(i);
	for(int i = 0; i < n; i++)
	{
		int games = 0;
		double sum = 0;
		for(int j = 0; j < n; j++) if(s[i][j] != '.')
		{
			games++;
			sum += getowp(j);
		}
		if(games == 0) oowp[i] = 0;
		else oowp[i] = sum / games;
	}
	for(int i = 0; i < n; i++) printf("%.7lf\n", wp[i]/4+owp[i]/2+oowp[i]/4);
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d:\n", i);
		test();
	}
}
