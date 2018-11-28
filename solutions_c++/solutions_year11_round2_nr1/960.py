/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <set>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair

int T;
int N;
char game[200][200];

double WP(int i)
{
	double A = 0, B = 0;
	REP(j, N) if (game[i][j] != '.')
	{
		B++;
		if (game[i][j] == '1')
			A++;
	}
	return A/B;
}

double OWP(int i)
{
	double A = 0, B = 0;
	REP(j, N) if (game[i][j] != '.')
	{
		B++;
		char temp = game[i][j];
		game[i][j] = game[j][i] = '.';
		A += WP(j);
		game[i][j] = temp;
		if (temp == '1')
			game[j][i] = '0';
		if (temp == '0')
			game[j][i] = '1';
	}
	return A/B;
}

double OOWP(int i)
{
	double A = 0, B = 0;
	REP(j, N) if (game[i][j] != '.')
	{
		B++;
		A += OWP(j);
	}
	return A/B;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d", &N);
		REP(i, N)
			scanf("%s", game[i]);
		printf("Case #%d:\n", tc+1);
		REP(i, N)
			printf("%.10lf\n", WP(i)/4 + OWP(i)/2 + OOWP(i)/4);
		
	}
}
