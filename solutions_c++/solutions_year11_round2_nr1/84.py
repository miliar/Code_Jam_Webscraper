// GCJ 2011 R1B
// wookayin

#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

#define infile "input.txt"
#define outfile "output.txt"

#define REP(i, n) for(int i=0; i<(int)(n); ++i)

using namespace std;

int n;
char stat[101][102];

int games[101];
int wins[101];

double WP[101];double OWP[101];
double OOWP[101];

void go()
{
	REP(i, n) games[i] = 0;
	vector<int> opponent[101];

	memset(wins, 0, sizeof(wins));
	memset(games, 0, sizeof(games));

	REP(i, n) {
		REP(j, n) {
			if(stat[i][j] != '.') {
				games[i]++;
				opponent[i].push_back(j);
			}
			if(stat[i][j] == '1') wins[i]++;
		}
		WP[i] = wins[i] / (double)games[i];
	}

	// OWP
	REP(i, n)
	{
		double s = 0;
		REP(q, opponent[i].size())
		{
			int j = opponent[i][q];
			int new_win = wins[j] - (int)(stat[j][i] == '1');
			int new_games = games[j] - 1;
			s += new_win / (double)new_games;
		}
		s /= opponent[i].size();
		OWP[i] = s;
	}

	// OOWP
	REP(i, n)
	{
		double s = 0;
		REP(q, opponent[i].size())
		{
			s += OWP[ opponent[i][q] ];
		}
		OOWP[i] = s / opponent[i].size();
	}
}

int main()
{
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);

	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; ++tt)
	{
		scanf("%d", &n);
		REP(i, n) scanf("%s", stat[i]);

		go();

		printf("Case #%d:\n", tt);
		
		REP(i, n) {
//			printf("%d: %lf %lf %lf\n", i, WP[i], OWP[i], OOWP[i]);
			printf("%.7lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}
	}
	return 0;
}