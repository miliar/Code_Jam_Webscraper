#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORN(i,a,n) for (int i = (a); i < (a)+(n); ++i)

//#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
//#define SIZE(x) int(x.size())

typedef pair<int,int> PII;
typedef long long ll;

/////////////////////////////////////////////////////////////////////////

char table[105][105];
double WP[105], OWP[105], OOWP[105];
int N;

double wepe(int team, int ignore) {
	int win = 0, play = 0;
	FOR (i, 0, N)
		if (i != ignore) {
			if (table[team][i] != '.')
				play++;
			if (table[team][i] == '1')
				win++;
		}
	return (double)win/(double)play;
}

void Solve(int testcase)
{
	scanf(" %d", &N);

	FOR (i, 0, N)
		scanf(" %s", table[i]);

	/*// games
	memset(games, 0, sizeof(games));
	FOR (i, 0, N)
		FOR (j, 0, N)
			if (tables[i][j] != '.')
				games[i]++;
	*/

	FOR (i, 0, N) {
		// WP
		WP[i] = wepe(i, -1);

		// OWP
		int play = 0;
		double sowp = 0;

		FOR (j, 0, N)
			if (table[i][j] != '.') {
				play++;
				sowp += wepe(j,i);
			}

		OWP[i] = sowp/(double)play;
	}

	FOR (i, 0, N) {

		// OOWP
		int play = 0;
		double soowp = 0;

		FOR (j, 0, N)
			if (table[i][j] != '.') {
				soowp += OWP[j];
				play++;
			}

		OOWP[i] = soowp/(double)play;
	}

	printf("Case #%d:\n", testcase+1);

	FOR (i, 0, N)
		printf("%.16f\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (t, 0, T)
		Solve(t);
	
	return 0;
}
